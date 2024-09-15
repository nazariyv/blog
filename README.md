# blog

template for your personal blog

this is a fork of [Vitalik Buterin's blog](https://github.com/vbuterin/blog)

## to add a new post

simply create a new markdown file in `posts/`, follow the usual rules of writing a markdown file

once you are done, run `publish.py` to generate `index.html`

then, run `publish.py posts/<name-of-your-new-post>` to generate the html for your new post (note that you need to have `pandoc` installed)

## see how it looks locally

To serve this blog locally, just open `site/index.html` in your browser

## hosting

I use fleek.xyz just like Vitalik
