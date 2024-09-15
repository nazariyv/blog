# blog

template for your personal blog

this is a fork of [Vitalik Buterin's blog](https://github.com/vbuterin/blog)

## to add a new post

simply create a new markdown file in `posts/`, follow the usual rules of writing a markdown file

to add an image, you need to put it in two places:

1/ in `images/<name-of-your-new-post>/<image-name>`

2/ in `site/images/<name-of-your-new-post>/<image-name>`

once you are done writing the **poast**, run `publish.py` to generate `index.html`

then, run `publish.py posts/<name-of-your-new-post>` to generate the html for your new post (note that you need to have `pandoc` installed)

## see how it looks locally

to server this blog locally, go to `site/` and run `python3 -m http.server`

open a browser tab and go to `http://localhost:8000`

## hosting

I use fleek.xyz just like Vitalik
