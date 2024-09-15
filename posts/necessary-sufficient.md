[category]: <> (Math)
[date]: <> (2024/09/14)
[title]: <> (Necessary and sufficient conditions in mathematics)
[pandoc]: <> (--mathjax)

Every so often I need to refresh my memory about the intuitive meaning of the "necessary" and "sufficient" conditions in mathematics. Chances are, you do too. So I'm writing this post to have as clear exposition as possible.

## set view

Let's start with a set view of these concepts.

![set view](../images/necessary-sufficient/venn.png)

To be a _red circle_ it is **necessary** to be a _red shape_. But not **sufficient**! (because you might be a _red square_ or any other _non-circle red shape_).

Similarly, to be a "red circle" it is **necessary** to be a "coloured circle". But not **sufficient**!

Conversely, being a _red circle_ is a **sufficient** condition for being both a _red shape_ and a _coloured circle_. Knowing that a shape is a _red circle_ guarantees that it is a _red shape_ (since all _red circles_ are _red shapes_) and that it is a _coloured circle_ (since all _red circles_ are circles with a colour). In this way, a **sufficient** condition provides enough information to ensure the conclusion.

Also, to be a _red shape_ and a _coloured circle_ is a **necessary** and **sufficient** condition for being a _red circle_.

## logic view

Define any two events: $P$ and $Q$.

"P is a necessary condition for Q" means: $P \Leftarrow Q$

"P is a sufficient condition for Q" means: $P \Rightarrow Q$
