[category]: <> (Math)
[date]: <> (2024/01/06)
[title]: <> (The Uncountability of the Cantor Set: A Journey Through Base-3)
[pandoc]: <> (--mathjax)

The Cantor set is one of the most fascinating mathematical objects ever discovered. It's a set that seems to vanish before our eyes as we construct it, yet contains so many points that they cannot be counted - even using infinite counting! Today, we'll explore this remarkable set and prove its uncountability using Georg Cantor's famous diagonalization argument.

## What is the Cantor Set?

The Cantor set is constructed by repeatedly removing the middle third of intervals, starting with the interval $[0,1]$. Let's walk through its construction:

1. Start with the interval $[0,1]$
2. Remove the middle third $(\frac{1}{3}, \frac{2}{3})$, leaving $[0, \frac{1}{3}] \cup [\frac{2}{3}, 1]$
3. Remove the middle third of each remaining interval
4. Continue this process infinitely

After each step, we get a collection of intervals. Let's calculate the first few iterations:

$$
\begin{align*}
\text{Step 0:}\quad & [0,1]\\[3pt]
\text{Step 1:}\quad & [0,\tfrac{1}{3}] \cup [\tfrac{2}{3},1]\\[3pt]
\text{Step 2:}\quad & [0,\tfrac{1}{9}] \cup [\tfrac{2}{9},\tfrac{1}{3}] \cup [\tfrac{2}{3},\tfrac{7}{9}] \cup [\tfrac{8}{9},1]\\[3pt]
\text{Step 3:}\quad & [0,\tfrac{1}{27}] \cup [\tfrac{2}{27},\tfrac{1}{9}] \cup [\tfrac{2}{9},\tfrac{7}{27}] \cup [\tfrac{8}{27},\tfrac{1}{3}]\ \cup\\[2pt]
                    & [\tfrac{2}{3},\tfrac{19}{27}] \cup [\tfrac{20}{27},\tfrac{7}{9}] \cup [\tfrac{8}{9},\tfrac{25}{27}] \cup [\tfrac{26}{27},1]
\end{align*}
$$

Each step keeps the outer thirds of every interval it is given, so the count of intervals doubles while each one shrinks by a factor of 3: at step $n$ there are $2^n$ intervals, each of length $3^{-n}$, for a total length of $\left(\tfrac{2}{3}\right)^n$. That total marches off to 0, which is worth holding on to -- we are about to show that what survives is nonetheless uncountable.

The Cantor set is what remains after infinitely many steps of this process.

## The Plan of Attack

To prove that the Cantor set is uncountable, we'll follow these steps:

1. Convert our intervals into base-3 (ternary) representation
2. Show that the Cantor set consists of all numbers in $[0,1]$ whose ternary expansion contains only 0s and 2s
3. Use Cantor's diagonalization argument to prove uncountability

## Converting Numbers to Different Bases

Before diving into ternary representations, let's understand how to convert numbers between bases. While our proof will only deal with numbers in $[0,1]$ (so we only need to convert fractional parts), understanding both whole and fractional conversions gives us a complete picture.

### Converting Whole Numbers

For whole numbers, we can represent any number as a sum of powers of the base. For example, in base 3 (ternary), each position represents a power of 3:

$$201_3 = 2 \cdot 3^2 + 0 \cdot 3^1 + 1 \cdot 3^0 = 18 + 0 + 1 = 19_{10}$$

More generally, each ternary whole number is of the form

$$x = \sum_k a_k 3^k \text{ where each } a_k \in \{0,1,2\}, \text{ and } k \in \mathbb{N}_0$$

I could never remember the conventional way of converting a whole number to another base, so here is how I do it. Say we want to convert 19 to base 3. Begin by dividing 19 by 3:

$$19 / 3 = 6 \text{ remainder } 1$$

this means that

$$19 = 6 \cdot 3^1 + 1 \cdot 3^0$$

we aren't done yet because $6 \notin \{0, 1, 2\}$, so we continue dividing by 3.

Divide 6 by 3:

$$6 / 3 = 2 \text{ remainder } 0$$

this means that

$$6 = 2 \cdot 3^1 + 0$$

substitute this into the original equation:

