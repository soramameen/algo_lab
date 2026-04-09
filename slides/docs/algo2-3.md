2.3 Designing algorithms
We can choose from a wide range of algorithm design techniques. For insertion
sort, we used an incremental approach: having sorted the subarray AŒ1 : : j 1,
we inserted the single element AŒj  into its proper place, yielding the sorted
subarray AŒ1 : : j .
In this section, we examine an alternative design approach, known as “divide-
and-conquer,” which we shall explore in more detail in Chapter 4. We’ll use divide-
and-conquer to design a sorting algorithm whose worst-case running time is much
less than that of insertion sort. One advantage of divide-and-conquer algorithms is
that their running times are often easily determined using techniques that we will
see in Chapter 4.
30 Chapter 2 Getting Started
2.3.1 The divide-and-conquer approach
Many useful algorithms are recursive in structure: to solve a given problem, they
call themselves recursively one or more times to deal with closely related sub-
problems. These algorithms typically follow a divide-and-conquer approach: they
break the problem into several subproblems that are similar to the original prob-
lem but smaller in size, solve the subproblems recursively, and then combine these
solutions to create a solution to the original problem.
The divide-and-conquer paradigm involves three steps at each level of the recur-
sion:
Divide the problem into a number of subproblems that are smaller instances of the
same problem.
Conquer the subproblems by solving them recursively. If the subproblem sizes are
small enough, however, just solve the subproblems in a straightforward manner.
Combine the solutions to the subproblems into the solution for the original prob-
lem.
The merge sort algorithm closely follows the divide-and-conquer paradigm. In-
tuitively, it operates as follows.
Divide: Divide the n-element sequence to be sorted into two subsequences of n=2
elements each.
Conquer: Sort the two subsequences recursively using merge sort.
Combine: Merge the two sorted subsequences to produce the sorted answer.
The recursion “bottoms out” when the sequence to be sorted has length 1, in which
case there is no work to be done, since every sequence of length 1 is already in
sorted order.
The key operation of the merge sort algorithm is the merging of two sorted
sequences in the “combine” step. We merge by calling an auxiliary procedure
MERGE.A; p; q; r/, where A is an array and p, q, and r are indices into the array
such that p q < r. The procedure assumes that the subarrays AŒp : : q and
AŒq C1 : : r are in sorted order. It merges them to form a single sorted subarray
that replaces the current subarray AŒp : : r.
Our MERGE procedure takes time ‚.n/, where n D r p C1 is the total
number of elements being merged, and it works as follows. Returning to our card-
playing motif, suppose we have two piles of cards face up on a table. Each pile is
sorted, with the smallest cards on top. We wish to merge the two piles into a single
sorted output pile, which is to be face down on the table. Our basic step consists
of choosing the smaller of the two cards on top of the face-up piles, removing it
from its pile (which exposes a new top card), and placing this card face down onto
2.3 Designing algorithms 31
the output pile. We repeat this step until one input pile is empty, at which time
we just take the remaining input pile and place it face down onto the output pile.
Computationally, each basic step takes constant time, since we are comparing just
the two top cards. Since we perform at most n basic steps, merging takes ‚.n/
time.
The following pseudocode implements the above idea, but with an additional
twist that avoids having to check whether either pile is empty in each basic step.
We place on the bottom of each pile a sentinel card, which contains a special value
that we use to simplify our code. Here, we use 1as the sentinel value, so that
whenever a card with 1is exposed, it cannot be the smaller card unless both piles
have their sentinel cards exposed. But once that happens, all the nonsentinel cards
have already been placed onto the output pile. Since we know in advance that
exactly r p C1 cards will be placed onto the output pile, we can stop once we
have performed that many basic steps.
MERGE.A; p; q; r/
1 n1 Dq p C1
2 n2 Dr q
3 let LŒ1 : : n1 C1 and RŒ1 : : n2 C1 be new arrays
4 for iD1 to n1
5 LŒi DAŒp Ci 1
6 for jD1 to n2
7 RŒj DAŒq Cj 
8 LŒn1 C1 D1
9 RŒn2 C1 D1
10 iD1
11 jD1
12 for kDp to r
13 if LŒi  RŒj 
14 AŒkDLŒi 
15 iDi C1
16 else AŒkDRŒj 
17 jDj C1
In detail, the MERGE procedure works as follows. Line 1 computes the length n1
of the subarray AŒp : : q, and line 2 computes the length n2 of the subarray
AŒq C1 : : r. We create arrays L and R (“left” and “right”), of lengths n1 C1
and n2 C1, respectively, in line 3; the extra position in each array will hold the
sentinel. The for loop of lines 4–5 copies the subarray AŒp : : q into LŒ1 : : n1,
and the for loop of lines 6–7 copies the subarray AŒq C1 : : r into RŒ1 : : n2.
Lines 8–9 put the sentinels at the ends of the arrays L and R. Lines 10–17, illus-
32 Chapter 2 Getting Started
8
9 10 11 12 13 14 15 16
17
8
9 10 11 12 13 14 15 16
17
A
…
2 4 5 7 1 2 3 6 …
A
…
1
4 5 7 1 2 3 6
…
1 2 3 4
5
1 2 3 6
∞
k
1 2 3 4 5
L R
2 4 5 7 ∞
i j
(a)
8
9 10 11 12 13 14 15 16
17
2 A
5 7 1 2 3 6
…
…
5
k
1 2 3 4 5
1 2 3 4
5
2 3 L R
2 4 5 7
∞
i j
(b)
9 10 11 12 13 14 15 16
61
∞
8
17
A
…
1
1
2 2
7 1 2 3 6
…
k
1 2 3 4 5
L R
2 4 5 7
∞
i j
(c)
1 2 3 4
1 2 3 4
5
2 3 61
∞
2 3 61
∞
k
1 2 3 4 5
L R
2 4 5 7
∞
i j
(d)
Figure 2.3 The operation of lines 10–17 in the call MERGE.A; 9; 12; 16/, when the subarray
AŒ9 : : 16 contains the sequence h2; 4; 5; 7; 1; 2; 3; 6i. After copying and inserting sentinels, the
array L contains h2; 4; 5; 7; 1i, and the array R contains h1; 2; 3; 6; 1i. Lightly shaded positions
in A contain their final values, and lightly shaded positions in L and R contain values that have yet
to be copied back into A. Taken together, the lightly shaded positions always comprise the values
originally in AŒ9 : : 16, along with the two sentinels. Heavily shaded positions in A contain values
that will be copied over, and heavily shaded positions in L and R contain values that have already
been copied back into A. (a)–(h) The arrays A, L, and R, and their respective indices k, i, and j
prior to each iteration of the loop of lines 12–17.
trated in Figure 2.3, perform the r p C1 basic steps by maintaining the following
loop invariant:
At the start of each iteration of the for loop of lines 12–17, the subarray
AŒp : : k 1 contains the k p smallest elements of LŒ1 : : n1 C1 and
RŒ1 : : n2 C1, in sorted order. Moreover, LŒi  and RŒj  are the smallest
elements of their arrays that have not been copied back into A.
We must show that this loop invariant holds prior to the first iteration of the for
loop of lines 12–17, that each iteration of the loop maintains the invariant, and
that the invariant provides a useful property to show correctness when the loop
terminates.
Initialization: Prior to the first iteration of the loop, we have kDp, so that the
subarray AŒp : : k 1 is empty. This empty subarray contains the k pD0
smallest elements of L and R, and since iDjD1, both LŒi  and RŒj  are the
smallest elements of their arrays that have not been copied back into A.
2.3 Designing algorithms 33
8
9 10 11 12 13 14 15 16
17
8
9 10 11 12 13 14 15 16
17
A
…
1
2 2 3 A
1 2 3 6
…
…
5
1
2 2 3 4
2 3 6
…
k
1 2 3 4 5
L R
2 4 5 7
∞
1 2 3 4
2 3 61
i j
(e)
9 10 11 12 13 14 15 16
17
1 2 3 4 5
k
1 2 3 4
5
∞
2 3 8
L R
2 4 5 7
∞
(f)
9 10 11 12 13 14 15 16
61
∞
i j
8
17
A
…
1
2 2 3 4 5 A
3 6
…
5
…
1
2 2 3 4 5
6
6
…
k
1 2 3 4 5
2 4 5 7
L R
∞
1 2 3 4
2 3 61
i j
(g)
9 10 11 12 13 14 15 16
5
∞
k
1 2 3 4 5
2 4 5 7
L R
∞
1 2 3 4
2 3 61
i j
(h)
∞
8
17
A
…
1
2 2 3 4 5
6
7
…
5
k
1 2 3 4 5
L R
2 4 5 7
∞
1 2 3 4
2 3 61
i j
(i)
∞
Figure 2.3, continued (i) The arrays and indices at termination. At this point, the subarray in
AŒ9 : : 16 is sorted, and the two sentinels in L and R are the only two elements in these arrays that
have not been copied into A.
Maintenance: To see that each iteration maintains the loop invariant, let us first
suppose that LŒi  RŒj . Then LŒi  is the smallest element not yet copied
back into A. Because AŒp : : k 1 contains the k p smallest elements, after
line 14 copies LŒi  into AŒk, the subarray AŒp : : k will contain the k p C1
smallest elements. Incrementing k (in the for loop update) and i (in line 15)
reestablishes the loop invariant for the next iteration. If instead LŒi  > RŒj ,
then lines 16–17 perform the appropriate action to maintain the loop invariant.
Termination: At termination, kDr C1. By the loop invariant, the subarray
AŒp : : k 1, which is AŒp : : r, contains the k pDr p C1 smallest
elements of LŒ1 : : n1 C1 and RŒ1 : : n2 C1, in sorted order. The arrays L
and R together contain n1 Cn2 C2Dr p C3 elements. All but the two
largest have been copied back into A, and these two largest elements are the
sentinels.
34 Chapter 2 Getting Started
To see that the MERGE procedure runs in ‚.n/ time, where n Dr p C1,
observe that each of lines 1–3 and 8–11 takes constant time, the for loops of
lines 4–7 take ‚.n1 Cn2/D‚.n/ time,7 and there are n iterations of the for
loop of lines 12–17, each of which takes constant time.
We can now use the MERGE procedure as a subroutine in the merge sort al-
gorithm. The procedure MERGE-SORT.A; p; r/ sorts the elements in the subar-
ray AŒp : : r. If p r, the subarray has at most one element and is therefore
already sorted. Otherwise, the divide step simply computes an index q that par-
titions AŒp : : r into two subarrays: AŒp : : q, containing dn=2eelements, and
AŒq C1 : : r, containing bn=2celements.8
MERGE-SORT.A; p; r/
1 if p < r
2 qDb.p Cr/=2c
3 MERGE-SORT.A; p; q/
4 MERGE-SORT.A; q C1; r/
5 MERGE.A; p; q; r/
To sort the entire sequence A DhAŒ1; AŒ2; : : : ; AŒni, we make the initial call
MERGE-SORT.A; 1; A:length/, where once again A:lengthDn. Figure 2.4 il-
lustrates the operation of the procedure bottom-up when n is a power of 2. The
algorithm consists of merging pairs of 1-item sequences to form sorted sequences
of length 2, merging pairs of sequences of length 2 to form sorted sequences of
length 4, and so on, until two sequences of length n=2 are merged to form the final
sorted sequence of length n.
2.3.2 Analyzing divide-and-conquer algorithms
When an algorithm contains a recursive call to itself, we can often describe its
running time by a recurrence equation or recurrence, which describes the overall
running time on a problem of size n in terms of the running time on smaller inputs.
We can then use mathematical tools to solve the recurrence and provide bounds on
the performance of the algorithm.
7We shall see in Chapter 3 how to formally interpret equations containing ‚-notation.
8The expression dxedenotes the least integer greater than or equal to x, and bxcdenotes the greatest
integer less than or equal to x. These notations are defined in Chapter 3. The easiest way to verify
that setting q to b.p Cr/=2cyields subarrays AŒp : : q and AŒq C1 : : r of sizes dn=2eand bn=2c,
respectively, is to examine the four cases that arise depending on whether each of p and r is odd or
even.
2.3 Designing algorithms 35
sorted sequence
1 2 2 3 4 5 6 7
merge
2 4 5 7 1 2 3 6
merge
merge
2 5 4 7 1 3 2 6
merge
5 2 merge
4 7 merge
1 3 merge
2 6
initial sequence
Figure 2.4 The operation of merge sort on the array A Dh5; 2; 4; 7; 1; 3; 2; 6i. The lengths of the
sorted sequences being merged increase as the algorithm progresses from bottom to top.
A recurrence for the running time of a divide-and-conquer algorithm falls out
from the three steps of the basic paradigm. As before, we let T .n/ be the running
time on a problem of size n. If the problem size is small enough, say n  c
for some constant c, the straightforward solution takes constant time, which we
write as ‚.1/. Suppose that our division of the problem yields a subproblems,
each of which is 1=b the size of the original. (For merge sort, both a and b are 2,
but we shall see many divide-and-conquer algorithms in which a ¤b.) It takes
time T .n=b/ to solve one subproblem of size n=b, and so it takes time aT .n=b/
to solve a of them. If we take D.n/ time to divide the problem into subproblems
and C.n/ time to combine the solutions to the subproblems into the solution to the
original problem, we get the recurrence
T .n/D(‚.1/ aT .n=b/ CD.n/ CC.n/ if n c ;
otherwise :
In Chapter 4, we shall see how to solve common recurrences of this form.
Analysis of merge sort
Although the pseudocode for MERGE-SORT works correctly when the number of
elements is not even, our recurrence-based analysis is simplified if we assume that
36 Chapter 2 Getting Started
the original problem size is a power of 2. Each divide step then yields two subse-
quences of size exactly n=2. In Chapter 4, we shall see that this assumption does
not affect the order of growth of the solution to the recurrence.
We reason as follows to set up the recurrence for T .n/, the worst-case running
time of merge sort on n numbers. Merge sort on just one element takes constant
time. When we have n > 1 elements, we break down the running time as follows.
Divide: The divide step just computes the middle of the subarray, which takes
constant time. Thus, D.n/D‚.1/.
Conquer: We recursively solve two subproblems, each of size n=2, which con-
tributes 2T .n=2/ to the running time.
Combine: We have already noted that the MERGE procedure on an n-element
subarray takes time ‚.n/, and so C.n/D‚.n/.
When we add the functions D.n/ and C.n/ for the merge sort analysis, we are
adding a function that is ‚.n/ and a function that is ‚.1/. This sum is a linear
function of n, that is, ‚.n/. Adding it to the 2T .n=2/ term from the “conquer”
step gives the recurrence for the worst-case running time T .n/ of merge sort:
T .n/D(‚.1/ 2T .n=2/ C‚.n/ if n > 1 : if n D1 ;
(2.1)
In Chapter 4, we shall see the “master theorem,” which we can use to show
that T .n/ is ‚.n lg n/, where lg n stands for log2 n. Because the logarithm func-
tion grows more slowly than any linear function, for large enough inputs, merge
sort, with its ‚.n lg n/ running time, outperforms insertion sort, whose running
time is ‚.n2/, in the worst case.
We do not need the master theorem to intuitively understand why the solution to
the recurrence (2.1) is T .n/D‚.n lg n/. Let us rewrite recurrence (2.1) as
T .n/D(c 2T .n=2/ Ccn if n > 1 ; if n D1 ;
(2.2)
where the constant c represents the time required to solve problems of size 1 as
well as the time per array element of the divide and combine steps.9
9It is unlikely that the same constant exactly represents both the time to solve problems of size 1
and the time per array element of the divide and combine steps. We can get around this problem by
letting c be the larger of these times and understanding that our recurrence gives an upper bound on
the running time, or by letting c be the lesser of these times and understanding that our recurrence
gives a lower bound on the running time. Both bounds are on the order of n lg n and, taken together,
give a ‚.n lg n/ running time.
2.3 Designing algorithms 37
Figure 2.5 shows how we can solve recurrence (2.2). For convenience, we as-
sume that n is an exact power of 2. Part (a) of the figure shows T .n/, which we
expand in part (b) into an equivalent tree representing the recurrence. The cn term
is the root (the cost incurred at the top level of recursion), and the two subtrees of
the root are the two smaller recurrences T .n=2/. Part (c) shows this process carried
one step further by expanding T .n=2/. The cost incurred at each of the two sub-
nodes at the second level of recursion is cn=2. We continue expanding each node
in the tree by breaking it into its constituent parts as determined by the recurrence,
until the problem sizes get down to 1, each with a cost of c. Part (d) shows the
resulting recursion tree.
Next, we add the costs across each level of the tree. The top level has total
cost cn, the next level down has total cost c.n=2/ Cc.n=2/Dcn, the level after
that has total cost c.n=4/ Cc.n=4/ Cc.n=4/ Cc.n=4/Dcn, and so on. In general,
the level i below the top has 2i nodes, each contributing a cost of c.n=2i /, so that
the i th level below the top has total cost 2i c.n=2i /Dcn. The bottom level has n
nodes, each contributing a cost of c, for a total cost of cn.
The total number of levels of the recursion tree in Figure 2.5 is lg n C1, where
n is the number of leaves, corresponding to the input size. An informal inductive
argument justifies this claim. The base case occurs when n D1, in which case the
tree has only one level. Since lg 1D0, we have that lg n C1 gives the correct
number of levels. Now assume as an inductive hypothesis that the number of levels
of a recursion tree with 2i leaves is lg 2i C1Di C1 (since for any value of i ,
we have that lg 2i Di ). Because we are assuming that the input size is a power
of 2, the next input size to consider is 2i C1. A tree with n D2i C1 leaves has
one more level than a tree with 2i leaves, and so the total number of levels is
.i C1/ C1Dlg 2i C1 C1.
To compute the total cost represented by the recurrence (2.2), we simply add up
the costs of all the levels. The recursion tree has lg n C1 levels, each costing cn,
for a total cost of cn.lg n C1/Dcn lg n Ccn. Ignoring the low-order term and
