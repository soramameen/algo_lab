3 Growth of Functions
The order of growth of the running time of an algorithm, defined in Chapter 2,
gives a simple characterization of the algorithm’s efficiency and also allows us to
compare the relative performance of alternative algorithms. Once the input size n
becomes large enough, merge sort, with its ‚.n lg n/ worst-case running time,
beats insertion sort, whose worst-case running time is ‚.n2/. Although we can
sometimes determine the exact running time of an algorithm, as we did for insertion
sort in Chapter 2, the extra precision is not usually worth the effort of computing
it. For large enough inputs, the multiplicative constants and lower-order terms of
an exact running time are dominated by the effects of the input size itself.
When we look at input sizes large enough to make only the order of growth of
the running time relevant, we are studying the asymptotic efficiency of algorithms.
That is, we are concerned with how the running time of an algorithm increases with
the size of the input in the limit, as the size of the input increases without bound.
Usually, an algorithm that is asymptotically more efficient will be the best choice
for all but very small inputs.
This chapter gives several standard methods for simplifying the asymptotic anal-
ysis of algorithms. The next section begins by defining several types of “asymp-
totic notation,” of which we have already seen an example in ‚-notation. We then
present several notational conventions used throughout this book, and finally we
review the behavior of functions that commonly arise in the analysis of algorithms.
3.1 Asymptotic notation
The notations we use to describe the asymptotic running time of an algorithm
are defined in terms of functions whose domains are the set of natural numbers
NDf0; 1; 2; : : :g. Such notations are convenient for describing the worst-case
running-time function T .n/, which usually is defined only on integer input sizes.
We sometimes find it convenient, however, to abuse asymptotic notation in a va-
44 Chapter 3 Growth of Functions
riety of ways. For example, we might extend the notation to the domain of real
numbers or, alternatively, restrict it to a subset of the natural numbers. We should
make sure, however, to understand the precise meaning of the notation so that when
we abuse, we do not misuse it. This section defines the basic asymptotic notations
and also introduces some common abuses.
Asymptotic notation, functions, and running times
We will use asymptotic notation primarily to describe the running times of algo-
rithms, as when we wrote that insertion sort’s worst-case running time is ‚.n2/.
Asymptotic notation actually applies to functions, however. Recall that we charac-
terized insertion sort’s worst-case running time as an2 CbnCc, for some constants
a, b, and c. By writing that insertion sort’s running time is ‚.n2/, we abstracted
away some details of this function. Because asymptotic notation applies to func-
tions, what we were writing as ‚.n2/ was the function an2 Cbn Cc, which in
that case happened to characterize the worst-case running time of insertion sort.
In this book, the functions to which we apply asymptotic notation will usually
characterize the running times of algorithms. But asymptotic notation can apply to
functions that characterize some other aspect of algorithms (the amount of space
they use, for example), or even to functions that have nothing whatsoever to do
with algorithms.
Even when we use asymptotic notation to apply to the running time of an al-
gorithm, we need to understand which running time we mean. Sometimes we are
interested in the worst-case running time. Often, however, we wish to characterize
the running time no matter what the input. In other words, we often wish to make
a blanket statement that covers all inputs, not just the worst case. We shall see
asymptotic notations that are well suited to characterizing running times no matter
what the input.
‚-notation
In Chapter 2, we found that the worst-case running time of insertion sort is
T .n/D‚.n2/. Let us define what this notation means. For a given function g.n/,
we denote by ‚.g.n// the set of functions
‚.g.n// Dff .n/ Wthere exist positive constants c1, c2, and n0 such that
0 c1g.n/ f .n/ c2g.n/ for all n n0g:
1
1Within set notation, a colon means “such that.”
3.1 Asymptotic notation 45
c2g.n/
cg.n/
f .n/
c1g.n/
f .n/
f .n/
cg.n/
n
n
n0
n0
n0 f .n/D‚.g.n// f .n/DO.g.n// f .n/D.g.n//
(a)
(b) (c)
n
Figure 3.1 Graphic examples of the ‚, O, and  notations. In each part, the value of n0 shown
is the minimum possible value; any greater value would also work. (a) ‚-notation bounds a func-
tion to within constant factors. We write f .n/D‚.g.n// if there exist positive constants n0, c1,
and c2 such that at and to the right of n0, the value of f .n/ always lies between c1g.n/ and c2g.n/
inclusive. (b) O-notation gives an upper bound for a function to within a constant factor. We write
f .n/DO.g.n// if there are positive constants n0 and c such that at and to the right of n0, the value
of f .n/ always lies on or below cg.n/. (c) -notation gives a lower bound for a function to within
a constant factor. We write f .n/D.g.n// if there are positive constants n0 and c such that at and
to the right of n0, the value of f .n/ always lies on or above cg.n/.
A function f .n/ belongs to the set ‚.g.n// if there exist positive constants c1
and c2 such that it can be “sandwiched” between c1g.n/ and c2g.n/, for suffi-
ciently large n. Because ‚.g.n// is a set, we could write “f .n/ 2 ‚.g.n//”
to indicate that f .n/ is a member of ‚.g.n//. Instead, we will usually write
“f .n/D‚.g.n//” to express the same notion. You might be confused because
we abuse equality in this way, but we shall see later in this section that doing so
has its advantages.
Figure 3.1(a) gives an intuitive picture of functions f .n/ and g.n/, where
f .n/D‚.g.n//. For all values of n at and to the right of n0, the value of f .n/
lies at or above c1g.n/ and at or below c2g.n/. In other words, for all n n0, the
function f .n/ is equal to g.n/ to within a constant factor. We say that g.n/ is an
asymptotically tight bound for f .n/.
The definition of ‚.g.n// requires that every member f .n/ 2 ‚.g.n// be
asymptotically nonnegative, that is, that f .n/ be nonnegative whenever n is suf-
ficiently large. (An asymptotically positive function is one that is positive for all
sufficiently large n.) Consequently, the function g.n/ itself must be asymptotically
nonnegative, or else the set ‚.g.n// is empty. We shall therefore assume that every
function used within ‚-notation is asymptotically nonnegative. This assumption
holds for the other asymptotic notations defined in this chapter as well.
46 Chapter 3 Growth of Functions
In Chapter 2, we introduced an informal notion of ‚-notation that amounted
to throwing away lower-order terms and ignoring the leading coefficient of the
highest-order term. Let us briefly justify this intuition by using the formal defi-
nition to show that 1
2 n2 3nD‚.n2/. To do so, we must determine positive
constants c1, c2, and n0 such that
1
c1n2 
n2 3n c2n2
2
for all n n0. Dividing by n2 yields
1
3
c1 
2
c2:
n
We can make the right-hand inequality hold for any value of n 1 by choosing any
constant c2 1=2. Likewise, we can make the left-hand inequality hold for any
value of n 7 by choosing any constant c1 1=14. Thus, by choosing c1 D1=14,
c2 D1=2, and n0 D7, we can verify that 1
2 n2 3nD‚.n2/. Certainly, other
choices for the constants exist, but the important thing is that some choice exists.
Note that these constants depend on the function 1
2 n2 3n; a different function
belonging to ‚.n2/ would usually require different constants.
We can also use the formal definition to verify that 6n3 ¤‚.n2/. Suppose
for the purpose of contradiction that c2 and n0 exist such that 6n3 c2n2 for
all n n0. But then dividing by n2 yields n c2=6, which cannot possibly hold
for arbitrarily large n, since c2 is constant.
Intuitively, the lower-order terms of an asymptotically positive function can be
ignored in determining asymptotically tight bounds because they are insignificant
for large n. When n is large, even a tiny fraction of the highest-order term suf-
fices to dominate the lower-order terms. Thus, setting c1 to a value that is slightly
smaller than the coefficient of the highest-order term and setting c2 to a value that
is slightly larger permits the inequalities in the definition of ‚-notation to be sat-
isfied. The coefficient of the highest-order term can likewise be ignored, since it
only changes c1 and c2 by a constant factor equal to the coefficient.
As an example, consider any quadratic function f .n/Dan2 Cbn Cc, where
a, b, and c are constants and a > 0. Throwing away the lower-order terms and
ignoring the constant yields f .n/D‚.n2/. Formally, to show the same thing, we
take the constants c1 Da=4, c2 D7a=4, and n0 D2max.jbj=a; pjcj=a/. You
may verify that 0 c1n2 an2 Cbn Cc c2n2 for all n n0. In general,
for any polynomial p.n/DPd
iD0 ai ni , where the ai are constants and ad > 0, we
have p.n/D‚.nd / (see Problem 3-1).
Since any constant is a degree-0 polynomial, we can express any constant func-
tion as ‚.n0/, or ‚.1/. This latter notation is a minor abuse, however, because the
3.1 Asymptotic notation 47
expression does not indicate what variable is tending to infinity.2 We shall often
use the notation ‚.1/ to mean either a constant or a constant function with respect
to some variable.
O-notation
The ‚-notation asymptotically bounds a function from above and below. When
we have only an asymptotic upper bound, we use O-notation. For a given func-
tion g.n/, we denote by O.g.n// (pronounced “big-oh of g of n” or sometimes
just “oh of g of n”) the set of functions
O.g.n// Dff .n/ Wthere exist positive constants c and n0 such that
0 f .n/ cg.n/ for all n n0g:
We use O-notation to give an upper bound on a function, to within a constant
factor. Figure 3.1(b) shows the intuition behind O-notation. For all values n at and
to the right of n0, the value of the function f .n/ is on or below cg.n/.
We write f .n/DO.g.n// to indicate that a function f .n/ is a member of the
set O.g.n//. Note that f .n/D ‚.g.n// implies f .n/D O.g.n//, since ‚-
notation is a stronger notion than O-notation. Written set-theoretically, we have
‚.g.n// O.g.n//. Thus, our proof that any quadratic function an2 Cbn Cc,
where a > 0, is in ‚.n2/ also shows that any such quadratic function is in O.n2/.
What may be more surprising is that when a > 0, any linear function an Cb is
in O.n2/, which is easily verified by taking c Da Cjbjand n0 Dmax.1; b=a/.
If you have seen O-notation before, you might find it strange that we should
write, for example, n DO.n2/. In the literature, we sometimes find O-notation
informally describing asymptotically tight bounds, that is, what we have defined
using ‚-notation. In this book, however, when we write f .n/DO.g.n//, we
are merely claiming that some constant multiple of g.n/ is an asymptotic upper
bound on f .n/, with no claim about how tight an upper bound it is. Distinguish-
ing asymptotic upper bounds from asymptotically tight bounds is standard in the
algorithms literature.
Using O-notation, we can often describe the running time of an algorithm
merely by inspecting the algorithm’s overall structure. For example, the doubly
nested loop structure of the insertion sort algorithm from Chapter 2 immediately
yields an O.n2/ upper bound on the worst-case running time: the cost of each it-
eration of the inner loop is bounded from above by O.1/ (constant), the indices i
2The real problem is that our ordinary notation for functions does not distinguish functions from
values. In -calculus, the parameters to a function are clearly specified: the function n2 could be
written as n:n2, or even r:r2. Adopting a more rigorous notation, however, would complicate
algebraic manipulations, and so we choose to tolerate the abuse.
48 Chapter 3 Growth of Functions
and j are both at most n, and the inner loop is executed at most once for each of
the n2 pairs of values for i and j.
Since O-notation describes an upper bound, when we use it to bound the worst-
case running time of an algorithm, we have a bound on the running time of the algo-
rithm on every input—the blanket statement we discussed earlier. Thus, the O.n2/
bound on worst-case running time of insertion sort also applies to its running time
on every input. The ‚.n2/ bound on the worst-case running time of insertion sort,
however, does not imply a ‚.n2/ bound on the running time of insertion sort on
every input. For example, we saw in Chapter 2 that when the input is already
sorted, insertion sort runs in ‚.n/ time.
Technically, it is an abuse to say that the running time of insertion sort is O.n2/,
since for a given n, the actual running time varies, depending on the particular
input of size n. When we say “the running time is O.n2/,” we mean that there is a
function f .n/ that is O.n2/ such that for any value of n, no matter what particular
input of size n is chosen, the running time on that input is bounded from above by
the value f .n/. Equivalently, we mean that the worst-case running time is O.n2/.
-notation
Just as O-notation provides an asymptotic upper bound on a function, -notation
provides an asymptotic lower bound. For a given function g.n/, we denote
by .g.n// (pronounced “big-omega of g of n” or sometimes just “omega of g
of n”) the set of functions
.g.n// Dff .n/ Wthere exist positive constants c and n0 such that
0 cg.n/ f .n/ for all n n0g:
Figure 3.1(c) shows the intuition behind -notation. For all values n at or to the
right of n0, the value of f .n/ is on or above cg.n/.
From the definitions of the asymptotic notations we have seen thus far, it is easy
to prove the following important theorem (see Exercise 3.1-5).
Theorem 3.1
For any two functions f .n/ and g.n/, we have f .n/D‚.g.n// if and only if
f .n/DO.g.n// and f .n/D.g.n//.
As an example of the application of this theorem, our proof that an2 Cbn Cc D
‚.n2/ for any constants a, b, and c, where a > 0, immediately implies that
an2 Cbn Cc D.n2/ and an2 Cbn Cc DO.n2/. In practice, rather than using
Theorem 3.1 to obtain asymptotic upper and lower bounds from asymptotically
tight bounds, as we did for this example, we usually use it to prove asymptotically
tight bounds from asymptotic upper and lower bounds.
3.1 Asymptotic notation 49
When we say that the running time (no modifier) of an algorithm is .g.n//,
we mean that no matter what particular input of size n is chosen for each value
of n, the running time on that input is at least a constant times g.n/, for sufficiently
large n. Equivalently, we are giving a lower bound on the best-case running time
of an algorithm. For example, the best-case running time of insertion sort is .n/,
which implies that the running time of insertion sort is .n/.
The running time of insertion sort therefore belongs to both .n/ and O.n2/,
since it falls anywhere between a linear function of n and a quadratic function of n.
Moreover, these bounds are asymptotically as tight as possible: for instance, the
running time of insertion sort is not .n2/, since there exists an input for which
insertion sort runs in ‚.n/ time (e.g., when the input is already sorted). It is not
contradictory, however, to say that the worst-case running time of insertion sort
is .n2/, since there exists an input that causes the algorithm to take .n2/ time.
Asymptotic notation in equations and inequalities
We have already seen how asymptotic notation can be used within mathematical
formulas. For example, in introducing O-notation, we wrote “n DO.n2/.” We
might also write 2n2 C3n C1D2n2 C‚.n/. How do we interpret such formulas?
When the asymptotic notation stands alone (that is, not within a larger formula)
on the right-hand side of an equation (or inequality), as in n DO.n2/, we have
already defined the equal sign to mean set membership: n 2O.n2/. In general,
however, when asymptotic notation appears in a formula, we interpret it as stand-
ing for some anonymous function that we do not care to name. For example, the
formula 2n2 C3n C1D2n2 C‚.n/ means that 2n2 C3n C1D2n2 Cf .n/,
where f .n/ is some function in the set ‚.n/. In this case, we let f .n/D3n C1,
which indeed is in ‚.n/.
Using asymptotic notation in this manner can help eliminate inessential detail
and clutter in an equation. For example, in Chapter 2 we expressed the worst-case
running time of merge sort as the recurrence
T .n/D2T .n=2/ C‚.n/ :
If we are interested only in the asymptotic behavior of T .n/, there is no point in
specifying all the lower-order terms exactly; they are all understood to be included
in the anonymous function denoted by the term ‚.n/.
The number of anonymous functions in an expression is understood to be equal
to the number of times the asymptotic notation appears. For example, in the ex-
pression
n
X
iD1
O.i / ;
50 Chapter 3 Growth of Functions
there is only a single anonymous function (a function of i ). This expression is thus
not the same as O.1/ CO.2/ CCO.n/, which doesn’t really have a clean
interpretation.
In some cases, asymptotic notation appears on the left-hand side of an equation,
as in
2n2 C‚.n/D‚.n2/ :
We interpret such equations using the following rule: No matter how the anony-
mous functions are chosen on the left of the equal sign, there is a way to choose
the anonymous functions on the right of the equal sign to make the equation valid.
Thus, our example means that for any function f .n/ 2‚.n/, there is some func-
tion g.n/ 2‚.n2/ such that 2n2 Cf .n/Dg.n/ for all n. In other words, the
right-hand side of an equation provides a coarser level of detail than the left-hand
side.
We can chain together a number of such relationships, as in
2n2 C3n C1D 2n2 C‚.n/
D ‚.n2/ :
We can interpret each equation separately by the rules above. The first equa-
tion says that there is some function f .n/ 2‚.n/ such that 2n2 C3n C1D
2n2 Cf .n/ for all n. The second equation says that for any function g.n/ 2‚.n/
(such as the f .n/ just mentioned), there is some function h.n/ 2 ‚.n2/ such
that 2n2 Cg.n/D h.n/ for all n. Note that this interpretation implies that
2n2 C3n C1D‚.n2/, which is what the chaining of equations intuitively gives
us.
o-notation
The asymptotic upper bound provided by O-notation may or may not be asymp-
totically tight. The bound 2n2 DO.n2/ is asymptotically tight, but the bound
2nDO.n2/ is not. We use o-notation to denote an upper bound that is not asymp-
totically tight. We formally define o.g.n// (“little-oh of g of n”) as the set
o.g.n// Dff .n/ Wfor any positive constant c > 0, there exists a constant
n0 > 0 such that 0 f .n/ < cg.n/ for all n n0g:
For example, 2nDo.n2/, but 2n2 ¤o.n2/.
The definitions of O-notation and o-notation are similar. The main difference
is that in f .n/DO.g.n//, the bound 0 f .n/ cg.n/ holds for some con-
stant c > 0, but in f .n/Do.g.n//, the bound 0 f .n/ < cg.n/ holds for all
constants c > 0. Intuitively, in o-notation, the function f .n/ becomes insignificant
relative to g.n/ as n approaches infinity; that is,
3.1 Asymptotic notation 51
f .n/
lim
n!1
D0 : (3.1)
g.n/
Some authors use this limit as a definition of the o-notation; the definition in this
book also restricts the anonymous functions to be asymptotically nonnegative.
!-notation
By analogy, !-notation is to -notation as o-notation is to O-notation. We use
!-notation to denote a lower bound that is not asymptotically tight. One way to
define it is by
f .n/ 2!.g.n// if and only if g.n/ 2o.f .n// :
Formally, however, we define !.g.n// (“little-omega of g of n”) as the set
!.g.n// Dff .n/ Wfor any positive constant c > 0, there exists a constant
n0 > 0 such that 0 cg.n/ < f .n/ for all n n0g:
For example, n2=2D!.n/, but n2=2 ¤!.n2/. The relation f .n/D!.g.n//
implies that
f .n/
lim
n!1
g.n/ D1;
if the limit exists. That is, f .n/ becomes arbitrarily large relative to g.n/ as n
approaches infinity.
Comparing functions
Many of the relational properties of real numbers apply to asymptotic comparisons
as well. For the following, assume that f .n/ and g.n/ are asymptotically positive.
Transitivity:
f .n/D‚.g.n// and g.n/D‚.h.n// imply f .n/D‚.h.n// ;
f .n/DO.g.n// and g.n/DO.h.n// imply f .n/DO.h.n// ;
f .n/D.g.n// and g.n/D.h.n// imply f .n/D.h.n// ;
f .n/Do.g.n// and g.n/Do.h.n// imply f .n/Do.h.n// ;
f .n/D!.g.n// and g.n/D!.h.n// imply f .n/D!.h.n// :
Reflexivity:
f .n/D ‚.f .n// ;
f .n/D O.f .n// ;
f .n/D .f .n// :
52 Chapter 3 Growth of Functions
f .n/DO.g.n// is like a b ;
f .n/D.g.n// is like a b ;
f .n/D‚.g.n// is like a Db ;
f .n/Do.g.n// is like a < b ;
f .n/D!.g.n// is like a > b :
Symmetry:
f .n/D‚.g.n// if and only if g.n/D‚.f .n// :
Transpose symmetry:
f .n/DO.g.n// if and only if g.n/D.f .n// ;
f .n/Do.g.n// if and only if g.n/D!.f .n// :
Because these properties hold for asymptotic notations, we can draw an analogy
between the asymptotic comparison of two functions f and g and the comparison
of two real numbers a and b:
We say that f .n/ is asymptotically smaller than g.n/ if f .n/Do.g.n//, and f .n/
is asymptotically larger than g.n/ if f .n/D!.g.n//.
One property of real numbers, however, does not carry over to asymptotic nota-
tion:
Trichotomy: For any two real numbers a and b, exactly one of the following must
hold: a < b, a Db, or a > b.
Although any two real numbers can be compared, not all functions are asymptot-
ically comparable. That is, for two functions f .n/ and g.n/, it may be the case
that neither f .n/DO.g.n// nor f .n/D.g.n// holds. For example, we cannot
compare the functions n and n1Csin n using asymptotic notation, since the value of
the exponent in n1Csin n oscillates between 0 and 2, taking on all values in between.
