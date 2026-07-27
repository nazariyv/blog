# blog

template for your personal blog

this is a fork of [Vitalik Buterin's blog](https://github.com/vbuterin/blog)

## to add a new post

simply create a new markdown file in `posts/`, follow the usual rules of writing a markdown file

to add an image, you need to put it in two places:

1/ in `images/<name-of-your-new-post>/<image-name>`

2/ in `site/images/<name-of-your-new-post>/<image-name>`

once you are done writing the **poast**, run (note that you need to have `pandoc` installed):

```sh
python3 publish.py posts/<name-of-your-new-post>.md
```

that renders the post into `site/<category>/<yyyy>/<mm>/<dd>/` **and** regenerates `site/index.html`, so it is the only command you need — the `.md` extension is required

to rebuild everything: `python3 publish.py posts/*.md`

## see how it looks locally

```sh
npx vercel dev
```

then open `http://localhost:3000`

`python3 -m http.server` from inside `site/` also works, but it doesn't implement
vercel's `cleanUrls`, so the extensionless links on the homepage will 404 — use
`vercel dev` if you want a preview that matches production

## hosting

hosted on vercel at [blog.naz.ooo](https://blog.naz.ooo). pushing to `main` deploys.

`vercel.json` points vercel at `site/` as the output directory and there is no
build step — the generated html is committed to the repo and served as-is, so
**always commit `site/` along with your post**
