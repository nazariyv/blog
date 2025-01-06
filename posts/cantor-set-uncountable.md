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

- Step 0: $[0,1]$
- Step 1: $[0,\frac{1}{3}] \cup [\frac{2}{3},1]$
- Step 2: $[0,\frac{1}{9}] \cup [\frac{2}{9},\frac{1}{3}] \cup [\frac{2}{3},\frac{7}{9}] \cup [\frac{8}{9},1]$
- Step 3: $[0,\frac{1}{27}] \cup [\frac{2}{27},\frac{1}{9}] \cup [\frac{2}{9},\frac{7}{27}] \cup [\frac{8}{27},\frac{1}{3}] \cup [\frac{2}{3},\frac{19}{27}] \cup [\frac{20}{27},\frac{7}{9}] \cup [\frac{8}{9},\frac{25}{27}] \cup [\frac{26}{27},1]$

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

$201_3 = 2 \cdot 3^2 + 0 \cdot 3^1 + 1 \cdot 3^0 = 18 + 0 + 1 = 19_{10}$

More generally, each ternary whole number is of the form

$$x = \sum_k a_k 3^k \text{ where each } a_k \in \{0,1,2\}, \text{ and } k \in \mathbb{N_0}$$

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

For the fractional part (which is what we'll need for our Cantor set proof), we're essentially dividing by powers of 3. Just as $0.1_{10}$ means $\frac{1}{10}$, in base 3, $0.1_3$ means $\frac{1}{3}$.

To convert a decimal fraction to base 3, we multiply by 3 and look at the whole number part. Let's convert 0.7 to base 3:

$$
\begin{align*}
0.7 \times 3 &= 2.1 \text{ (write down 2)}\\
0.1 \times 3 &= 0.3 \text{ (write down 0)}\\
0.3 \times 3 &= 0.9 \text{ (write down 0)}\\
0.9 \times 3 &= 2.7 \text{ (write down 2)}\\
0.7 \times 3 &= 2.1 \text{ (pattern repeats)}\\
&\vdots
\end{align*}
$$

Therefore, $0.7_{10} = 0.20202..._3$

Each digit in this expansion represents a fraction:
$0.20202..._3 = \frac{2}{3^1} + \frac{0}{3^2} + \frac{2}{3^3} + \frac{0}{3^4} + \frac{2}{3^5} + ...$

This understanding of fractions in base 3 will be crucial for our proof about the Cantor set, as we'll see that every number in the set has a special property in its base-3 representation.

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

- Step 0: $[0.0_3, 0.2222..._3]$
- Step 1: $[0.0_3, 0.0222..._3] \cup [0.2_3, 0.2222..._3]$
- Step 2: $[0.0_3, 0.0022..._3] \cup [0.02_3, 0.0222..._3] \cup [0.2_3, 0.2022..._3] \cup [0.22_3, 0.2222..._3]$

## The Magic of Base-3: Removing Numbers with 1s

Here's where things get interesting! When we remove the middle third of an interval, we're actually removing all numbers that have a 1 in that position of their ternary expansion.

Let's look at what we remove in each step:

- Step 1: We remove $(\frac{1}{3}, \frac{2}{3})$, which in base 3 is $(0.1_3, 0.2_3)$
- Step 2: We remove:
  - $(\frac{1}{9}, \frac{2}{9})$, which is $(0.01_3, 0.02_3)$
  - $(\frac{7}{9}, \frac{8}{9})$, which is $(0.21_3, 0.22_3)$
- Step 3: We remove intervals like:
  - $(\frac{1}{27}, \frac{2}{27})$, which is $(0.001_3, 0.002_3)$
  - $(\frac{7}{27}, \frac{8}{27})$, which is $(0.021_3, 0.022_3)$
  - $(\frac{19}{27}, \frac{20}{27})$, which is $(0.201_3, 0.202_3)$
  - $(\frac{25}{27}, \frac{26}{27})$, which is $(0.221_3, 0.222_3)$

In each case, we're removing numbers that have a 1 in the nth position (where n is the step number). This means the Cantor set contains exactly those numbers whose ternary expansion consists only of 0s and 2s!

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

Therefore, the Cantor set must be uncountable!

## Why This Matters

The Cantor set is remarkably counterintuitive. Despite having zero length (its Lebesgue measure is 0), it contains uncountably many points. It's a perfect example of how infinite sets can behave in surprising ways, and it plays a crucial role in topology and analysis.

This uncountability proof also introduces techniques that are useful in many other areas of mathematics. The base-3 representation gives us a concrete way to understand which points are in the Cantor set, while the diagonalization argument is a powerful tool that appears throughout mathematics.

## References

1. <a href="https://people.maths.bris.ac.uk/~maxmr/analysis1/Pickering_EDITED_FINAL.pdf" target="_blank" rel="noopener noreferrer">Representing fractions using different bases</a>

## TODOs

- re-write the fractional ternary expansion section
