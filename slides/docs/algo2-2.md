2.2 Analyzing algorithms
Analyzing an algorithm has come to mean predicting the resources that the algo-
rithm requires. Occasionally, resources such as memory, communication band-
width, or computer hardware are of primary concern, but most often it is compu-
tational time that we want to measure. Generally, by analyzing several candidate
algorithms for a problem, we can identify a most efficient one. Such analysis may
indicate more than one viable candidate, but we can often discard several inferior
algorithms in the process.
Before we can analyze an algorithm, we must have a model of the implemen-
tation technology that we will use, including a model for the resources of that
technology and their costs. For most of this book, we shall assume a generic one-
processor, random-access machine (RAM) model of computation as our imple-
mentation technology and understand that our algorithms will be implemented as
computer programs. In the RAM model, instructions are executed one after an-
other, with no concurrent operations.
Strictly speaking, we should precisely define the instructions of the RAM model
and their costs. To do so, however, would be tedious and would yield little insight
into algorithm design and analysis. Yet we must be careful not to abuse the RAM
model. For example, what if a RAM had an instruction that sorts? Then we could
sort in just one instruction. Such a RAM would be unrealistic, since real computers
do not have such instructions. Our guide, therefore, is how real computers are de-
signed. The RAM model contains instructions commonly found in real computers:
arithmetic (such as add, subtract, multiply, divide, remainder, floor, ceiling), data
movement (load, store, copy), and control (conditional and unconditional branch,
subroutine call and return). Each such instruction takes a constant amount of time.
The data types in the RAM model are integer and floating point (for storing real
numbers). Although we typically do not concern ourselves with precision in this
book, in some applications precision is crucial. We also assume a limit on the size
of each word of data. For example, when working with inputs of size n, we typ-
ically assume that integers are represented by c lg n bits for some constant c 1.
We require c 1 so that each word can hold the value of n, enabling us to index the
individual input elements, and we restrict c to be a constant so that the word size
does not grow arbitrarily. (If the word size could grow arbitrarily, we could store
huge amounts of data in one word and operate on it all in constant time—clearly
an unrealistic scenario.)
24 Chapter 2 Getting Started
Real computers contain instructions not listed above, and such instructions rep-
resent a gray area in the RAM model. For example, is exponentiation a constant-
time instruction? In the general case, no; it takes several instructions to compute xy
when x and y are real numbers. In restricted situations, however, exponentiation is
a constant-time operation. Many computers have a “shift left” instruction, which
in constant time shifts the bits of an integer by k positions to the left. In most
computers, shifting the bits of an integer by one position to the left is equivalent
to multiplication by 2, so that shifting the bits by k positions to the left is equiv-
alent to multiplication by 2k . Therefore, such computers can compute 2k in one
constant-time instruction by shifting the integer 1 by k positions to the left, as long
as k is no more than the number of bits in a computer word. We will endeavor to
avoid such gray areas in the RAM model, but we will treat computation of 2k as a
constant-time operation when k is a small enough positive integer.
In the RAM model, we do not attempt to model the memory hierarchy that is
common in contemporary computers. That is, we do not model caches or virtual
memory. Several computational models attempt to account for memory-hierarchy
effects, which are sometimes significant in real programs on real machines. A
handful of problems in this book examine memory-hierarchy effects, but for the
most part, the analyses in this book will not consider them. Models that include
the memory hierarchy are quite a bit more complex than the RAM model, and so
they can be difficult to work with. Moreover, RAM-model analyses are usually
excellent predictors of performance on actual machines.
Analyzing even a simple algorithm in the RAM model can be a challenge. The
mathematical tools required may include combinatorics, probability theory, alge-
braic dexterity, and the ability to identify the most significant terms in a formula.
Because the behavior of an algorithm may be different for each possible input, we
need a means for summarizing that behavior in simple, easily understood formulas.
Even though we typically select only one machine model to analyze a given al-
gorithm, we still face many choices in deciding how to express our analysis. We
would like a way that is simple to write and manipulate, shows the important char-
acteristics of an algorithm’s resource requirements, and suppresses tedious details.
Analysis of insertion sort
The time taken by the INSERTION-SORT procedure depends on the input: sorting a
thousand numbers takes longer than sorting three numbers. Moreover, INSERTION-
SORT can take different amounts of time to sort two input sequences of the same
size depending on how nearly sorted they already are. In general, the time taken
by an algorithm grows with the size of the input, so it is traditional to describe the
running time of a program as a function of the size of its input. To do so, we need
to define the terms “running time” and “size of input” more carefully.
2.2 Analyzing algorithms 25
The best notion for input size depends on the problem being studied. For many
problems, such as sorting or computing discrete Fourier transforms, the most nat-
ural measure is the number of items in the input—for example, the array size n
for sorting. For many other problems, such as multiplying two integers, the best
measure of input size is the total number of bits needed to represent the input in
ordinary binary notation. Sometimes, it is more appropriate to describe the size of
the input with two numbers rather than one. For instance, if the input to an algo-
rithm is a graph, the input size can be described by the numbers of vertices and
edges in the graph. We shall indicate which input size measure is being used with
each problem we study.
The running time of an algorithm on a particular input is the number of primitive
operations or “steps” executed. It is convenient to define the notion of step so
that it is as machine-independent as possible. For the moment, let us adopt the
following view. A constant amount of time is required to execute each line of our
pseudocode. One line may take a different amount of time than another line, but
we shall assume that each execution of the i th line takes time ci , where ci is a
constant. This viewpoint is in keeping with the RAM model, and it also reflects
how the pseudocode would be implemented on most actual computers.5
In the following discussion, our expression for the running time of INSERTION-
SORT will evolve from a messy formula that uses all the statement costs ci to a
much simpler notation that is more concise and more easily manipulated. This
simpler notation will also make it easy to determine whether one algorithm is more
efficient than another.
We start by presenting the INSERTION-SORT procedure with the time “cost”
of each statement and the number of times each statement is executed. For each
jD2; 3; : : : ; n, where n DA:length, we let tj denote the number of times the
while loop test in line 5 is executed for that value of j . When a for or while loop
exits in the usual way (i.e., due to the test in the loop header), the test is executed
one time more than the loop body. We assume that comments are not executable
statements, and so they take no time.
5There are some subtleties here. Computational steps that we specify in English are often variants
of a procedure that requires more than just a constant amount of time. For example, later in this
book we might say “sort the points by x-coordinate,” which, as we shall see, takes more than a
constant amount of time. Also, note that a statement that calls a subroutine takes constant time,
though the subroutine, once invoked, may take more. That is, we separate the process of calling the
subroutine—passing parameters to it, etc.—from the process of executing the subroutine.
26 Chapter 2 Getting Started
INSERTION-SORT.A/ cost times
1 for jD2 to A:length c1 n
2 keyDAŒj  c2 n 1
3 // Insert AŒj  into the sorted
sequence AŒ1 : : j 1. 0 n 1
4 iDj 1 c4 n 1
5 while i > 0 and AŒi  > key c5 Pn
jD2 tj
6 AŒi C1DAŒi  c6 Pn
jD2.tj 1/
7 iDi 1 c7 Pn
jD2.tj 1/
8 AŒi C1Dkey c8 n 1
The running time of the algorithm is the sum of running times for each state-
ment executed; a statement that takes ci steps to execute and executes n times will
contribute ci n to the total running time.6 To compute T .n/, the running time of
INSERTION-SORT on an input of n values, we sum the products of the cost and
times columns, obtaining
T .n/D c1n Cc2.n 1/ Cc4.n 1/ Cc5
n
X
jD2
tj Cc6
n
X
.tj 1/
jD2
n
Cc7
X
.tj 1/ Cc8.n 1/ :
jD2
Even for inputs of a given size, an algorithm’s running time may depend on
which input of that size is given. For example, in INSERTION-SORT, the best
case occurs if the array is already sorted. For each jD2; 3; : : : ; n, we then find
that AŒi  key in line 5 when i has its initial value of j 1. Thus tj D1 for
jD2; 3; : : : ; n, and the best-case running time is
T .n/D c1n Cc2.n 1/ Cc4.n 1/ Cc5.n 1/ Cc8.n 1/
D .c1 Cc2 Cc4 Cc5 Cc8/n .c2 Cc4 Cc5 Cc8/ :
We can express this running time as an Cb for constants a and b that depend on
the statement costs ci ; it is thus a linear function of n.
If the array is in reverse sorted order—that is, in decreasing order—the worst
case results. We must compare each element AŒj  with each element in the entire
sorted subarray AŒ1 : : j 1, and so tj Dj for jD2; 3; : : : ; n. Noting that
6This characteristic does not necessarily hold for a resource such as memory. A statement that
references m words of memory and is executed n times does not necessarily reference mn distinct
words of memory.
2.2 Analyzing algorithms 27
n
X
jD2
jD
n.n C1/
2
1
and
n
X
.j 1/D
jD2
n.n 1/
2
(see Appendix A for a review of how to solve these summations), we find that in
the worst case, the running time of INSERTION-SORT is
T .n/D c1n Cc2.n 1/ Cc4.n 1/ Cc5 n.n C1/
2
1
Cc6 n.n 1/
2 Cc7 n.n 1/
2 Cc8.n 1/
D c5
c6
c7
2 C
2 C
2 n2 Cc1 Cc2 Cc4 C
c5
c6
c7
2 Cc8n
2
2
.c2 Cc4 Cc5 Cc8/ :
We can express this worst-case running time as an2 Cbn Cc for constants a, b,
and c that again depend on the statement costs ci ; it is thus a quadratic function
of n.
Typically, as in insertion sort, the running time of an algorithm is fixed for a
given input, although in later chapters we shall see some interesting “randomized”
algorithms whose behavior can vary even for a fixed input.
Worst-case and average-case analysis
In our analysis of insertion sort, we looked at both the best case, in which the input
array was already sorted, and the worst case, in which the input array was reverse
sorted. For the remainder of this book, though, we shall usually concentrate on
finding only the worst-case running time, that is, the longest running time for any
input of size n. We give three reasons for this orientation.
 The worst-case running time of an algorithm gives us an upper bound on the