$$19 = \left(2 \cdot 3^1 + 0\right) \cdot 3^1 + 1 \cdot 3^0$$

Expand it all out now:

$$19 = 2 \cdot 3^2 + 0 \cdot 3^1 + 1 \cdot 3^0$$

in other words:

$$19_{10} = 201_3$$

### Converting Fractional Parts

For the fractional part (which is what we'll need for our Cantor set proof), the positions to the right of the point are *negative* powers of the base. Just as $0.1_{10}$ means $\frac{1}{10}$, in base 3, $0.1_3$ means $\frac{1}{3}$:

$$0.d_1d_2d_3..._3 = \frac{d_1}{3} + \frac{d_2}{3^2} + \frac{d_3}{3^3} + ... \text{ where each } d_k \in \{0,1,2\}$$

That sum hands us the algorithm. Multiplying by 3 shifts every digit one place to the left, so $d_1$ pops out as the whole-number part and the rest stays behind the point:

$$3 \times 0.d_1d_2d_3..._3 = d_1 . d_2d_3..._3$$

So: multiply by 3, write down the whole part as your next digit, discard it, and repeat with what's left. Let's convert $0.7$:

$$
\begin{align*}
0.7 \times 3 &= \mathbf{2}.1 & \text{write down } 2, \text{ keep } 0.1\\
0.1 \times 3 &= \mathbf{0}.3 & \text{write down } 0, \text{ keep } 0.3\\
0.3 \times 3 &= \mathbf{0}.9 & \text{write down } 0, \text{ keep } 0.9\\
0.9 \times 3 &= \mathbf{2}.7 & \text{write down } 2, \text{ keep } 0.7
\end{align*}
$$

The leftover is $0.7$ again, exactly where we came in, so the digits now repeat forever with period 4:

$$0.7_{10} = 0.20022002..._3 = 0.\overline{2002}_3$$

Let's verify that, since a repeating expansion has a closed form. A block of $n$ digits repeating forever equals the block's value over $3^n - 1$:

$$0.\overline{2002}_3 = \frac{2 \cdot 3^3 + 0 \cdot 3^2 + 0 \cdot 3 + 2}{3^4 - 1} = \frac{56}{80} = \frac{7}{10}$$

Notice how much less hospitable base 3 is to $0.7$ than base 10 is: the expansion never terminates. That isn't bad luck. A fraction in lowest terms terminates in base 3 exactly when its denominator is a power of 3, and $10 = 2 \cdot 5$ shares no factor with 3, so $\frac{7}{10}$ has no choice but to repeat.

Happily, the numbers the Cantor set is built from are the hospitable ones. Every endpoint we will meet -- $\frac{1}{3}$, $\frac{2}{9}$, $\frac{7}{27}$ and their relatives -- has a power of 3 underneath, so each one terminates after just a few ternary digits.

## Our Intervals in Ternary Form

Let's convert some of the Cantor sets' endpoints to base 3. This will reveal a beautiful pattern!

$\frac{1}{3}$ in base 3:
$$
\begin{align*}
0.333333... \times 3 &= 1.0 & \text{ (write down 1)}
\end{align*}
$$
Therefore, $\frac{1}{3}_{10} = 0.1_3$

$\frac{2}{3}$ in base 3:
$$
\begin{align*}
0.666666... \times 3 &= 2.0 & \text{ (write down 2)}
\end{align*}
$$
Therefore, $\frac{2}{3}_{10} = 0.2_3$

$\frac{1}{9}$ in base 3:
$$
\begin{align*}
0.111111... \times 3 &= 0.333333... & \text{ (write down 0)}\\
0.333333... \times 3 &= 1.0 & \text{ (write down 1)}
\end{align*}
$$
Therefore, $\frac{1}{9}_{10} = 0.01_3$

$\frac{2}{9}$ in base 3:
$$
\begin{align*}
0.222222... \times 3 &= 0.666666... & \text{ (write down 0)}\\
0.666666... \times 3 &= 2.0 & \text{ (write down 2)}
\end{align*}
$$
Therefore, $\frac{2}{9}_{10} = 0.02_3$

$\frac{7}{9}$ in base 3:
$$
\begin{align*}
0.777777... \times 3 &= 2.333333... & \text{ (write down 2)}\\
0.333333... \times 3 &= 1.0 & \text{ (write down 1)}
\end{align*}
$$
Therefore, $\frac{7}{9}_{10} = 0.21_3$

$\frac{8}{9}$ in base 3:
$$
\begin{align*}
0.888888... \times 3 &= 2.666666... & \text{ (write down 2)}\\
0.666666... \times 3 &= 2.0 & \text{ (write down 2)}
\end{align*}
$$
Therefore, $\frac{8}{9}_{10} = 0.22_3$

Now our first few intervals in ternary form are:

$$
\begin{align*}
\text{Step 0:}\quad & [0.0_3,\ 0.2222..._3]\\[3pt]
\text{Step 1:}\quad & [0.0_3,\ 0.0222..._3] \cup [0.2_3,\ 0.2222..._3]\\[3pt]
\text{Step 2:}\quad & [0.0_3,\ 0.0022..._3] \cup [0.02_3,\ 0.0222..._3]\ \cup\\[2pt]
                    & [0.2_3,\ 0.2022..._3] \cup [0.22_3,\ 0.2222..._3]
\end{align*}
$$

## The Magic of Base-3: Removing Numbers with 1s

Here's where things get interesting! When we remove the middle third of an interval, we're actually removing all numbers that have a 1 in that position of their ternary expansion.

Let's look at what we remove in each step:

- Step 1: We remove $(\tfrac{1}{3}, \tfrac{2}{3})$, which in base 3 is $(0.1_3, 0.2_3)$
- Step 2: We remove:
  - $(\tfrac{1}{9}, \tfrac{2}{9})$, which is $(0.01_3, 0.02_3)$
  - $(\tfrac{7}{9}, \tfrac{8}{9})$, which is $(0.21_3, 0.22_3)$
- Step 3: We remove intervals like:
  - $(\tfrac{1}{27}, \tfrac{2}{27})$, which is $(0.001_3, 0.002_3)$
  - $(\tfrac{7}{27}, \tfrac{8}{27})$, which is $(0.021_3, 0.022_3)$
  - $(\tfrac{19}{27}, \tfrac{20}{27})$, which is $(0.201_3, 0.202_3)$
  - $(\tfrac{25}{27}, \tfrac{26}{27})$, which is $(0.221_3, 0.222_3)$

In each case, we're removing numbers that have a 1 in the nth position (where n is the step number). This means the Cantor set contains exactly those numbers whose ternary expansion consists only of 0s and 2s!

## The One Catch: Numbers With Two Names

There's a subtlety hiding in that last sentence, and the proof doesn't stand up without it.

Look at $\frac{1}{3}$. The set we remove at step 1 is the **open** interval $(\frac{1}{3}, \frac{2}{3})$, which does not include its own endpoints, so $\frac{1}{3}$ is never removed at any stage. It really is in the Cantor set. Yet we computed above that $\frac{1}{3} = 0.1_3$ -- an expansion with a 1 in it. Both facts can't sit comfortably beside the claim we just made.

The way out is that some numbers have **two** ternary expansions. Alongside $\frac{1}{3} = 0.1000..._3$ we also have

$$0.0222..._3 = \frac{0}{3} + \frac{2}{3^2} + \frac{2}{3^3} + ... = \frac{2/9}{1 - 1/3} = \frac{1}{3}$$

Two different digit strings, one number. This is precisely the base-3 cousin of $0.5 = 0.4999..._{10}$, and it happens for exactly those numbers whose expansion terminates -- the ones of the form $\frac{k}{3^n}$.

So the honest statement of our characterisation is:

> The Cantor set is the set of numbers in $[0,1]$ having **at least one** ternary expansion that uses only 0s and 2s.

$\frac{1}{3}$ makes the cut through its second name, $0.0222..._3$. A number sitting strictly inside a removed middle third has no such escape route: $\frac{1}{2} = 0.1111..._3$ doesn't terminate, so that is its only expansion, and it is stuck with its 1s. Out it goes, as it should.

From here on, whenever a number has two names we'll always choose the one that avoids 1s. With that convention in place, every element of the Cantor set is a string of 0s and 2s, and we can finally count them.

## The Diagonalization Proof

Now we can prove the Cantor set is uncountable. Let's proceed by contradiction.

Suppose the Cantor set is countable. Then we can list all its elements:

$$
\begin{align*}
x_1 &= 0.a_{11}a_{12}a_{13}..._3\\
x_2 &= 0.a_{21}a_{22}a_{23}..._3\\
x_3 &= 0.a_{31}a_{32}a_{33}..._3\\
&\vdots
\end{align*}
$$

where each $a_{ij}$ is either 0 or 2.

We'll construct a number $y$ in the Cantor set that differs from every number in our list. Define $y = 0.b_1b_2b_3..._3$ where:

- $b_n = 0$ if $a_{nn} = 2$
- $b_n = 2$ if $a_{nn} = 0$

Since $y$ contains only 0s and 2s, it's in the Cantor set. However, $y$ differs from each $x_n$ in the nth digit, so it can't be in our list. This contradicts our assumption that we listed all elements of the Cantor set.

There's one gap left to close, and it's exactly where the two-names problem could have bitten us. Differing in a digit only shows the two *strings* are different; what we need is that the two *numbers* are different. Here our convention saves us. For two distinct strings to denote the same number, one would have to end $...a1000...$ and the other $...a0222...$ -- and neither of those is free of 1s. Since every string in play consists only of 0s and 2s, distinct strings must denote distinct numbers, so $y \neq x_n$ as real numbers for every $n$.

Therefore, the Cantor set must be uncountable!

(This is why the familiar "diagonalise the decimals" proof has to be handled with care, and why doing it inside the Cantor set is so much cleaner: banning the digit 1 also bans the ambiguity.)

## Exercises

Have a go at each before unfolding the answer underneath it. The tools are the ones from above: convert to base 3, then ask whether the digits can be made to avoid 1s.

1. **A point you might not expect**:

   Is $\tfrac{1}{4}$ in the Cantor set?

   <details><summary>show answer</summary>

   Run the algorithm:

   $$
   \begin{align*}
   \tfrac{1}{4} \times 3 &= \tfrac{3}{4} = \mathbf{0}.75 & \text{write } 0, \text{ keep } \tfrac{3}{4}\\
   \tfrac{3}{4} \times 3 &= \tfrac{9}{4} = \mathbf{2}.25 & \text{write } 2, \text{ keep } \tfrac{1}{4}
   \end{align*}
   $$

   We're back at $\tfrac{1}{4}$, so $\tfrac{1}{4} = 0.\overline{02}_3$. Checking with the closed form:

   $$\frac{0 \cdot 3 + 2}{3^2 - 1} = \frac{2}{8} = \frac{1}{4}$$

   Only 0s and 2s, so **yes**, $\tfrac{1}{4}$ is in the Cantor set.

   This is the exercise worth doing, because $\tfrac{1}{4}$ is not an endpoint of *any* interval at *any* step -- every endpoint has a power of 3 underneath it, and 4 is not one. So the Cantor set is not merely the endpoints left over from the construction. It contains points that arise as limits, and in fact the endpoints are only countably many, so essentially *all* of the Cantor set is points like this one.

   </details>

2. **A point that goes**:

   Is $\tfrac{1}{2}$ in the Cantor set?

   <details><summary>show answer</summary>

   $\tfrac{1}{2} \times 3 = 1.5$, so the first digit is 1 and $\tfrac{1}{2}$ remains -- the digit is 1 forever, giving $\tfrac{1}{2} = 0.\overline{1}_3$, and indeed $\frac{1}{3-1} = \frac{1}{2}$.

   Could it have a second name, the way $\tfrac{1}{3}$ did? No: two names only exist for expansions that terminate, i.e. numbers of the form $\tfrac{k}{3^n}$. This expansion never terminates, so it's the only one available and it is riddled with 1s. **Not** in the Cantor set.

   No surprise geometrically -- $\tfrac{1}{2}$ is dead centre of $(\tfrac{1}{3}, \tfrac{2}{3})$, so it is the very first thing removed.

   </details>

3. **An endpoint that looks wrong**:

   $\tfrac{7}{9}$ is an endpoint of one of the step-2 intervals, so it is never removed and must be in the Cantor set. But we computed earlier that $\tfrac{7}{9} = 0.21_3$, which contains a 1. Resolve the apparent contradiction.

   <details><summary>show answer</summary>

   $\tfrac{7}{9}$ terminates, so it has a second name. Trade the final 1 for a 0 followed by all 2s:

   $$0.20222..._3 = \tfrac{2}{3} + \tfrac{0}{9} + \left(\tfrac{2}{27} + \tfrac{2}{81} + ...\right) = \tfrac{2}{3} + \frac{2/27}{1 - 1/3} = \tfrac{2}{3} + \tfrac{1}{9} = \tfrac{7}{9}$$

   So

   $$\tfrac{7}{9} = 0.21_3 = 0.20222..._3$$

   and the second name uses only 0s and 2s. **In the set**, and the characterisation survives -- which is exactly why it has to be stated as "*has at least one* expansion using only 0s and 2s" rather than "its expansion uses only 0s and 2s".

   The general trick: any terminating expansion ending in a 1 can be rewritten by dropping that 1 to a 0 and appending 2s forever. It's the same manoeuvre as $0.5 = 0.4999...$ in base 10.

   </details>

4. **How much is left**:

   Add up the total length of everything removed. What does that say about the length of the Cantor set, and how does it sit beside the result we just proved?

   <details><summary>show answer</summary>

   At step $n$ we remove $2^{n-1}$ intervals, each of length $3^{-n}$. Summing over all steps:

   $$\sum_{n=1}^{\infty} \frac{2^{n-1}}{3^n} = \frac{1}{3}\sum_{n=1}^{\infty}\left(\tfrac{2}{3}\right)^{n-1} = \frac{1}{3} \cdot \frac{1}{1 - 2/3} = \frac{1}{3} \cdot 3 = 1$$

   We remove total length 1 from an interval of length 1, so the Cantor set has length -- Lebesgue measure -- **zero**. This agrees with the other count: what survives at step $n$ has total length $\left(\tfrac{2}{3}\right)^n \to 0$.

   Set that beside the theorem and you get the punchline of the whole post: the Cantor set has **zero length yet uncountably many points**. Neither fact softens the other. "Uncountable" and "has some length" turn out to be entirely independent properties, which is precisely why measure theory needs to be built as its own subject rather than read off from cardinality.

   </details>

5. **Why the digit ban matters**:

   Suppose you tried the diagonal argument directly on all of $[0,1]$ in base 10: list the reals, then build $y$ by changing the $n$th decimal digit of the $n$th number. Where does this break, and why doesn't the Cantor set version suffer the same fate?

   <details><summary>show answer</summary>

   It breaks at exactly the step we had to be careful about: differing in every digit does **not** guarantee being a different number. Suppose your rule turns a digit 5 into 4, and the list happens to produce $y = 0.4999...$ while $x_1 = 0.5000...$. Every digit differs, yet $y = x_1$, so the "new" number was on the list after all and no contradiction follows.

   The fix in the real-number proof is to choose replacement digits avoiding 0 and 9, so the ambiguous pairs can never arise. Our version gets this for free: allowing only 0s and 2s already rules out both shapes of a double name, since a clash needs one string ending $...1000...$ and the other $...0222...$, and the digit 1 is banned.

   So banning 1s does double duty -- it characterises the Cantor set *and* removes the one loophole that could sink the diagonal argument. That's what made this the tidy setting for the proof.

   </details>

## Why This Matters

The Cantor set is remarkably counterintuitive. Despite having zero length (its Lebesgue measure is 0), it contains uncountably many points. It's a perfect example of how infinite sets can behave in surprising ways, and it plays a crucial role in topology and analysis.

This uncountability proof also introduces techniques that are useful in many other areas of mathematics. The base-3 representation gives us a concrete way to understand which points are in the Cantor set, while the diagonalization argument is a powerful tool that appears throughout mathematics.

## References

1. <a href="https://people.maths.bris.ac.uk/~maxmr/analysis1/Pickering_EDITED_FINAL.pdf" target="_blank" rel="noopener noreferrer">Representing fractions using different bases</a>
