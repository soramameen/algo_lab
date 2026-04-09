3.2 Standard notations and common functions
This section reviews some standard mathematical functions and notations and ex-
plores the relationships among them. It also illustrates the use of the asymptotic
notations.
Monotonicity
A function f .n/ is monotonically increasing if m n implies f .m/ f .n/.
Similarly, it is monotonically decreasing if m n implies f .m/ f .n/. A
function f .n/ is strictly increasing if m < n implies f .m/ < f .n/ and strictly
decreasing if m < n implies f .m/ > f .n/.
54 Chapter 3 Growth of Functions
Floors and ceilings
For any real number x, we denote the greatest integer less than or equal to x by bxc
(read “the floor of x”) and the least integer greater than or equal to x by dxe(read
“the ceiling of x”). For all real x,
x 1 < bxc  x  dxe < x C1 : (3.3)
For any integer n,
dn=2eCbn=2cDn ;
and for any real number x 0 and integers a; b > 0,
dx=ae
b D lx
ab m; (3.4)
bx=ac
b D jx
ab k; (3.5)
la
b m
a C.b 1/
b ; (3.6)
ja
b k
a .b 1/
b : (3.7)
The floor function f .x/Dbxcis monotonically increasing, as is the ceiling func-
tion f .x/Ddxe.
Modular arithmetic
For any integer a and any positive integer n, the value a mod n is the remainder
(or residue) of the quotient a=n:
a mod n Da n ba=nc: (3.8)
It follows that
0 a mod n < n : (3.9)
Given a well-defined notion of the remainder of one integer when divided by an-
other, it is convenient to provide special notation to indicate equality of remainders.
If .a mod n/D.b mod n/, we write a b .mod n/ and say that a is equivalent
to b, modulo n. In other words, a b .mod n/ if a and b have the same remain-
der when divided by n. Equivalently, a b .mod n/ if and only if n is a divisor
of b a. We write a 6b .mod n/ if a is not equivalent to b, modulo n.
3.2 Standard notations and common functions 55
Polynomials
Given a nonnegative integer d , a polynomial in n of degree d is a function p.n/
of the form
d
p.n/D
X
ai ni
;
iD0
where the constants a0; a1; : : : ; ad are the coefficients of the polynomial and
ad ¤0. A polynomial is asymptotically positive if and only if ad > 0. For an
asymptotically positive polynomial p.n/ of degree d , we have p.n/D‚.nd /. For
any real constant a 0, the function na is monotonically increasing, and for any
real constant a 0, the function na is monotonically decreasing. We say that a
function f .n/ is polynomially bounded if f .n/DO.nk / for some constant k.
Exponentials
For all real a > 0, m, and n, we have the following identities:
a0
a1
a 1
.am/n
.am/n
aman
D 1 ;
D a ;
D 1=a ;
D amn
;
D .an/m
D amCn
;
:
For all n and a  1, the function an is monotonically increasing in n. When
convenient, we shall assume 00 D1.
We can relate the rates of growth of polynomials and exponentials by the fol-
lowing fact. For all real constants a and b such that a > 1,
nb
lim
n!1
nb
D0 ; (3.10)
an
from which we can conclude that
Do.an/ :
Thus, any exponential function with a base strictly greater than 1 grows faster than
any polynomial function.
Using e to denote 2:71828 : : :, the base of the natural logarithm function, we
have for all real x,
x2
x3
ex
D1 Cx C
2Š C
3Š CD
1
X
iD0
xi
i Š ; (3.11)
56 Chapter 3 Growth of Functions
where “Š” denotes the factorial function defined later in this section. For all real x,
we have the inequality
ex 1 Cx ; (3.12)
where equality holds only when x D0. When jxj1, we have the approximation
1 Cx ex 1 Cx Cx2
: (3.13)
When x !0, the approximation of ex by 1 Cx is quite good:
ex
D1 Cx C‚.x2/ :
(In this equation, the asymptotic notation is used to describe the limiting behavior
as x !0 rather than as x !1.) We have for all x,
lim
n!1 1 C
x
n n
Dex
: (3.14)
Logarithms
We shall use the following notations:
lg n D log2 n (binary logarithm) ,
ln n D loge n (natural logarithm) ,
lgk n D .lg n/k (exponentiation) ,
lg lg n D lg.lg n/ (composition) .
An important notational convention we shall adopt is that logarithm functions will
apply only to the next term in the formula, so that lg n Ck will mean .lg n/ Ck
and not lg.n Ck/. If we hold b > 1 constant, then for n > 0, the function logb n
is strictly increasing.
For all real a > 0, b > 0, c > 0, and n,
a D blogb a
;
logc .ab/D logc a Clogc b ;
logb an
D n logb a ;
logc a
logb a D
logc b ; (3.15)
logb .1=a/D logb a ;
1
logb a D
loga b ;
alogb c
D clogb a
; (3.16)
where, in each equation above, logarithm bases are not 1.
3.2 Standard notations and common functions 57
By equation (3.15), changing the base of a logarithm from one constant to an-
other changes the value of the logarithm by only a constant factor, and so we shall
often use the notation “lg n” when we don’t care about constant factors, such as in
O-notation. Computer scientists find 2 to be the most natural base for logarithms
because so many algorithms and data structures involve splitting a problem into
two parts.
There is a simple series expansion for ln.1 Cx/ when jxj< 1:
x2
x3
x4
x5
ln.1 Cx/Dx
2 C
3
4 C
5
:
We also have the following inequalities for x > 1:
x
 ln.1 Cx/  x ; (3.17)