running time for any input. Knowing it provides a guarantee that the algorithm
will never take any longer. We need not make some educated guess about the
running time and hope that it never gets much worse.
 For some algorithms, the worst case occurs fairly often. For example, in search-
ing a database for a particular piece of information, the searching algorithm’s
worst case will often occur when the information is not present in the database.
In some applications, searches for absent information may be frequent.
28 Chapter 2 Getting Started
 The “average case” is often roughly as bad as the worst case. Suppose that we
randomly choose n numbers and apply insertion sort. How long does it take to
determine where in subarray AŒ1 : : j 1 to insert element AŒj ? On average,
half the elements in AŒ1 : : j 1 are less than AŒj , and half the elements are
greater. On average, therefore, we check half of the subarray AŒ1 : : j 1, and
so tj is about j=2. The resulting average-case running time turns out to be a
quadratic function of the input size, just like the worst-case running time.
In some particular cases, we shall be interested in the average-case running time
of an algorithm; we shall see the technique of probabilistic analysis applied to
various algorithms throughout this book. The scope of average-case analysis is
limited, because it may not be apparent what constitutes an “average” input for
a particular problem. Often, we shall assume that all inputs of a given size are
equally likely. In practice, this assumption may be violated, but we can sometimes
use a randomized algorithm, which makes random choices, to allow a probabilistic
analysis and yield an expected running time. We explore randomized algorithms
more in Chapter 5 and in several other subsequent chapters.
Order of growth
We used some simplifying abstractions to ease our analysis of the INSERTION-
SORT procedure. First, we ignored the actual cost of each statement, using the
constants ci to represent these costs. Then, we observed that even these constants
give us more detail than we really need: we expressed the worst-case running time
as an2 Cbn Cc for some constants a, b, and c that depend on the statement
costs ci . We thus ignored not only the actual statement costs, but also the abstract
costs ci.
We shall now make one more simplifying abstraction: it is the rate of growth,
or order of growth, of the running time that really interests us. We therefore con-
sider only the leading term of a formula (e.g., an2), since the lower-order terms are
relatively insignificant for large values of n. We also ignore the leading term’s con-
stant coefficient, since constant factors are less significant than the rate of growth
in determining computational efficiency for large inputs. For insertion sort, when
we ignore the lower-order terms and the leading term’s constant coefficient, we are
left with the factor of n2 from the leading term. We write that insertion sort has a
worst-case running time of ‚.n2/ (pronounced “theta of n-squared”). We shall use
‚-notation informally in this chapter, and we will define it precisely in Chapter 3.
We usually consider one algorithm to be more efficient than another if its worst-
case running time has a lower order of growth. Due to constant factors and lower-
order terms, an algorithm whose running time has a higher order of growth might
take less time for small inputs than an algorithm whose running time has a lower
2.3 Designing algorithms 29
order of growth. But for large enough inputs, a ‚.n2/ algorithm, for example, will
run more quickly in the worst case than a ‚.n3/ algorithm.
Exercises
2.2-1
Express the function n3=1000 100n2 100n C3 in terms of ‚-notation.
2.2-2
Consider sorting n numbers stored in array A by first finding the smallest element
of A and exchanging it with the element in AŒ1. Then find the second smallest
element of A, and exchange it with AŒ2. Continue in this manner for the first n 1
elements of A. Write pseudocode for this algorithm, which is known as selection
sort. What loop invariant does this algorithm maintain? Why does it need to run
for only the first n 1 elements, rather than for all n elements? Give the best-case
and worst-case running times of selection sort in ‚-notation.
2.2-3
Consider linear search again (see Exercise 2.1-3). How many elements of the in-
put sequence need to be checked on the average, assuming that the element being
searched for is equally likely to be any element in the array? How about in the
worst case? What are the average-case and worst-case running times of linear
search in ‚-notation? Justify your answers.
2.2-4
How can we modify almost any algorithm to have a good best-case running time?
