[category]: <> (Math)
[date]: <> (2024/09/18)
[title]: <> (Implication)
[pandoc]: <> (--mathjax)

I find most explanations of the implication unsatisfactory, personally. This post attempts to motivate the definition of implication, rather than trying to explain it.

---

Why is that dreaded implication **True** when the hypothesis is **False**?

- "Just remember the truth table and use it"
- "It's just a definition"
- "It's a vacuous truth"
- "Becase I haven't broken a promise"

Somehow, none of these answers are satisfactory. Whoever came up with implication must have had a good reason for it. What is it?

I went through a thought experiment to understand this. To my pleasant surprise, I have also stumbled upon an <a href="https://philosophy.lander.edu/logic/conditional.html" target="_blank" rel="noopener noreferrer">article</a> that went through a very similar thought experiment.

Let's begin.

---

Imagine you are a logician coming up with connectives. You are devising a formal logic system that is consistent and complete (at least until Gödel drops a bombshell on you). We already have disjunction and conjunction, but we keep exploring what else we can do. So we want to come up with a new and unique connective that deals with two statements that may be related (but not necessarily). We want to come up with a connective that might tell us something about the conclusion if we know some information about the hypothesis (and they may very well be unrelated).

Let hypothesis be denoted by $P$ and conclusion be denoted by $Q$. Let's also denote the connective by $\implies$ and call it "implication". We start thinking about what the truth table of $P \implies Q$ might look like.

| $P$ | $Q$ | $P \Rightarrow Q$ |
| --- | --- | ----------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | ?                 |
| F   | F   | ?                 |

First two rows are easy. But what about the last two? In a binary (true or false) system we have to pick one of the two. False feels "intuitive". What happens if we pick False for both?

Well, this is just conjunction:

| $P$ | $Q$ | $P \Rightarrow Q$ | $P \land Q$ |
| --- | --- | ----------------- | ----------- |
| T   | T   | **T**             | **T**       |
| T   | F   | **F**             | **F**       |
| F   | T   | **F?**            | **F**       |
| F   | F   | **F?**            | **F**       |

We haven't produced any new concept here, so those two rows certainly aren't both False. Therefore, **at least one of the two rows must resolve to True**. Which one? Let's start with the third row.

| $P$ | $Q$   | $P \Rightarrow Q$ |
| --- | ----- | ----------------- |
| T   | **T** | **T**             |
| T   | **F** | **F**             |
| F   | **T** | **T?**            |
| F   | **F** | **F?**            |

What does this mean? It means that holistically our connective says: "Q whatever is P" or equivalently, quite literally, just "Q", and that's hardly useful. Again, this isn't the right configuration. Alright, perhaps we should pick True for the last row.

| $P$ | $Q$ | $P \Rightarrow Q$ |
| --- | --- | ----------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | F?                |
| F   | F   | T?                |

Intuitively, the last row feels wrong, but we have arrived at exactly this configuration through a rigorous process of thought and after exhausting all other options, so we can't throw it away based on how it "feels". There is something odd however with when $P$ is False, $Q$ is True and implication is False. We have a hypothesis that is False, conclusion that is True, but somehow our implication is still False. If our hypothesis $P$ is "I exercise", and conclusion $Q$ is "I lose weight" and it so happens that I have lost weight but did not exercise (I stopped chugging soda every day) our implication "I exercise => I lose weight" is False, despite me losing weight. This is wrong. We arrive at the only final configuration that must be the one, and as we know: it is. The implication table you all know and love.

| $P$ | $Q$ | $P \Rightarrow Q$ |
| --- | --- | ----------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | T                 |
| F   | F   | T                 |

## Paradoxess

Implication isn't without some peculiarities.

## References

<a href="https://en.wikipedia.org/wiki/Implication_(logic)" target="_blank" rel="noopener noreferrer">implication wikipedia article</a>

<a href="https://www.wikiwand.com/en/articles/Paradoxes_of_material_implication" target="_blank" rel="noopener noreferrer">paradoxes of material implication</a>

<a href="https://www.youtube.com/watch?v=XhQp8suacqI&t=6s" target="_blank" rel="noopener noreferrer">material conditional is permissible</a>

<a href="https://philosophy.lander.edu/logic/conditional.html" target="_blank" rel="noopener noreferrer">an extremely good resource on material conditional</a>