1 Cx
where equality holds only for x D0.
We say that a function f .n/ is polylogarithmically bounded if f .n/DO.lgk n/
for some constant k. We can relate the growth of polynomials and polylogarithms
by substituting lg n for n and 2a for a in equation (3.10), yielding
lgb n
lgb n
lim
n!1
.2a /lg n
D lim
n!1
D0 :
na
From this limit, we can conclude that
lgb n Do.na/
for any constant a > 0. Thus, any positive polynomial function grows faster than
any polylogarithmic function.
Factorials
The notation nŠ (read “n factorial”) is defined for integers n 0 as
nŠD(1 if n D0 ;
n.n 1/Š if n > 0 :
Thus, nŠD123n.
A weak upper bound on the factorial function is nŠ nn, since each of the n
terms in the factorial product is at most n. Stirling’s approximation,
nŠDp2 n n
e n 1 C‚ 1
n ; (3.18)
58 Chapter 3 Growth of Functions
where e is the base of the natural logarithm, gives us a tighter upper bound, and a
lower bound as well. As Exercise 3.2-3 asks you to prove,
nŠD o.nn/ ;
nŠD !.2n/ ;
lg.nŠ/D ‚.n lg n/ ; (3.19)
where Stirling’s approximation is helpful in proving equation (3.19). The following
equation also holds for all n 1:
nŠDp2 n n
e n
e˛n (3.20)
where
1
< ˛n <
12n C1
1
12n
: (3.21)
Functional iteration
We use the notation f .i /.n/ to denote the function f .n/ iteratively applied i times
to an initial value of n. Formally, let f .n/ be a function over the reals. For non-
negative integers i , we recursively define
f .i /.n/D(n f .f .i 1/.n// if i > 0 :
if iD0 ;
For example, if f .n/D2n, then f .i /.n/D2i n.
The iterated logarithm function
We use the notation lg
n (read “log star of n”) to denote the iterated logarithm, de-
fined as follows. Let lg.i / n be as defined above, with f .n/Dlg n. Because the log-
arithm of a nonpositive number is undefined, lg.i / n is defined only if lg.i 1/ n > 0.
Be sure to distinguish lg.i / n (the logarithm function applied i times in succession,
starting with argument n) from lgi n (the logarithm of n raised to the i th power).
Then we define the iterated logarithm function as
lg
n Dmin ˚i 0 Wlg.i / n 1 :
The iterated logarithm is a very slowly growing function:
lg 2D 1 ;
lg 4D 2 ;
lg 16D 3 ;
lg 65536D 4 ;
lg.265536/D 5 :
3.2 Standard notations and common functions 59
Since the number of atoms in the observable universe is estimated to be about 1080
,
which is much less than 265536, we rarely encounter an input size n such that
lg n > 5.
Fibonacci numbers
We define the Fibonacci numbers by the following recurrence:
F0 D 0 ;
F1 D 1 ; (3.22)
Fi D Fi 1 CFi 2 for i 2 :
Thus, each Fibonacci number is the sum of the two previous ones, yielding the
sequence
0; 1; 1; 2; 3; 5; 8; 13; 21; 34; 55; : : : :
Fibonacci numbers are related to the golden ratio  and to its conjugatey
, which
are the two roots of the equation
x2
Dx C1 (3.23)
and are given by the following formulas (see Exercise 3.2-6):
D
y
D
1 Cp5
2 (3.24)
D 1:61803 : : : ;
1 p5
2
D
:61803 : : : :
Specifically, we have
Fi D
iy
i
p5
;
which we can prove by induction (Exercise 3.2-7). Since ˇˇy
ˇˇ< 1, we have
ˇˇy
i ˇˇ
p5
<
<
1
p5
1
2 ;
which implies that
60 Chapter 3 Growth of Functions
Fi Di
p5
C
1
2 ; (3.25)
which is to say that the i th Fibonacci number Fi is equal to i =p5 rounded to the
nearest integer. Thus, Fibonacci numbers grow exponentially.
