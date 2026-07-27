#!/usr/bin/python3
import os
import sys
import re
from datetime import datetime, timezone
from email.utils import format_datetime
from xml.sax.saxutils import escape as xml_escape

# The page is assembled as: HEAD_OPEN + <title> + twitter card + HEAD_CLOSE
# + body content + FOOTER. HEAD_CLOSE and FOOTER contain literal braces (JS
# object literals), so nothing here goes through str.format -- the pieces are
# concatenated instead.
HEAD_OPEN = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
"""

HEAD_CLOSE = r"""
<link rel="stylesheet" type="text/css" href="/css/common-vendor.b8ecfc406ac0b5f77a26.css">
<link rel="stylesheet" type="text/css" href="/css/fretboard.f32f2a8d5293869f0195.css">
<link rel="stylesheet" type="text/css" href="/css/pretty.0ae3265014f89d9850bf.css">
<link rel="stylesheet" type="text/css" href="/css/pretty-vendor.83ac49e057c3eac4fce3.css">
<link rel="stylesheet" type="text/css" href="/css/global.css">
<link rel="stylesheet" type="text/css" href="/css/misc.css">

<script>
  MathJax = {
    tex: {
      // the backslashes must be doubled: JS drops the backslash in '\(',
      // which would tell MathJax that inline math is delimited by bare
      // parens and leave pandoc's real \(...\) spans unrendered
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    svg: {
      fontCache: 'global',
    }
  };
</script>
<script
  type="text/javascript"
  id="MathJax-script"
  async
  src="/scripts/tex-svg.js"
></script>
</head>

<body>
  <div
    id="doc"
    class="container-fluid markdown-body comment-enabled"
    data-hard-breaks="true"
  >
    <div id="color-mode-switch">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
        />
      </svg>
      <input type="checkbox" id="switch" />
      <label for="switch">Dark Mode Toggle</label>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
        />
      </svg>
    </div>

    <script type="text/javascript">
      // Update root html class to set CSS colors
      const toggleDarkMode = () => {
        const root = document.querySelector("html");
        root.classList.toggle("dark");
      };

      // Update local storage value for colorScheme
      const toggleColorScheme = () => {
        const colorScheme = localStorage.getItem("colorScheme");
        if (colorScheme === "light")
          localStorage.setItem("colorScheme", "dark");
        else localStorage.setItem("colorScheme", "light");
      };

      // Set toggle input handler
      const toggle = document.querySelector(
        '#color-mode-switch input[type="checkbox"]'
      );
      if (toggle)
        toggle.onclick = () => {
          toggleDarkMode();
          toggleColorScheme();
        };

      // Check for color scheme on init
      const checkColorScheme = () => {
        const colorScheme = localStorage.getItem("colorScheme");
        // Default to light for first view
        if (colorScheme === null || colorScheme === undefined)
          localStorage.setItem("colorScheme", "light");
        // If previously saved to dark, toggle switch and update colors
        if (colorScheme === "dark") {
          toggle.checked = true;
          toggleDarkMode();
        }
      };
      checkColorScheme();
    </script>
"""

FOOTER = """
</div>

<div>
<small>noticed a mistake or have a suggestion? submit a pull request <a href="https://github.com/nazariyv/blog" target="_blank">here</a></small>
</div>

</body>
</html>
"""

TOC_HEADER = """

<br>
<h1>{}</h1>
<br>
<br>
<ul class="post-list">

"""

TOC_FOOTER = """ </ul>
</div>

</body>
</html>
"""

TOC_ITEM_TEMPLATE = """

<li>
    <span class="post-meta">{}</span>
    <h3>
      <a class="post-link" href="{}">{}</a>
    </h3>
</li>

"""

TWITTER_CARD_TEMPLATE = """
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{}" />
<meta name="twitter:image" content="{}" />
"""

FEED_TEMPLATE = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>{title}</title>
  <link>{domain}/</link>
  <description>{title}</description>
  <image>
      <url>{icon}</url>
      <title>{title}</title>
      <link>{domain}/</link>
  </image>
{items}
</channel>
</rss>
"""

FEED_ITEM_TEMPLATE = """
<item>
<title>{title}</title>
<link>{url}</link>
<guid>{url}</guid>
<pubDate>{pubdate}</pubDate>
<description>{description}</description>
</item>
"""


def extract_metadata(fil, filename=None):
    metadata = {}
    if filename:
        assert filename[-3:] == '.md'
        metadata["filename"] = filename[:-3]+'.html'
    while True:
        line = fil.readline()
        if line and line[0] == '[' and ']' in line:
            key = line[1:line.find(']')]
            value_start = line.index('(')+1
            value_end = line.index(')')
            metadata[key] = line[value_start:value_end]
        else:
            break
    return metadata


def metadata_to_path(metadata):
    return os.path.join(metadata['category'].lower(), metadata['date'], metadata['filename'])


def post_url_path(metadata):
    """Site-relative URL for a post. vercel.json sets cleanUrls, so the URL
    drops the .html that the file on disk keeps."""
    return os.path.join('/', metadata_to_path(metadata)).removesuffix('.html')


def make_twitter_card(metadata, global_config):
    return TWITTER_CARD_TEMPLATE.format(metadata['title'], global_config['icon'])


def make_head(title, twitter_card):
    return HEAD_OPEN + '<title>{}</title>\n'.format(title) + twitter_card + HEAD_CLOSE


def make_post_header(metadata):
    year, month, day = metadata['date'].split('/')
    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'[int(month)*3-3:][:3]
    return f"""
<br>
<h1 style="margin-bottom:7px"> {metadata['title']} </h1>
<small style="float:left; color: #888"> {year} {month} {day} </small>
<small style="float:right; color: #888"><a href="/">See all posts</a></small>
<br> <br> <br>
"""


def defancify(text):
    return text \
        .replace("’", "'") \
        .replace('“', '"') \
        .replace('”', '"') \
        .replace('…', '...') \


def make_toc_item(metadata):
    year, month, day = metadata['date'].split('/')
    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'[int(month)*3-3:][:3]
    return TOC_ITEM_TEMPLATE.format(
        year+' '+month+' '+day, post_url_path(metadata), metadata['title'])


def update_image_srcs(html_content):
    # This regex looks for img tags with src attributes starting with "../images/"
    pattern = r'<img[^>]*src=["\']\.\.\/images\/([^"\']+)["\']'

    # This function will be called for each match
    def replace_src(match):
        return match.group(0).replace("../images/", "/images/")

    # Replace all matching src attributes
    return re.sub(pattern, replace_src, html_content)


def unwrap_summary(html_content):
    """pandoc parses the inside of a <details> block as markdown, which leaves
    <summary> wrapped in a paragraph. A <summary> inside a <p> is not a valid
    child of <details>, so the browser stops treating it as the disclosure
    label and renders it as ordinary text. Strip the wrapping <p>."""
    return re.sub(r'<p>\s*(<summary>.*?</summary>)\s*</p>', r'\1',
                  html_content, flags=re.DOTALL)


# Feed descriptions are plain text, so the little inline TeX that shows up in
# opening paragraphs is rendered as the symbol it stands for rather than left
# as a backslash command.
TEX_TO_TEXT = {
    r'\Rightarrow': '⇒', r'\implies': '⇒',
    r'\Leftarrow': '⇐', r'\impliedby': '⇐',
    r'\Leftrightarrow': '⇔', r'\iff': '⇔',
    r'\land': '∧', r'\lor': '∨', r'\neg': '¬',
    r'\subseteq': '⊆', r'\subset': '⊂', r'\cup': '∪',
    r'\cap': '∩', r'\in': '∈', r'\notin': '∉',
    r'\neq': '≠', r'\leq': '≤', r'\geq': '≥',
    r'\cdot': '·', r'\times': '×', r'\ldots': '...',
    r'\mathbb{N}': 'ℕ', r'\mathbb{R}': 'ℝ',
}


def detex(text):
    """Turn the inline math in a paragraph into readable plain text."""
    def render(match):
        body = match.group(1)
        for command, symbol in TEX_TO_TEXT.items():
            body = body.replace(command, symbol)
        return re.sub(r'\s+', ' ', body).strip()
    return re.sub(r'\$([^$]+)\$', render, text)


def first_paragraph(file_location):
    """First prose paragraph of a post, used as the feed description."""
    with open(file_location) as fil:
        extract_metadata(fil)          # skip the [key]: <> (value) block
        for line in fil:
            line = line.strip()
            if line and not line.startswith(('#', '>', '-', '!', '|', '[')):
                # strip the markdown that would be noise in a feed reader
                line = re.sub(r'<[^>]+>', '', line)
                line = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
                line = re.sub(r'[_*`]', '', line)
                return defancify(detex(line))
    return ''


def make_feed(metadatas, global_config):
    domain = global_config['domain'].rstrip('/')
    items = []
    for metadata in metadatas:
        year, month, day = (int(p) for p in metadata['date'].split('/'))
        pubdate = format_datetime(
            datetime(year, month, day, tzinfo=timezone.utc))
        items.append(FEED_ITEM_TEMPLATE.format(
            title=xml_escape(metadata['title']),
            url=xml_escape(domain + post_url_path(metadata)),
            pubdate=pubdate,
            description=xml_escape(metadata.get('description', '')),
        ))
    return FEED_TEMPLATE.format(
        title=xml_escape(global_config['title']),
        domain=xml_escape(domain),
        icon=xml_escape(global_config['icon']),
        items=''.join(items),
    )


if __name__ == '__main__':
    # Get blog config
    global_config = extract_metadata(open('config.md'))

    # Normal case: process each provided file
    for file_location in sys.argv[1:]:
        filename = os.path.split(file_location)[1]
        print("Processing file: {}".format(filename))

        # Extract path
        metadata = extract_metadata(open(file_location), filename)
        path = metadata_to_path(metadata)
        print("Path selected: {}".format(path))

        # Make sure target directory exists
        truncated_path = os.path.split(path)[0]
        os.makedirs(os.path.join('site', truncated_path), exist_ok=True)

        # Generate the html file
        out_location = os.path.join('site', path)
        options = metadata.get('pandoc', '')

        os.system('pandoc -o /tmp/temp_output.html {} {}'.format(file_location, options))
        temp_content = open('/tmp/temp_output.html').read()
        processed_content = unwrap_summary(update_image_srcs(temp_content))
        total_file_contents = (
            make_head(metadata['title'], make_twitter_card(metadata, global_config)) +
            make_post_header(metadata) +
            defancify(processed_content) +
            FOOTER
        )

        # Put it in the desired location
        open(out_location, 'w').write(total_file_contents)

    # Reset ToC
    metadatas = []
    for filename in sorted(os.listdir('posts')):
        if filename.endswith('.md'):
            file_location = os.path.join('posts', filename)
            metadata = extract_metadata(open(file_location), filename)
            metadata['description'] = first_paragraph(file_location)
            metadatas.append(metadata)

    sorted_metadatas = sorted(metadatas, key=lambda x: x['date'], reverse=True)
    toc_items = [make_toc_item(metadata) for metadata in sorted_metadatas]

    toc = (
        make_head(global_config['title'],
                  make_twitter_card(global_config, global_config)) +
        TOC_HEADER.format(global_config['title']) +
        ''.join(toc_items) +
        TOC_FOOTER
    )

    open('site/index.html', 'w').write(toc)

    # Regenerate the feed so it can never drift from the posts
    open('site/feed.xml', 'w').write(make_feed(sorted_metadatas, global_config))
    print("Wrote site/index.html and site/feed.xml ({} posts)".format(len(sorted_metadatas)))
