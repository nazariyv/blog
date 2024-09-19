[category]: <> (Math)
[date]: <> (2024/09/18)
[title]: <> (Implication)
[pandoc]: <> (--mathjax)

I find most explanations of the implication unsatisfactory, personally. This post attempts to motivate the definition of implication, rather than trying to explain it.

---

In mathematical logic, implication is a logical operation typically denoted as $P \Rightarrow Q$, which can be read as "if $P$, then $Q$". It's a fundamental concept that forms the basis of many logical arguments and proofs. However, its definition often leads to confusion, particularly when the hypothesis is false.

Why is that dreaded implication **true** when the hypothesis is **false**?

Common explanations include:

- "Just remember the truth table and use it"
- "It's just a definition"
- "It's a vacuous truth"
- "Because I haven't broken a promise"

Somehow, none of these answers are satisfactory. Whoever came up with implication must have had a good reason for it. What is it?

I went through a thought experiment to understand this. To my pleasant surprise, I have also stumbled upon an <a href="https://philosophy.lander.edu/logic/conditional.html" target="_blank" rel="noopener noreferrer">article</a> that went through a very similar thought experiment.

Let's begin.

---

Imagine you are a logician coming up with connectives. You are devising a formal logic system that is consistent and complete (at least until Gödel drops a bombshell on you). We already have negation, disjunction and conjunction, but we keep exploring what else we can do. So we want to come up with a new and unique connective that deals with two statements that may be related (but not necessarily). We want to come up with a connective that might tell us something about the conclusion if we know some information about the hypothesis (and they may very well be unrelated).

Let hypothesis be denoted by $P$ and conclusion be denoted by $Q$. Let's also denote the connective by $\implies$ and call it "implication". We start thinking about what the truth table of $P \implies Q$ might look like.

| $P$ | $Q$ | $P \Rightarrow Q$ |
| --- | --- | ----------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | ?                 |
| F   | F   | ?                 |

The first two rows are easy to determine. When $P$ is true and $Q$ is true, the implication is clearly true - if the hypothesis is true and the conclusion is true, the implication holds. When $P$ is true and $Q$ is false, the implication must be false - if the hypothesis is true but the conclusion is false, the implication doesn't hold.

But what about the last two? In a binary (true or false) system we have to pick one of the two. false feels "intuitive". What happens if we pick false for both?

Well, this is just conjunction:

| $P$ | $Q$ | $P \Rightarrow Q$ | $P \land Q$ |
| --- | --- | ----------------- | ----------- |
| T   | T   | **T**             | **T**       |
| T   | F   | **F**             | **F**       |
| F   | T   | **F?**            | **F**       |
| F   | F   | **F?**            | **F**       |

We haven't produced any new concept here, so those two rows certainly aren't both false. Therefore, **at least one of the two rows must resolve to true**. Which one? Let's start with the third row.

| $P$ | $Q$   | $P \Rightarrow Q$ |
| --- | ----- | ----------------- |
| T   | **T** | **T**             |
| T   | **F** | **F**             |
| F   | **T** | **T?**            |
| F   | **F** | **F?**            |

What does this mean? It means that holistically our connective says: "$Q$ whatever is $P$" or equivalently, quite literally, just "$Q$", and that's hardly useful. Again, this isn't the right configuration. Alright, perhaps we should pick true for the last row.

| $P$ | $Q$ | $P \Rightarrow Q$ |
| --- | --- | ----------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | F?                |
| F   | F   | T?                |

Intuitively, the last row feels wrong, but we have arrived at exactly this configuration through a rigorous process of thought and after exhausting all other options, so we can't throw it away based on how it "feels". There is something odd however with when $P$ is false, $Q$ is true and implication is false. We have a hypothesis that is false, conclusion that is true, but somehow our implication is still false. If our hypothesis $P$ is "I exercise", and conclusion $Q$ is "I lose weight" and it so happens that I have lost weight but did not exercise (I stopped chugging soda every day) our implication "I exercise => I lose weight" is false, despite me losing weight. This is wrong. We arrive at the only final configuration that must be the one, and as we know: it is. The implication table you all know and love.

| $P$ | $Q$ | $P \Rightarrow Q$ |
| --- | --- | ----------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | T                 |
| F   | F   | T                 |

## paradoxes

Implication isn't without some peculiarities. Two classes of paradoxes arise from the definition of implication. Note, however, that paradoxes do not imply inconsistency (when you can prove both the statement and its negation). They are just unintuitive.

1. Paradoxes arising when the hypothesis is false.
   - Whenever the hypothesis is false, the whole conditional is true, regardless of the conclusion.
   - This leads to counterintuitive results like "If moon is made of cheese, then life exists on other planets" being considered true.
2. Paradoxes arising when the conclusion is true.
   - Whenever the conclusion is true, the conditional is true, regardless of the hypothesis.
   - This leads to counterintuitive results like "If life exists on other planets, then life exists on earth" being considered true.

These paradoxes stem from the truth table definition of material implication, where the conditional is only false when the hypothesis is true and the conclusion is false. In all other cases, including when the hypothesis is false or the conclusion is true, the conditional is considered true.

These are called "paradoxes" not because they lead to logical contradictions, but because they violate our intuitive understanding of "if-then" statements in everyday language. In natural language, we often assume a causal or relevant connection between the "if" part and the "then" part, which isn't necessarily the case in mathematical logic. This disconnect between formal logic and intuitive reasoning is what makes these situations feel paradoxical, even though they're logically consistent within the framework of material implication.

These paradoxes arise from trying to use material implication to capture all uses of "if...then" statements in natural language, when it is just one specific type of implication that does not always align with colloquial usage (if you are interested, try researching <a href="https://en.wikipedia.org/wiki/Non-classical_logic" target="_blank" rel="noopener noreferrer">"non-classical logic"</a>).

## conclusion

Understanding implication is crucial in logic and mathematics. It forms the basis of many logical arguments, proofs, and deductions. While its definition might seem counterintuitive at first, especially when the hypothesis is false, we've seen that it arises naturally when we try to create a logical operator that relates two statements in a meaningful way.

The seeming paradoxes of implication highlight the difference between formal logical systems and our intuitive reasoning. By understanding these nuances, we can use implication more effectively in formal logic while being aware of its limitations when applied to natural language.

Remember, in the realm of mathematical logic, implication is a precisely defined concept that behaves in ways that might not always align with our everyday understanding of "if-then" statements. This precision is what makes it so powerful in formal reasoning, even if it sometimes leads to results that feel paradoxical.

## references

<a href="https://en.wikipedia.org/wiki/Implication_(logic)" target="_blank" rel="noopener noreferrer">implication wikipedia article</a>

<a href="https://www.wikiwand.com/en/articles/Paradoxes_of_material_implication" target="_blank" rel="noopener noreferrer">paradoxes of material implication</a>

<a href="https://www.youtube.com/watch?v=XhQp8suacqI&t=6s" target="_blank" rel="noopener noreferrer">material conditional is permissible</a>

<a href="https://philosophy.lander.edu/logic/conditional.html" target="_blank" rel="noopener noreferrer">an extremely good resource on material conditional</a>
