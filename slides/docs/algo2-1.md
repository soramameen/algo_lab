2 Getting Started
This chapter will familiarize you with the framework we shall use throughout the
book to think about the design and analysis of algorithms. It is self-contained, but
it does include several references to material that we introduce in Chapters 3 and 4.
(It also contains several summations, which Appendix A shows how to solve.)
We begin by examining the insertion sort algorithm to solve the sorting problem
introduced in Chapter 1. We define a “pseudocode” that should be familiar to you if
you have done computer programming, and we use it to show how we shall specify
our algorithms. Having specified the insertion sort algorithm, we then argue that it
correctly sorts, and we analyze its running time. The analysis introduces a notation
that focuses on how that time increases with the number of items to be sorted.
Following our discussion of insertion sort, we introduce the divide-and-conquer
approach to the design of algorithms and use it to develop an algorithm called
merge sort. We end with an analysis of merge sort’s running time.
2.1 Insertion sort
Our first algorithm, insertion sort, solves the sorting problem introduced in Chap-
ter 1:
Input: A sequence of n numbers ha1; a2; : : : ; ani.
Output: A permutation (reordering) ha0
1; a0
2; : : : ; a0
niof the input sequence such
that a0
1 a0
2 a0
n.
The numbers that we wish to sort are also known as the keys. Although conceptu-
ally we are sorting a sequence, the input comes to us in the form of an array with n
elements.
In this book, we shall typically describe algorithms as programs written in a
pseudocode that is similar in many respects to C, C++, Java, Python, or Pascal. If
you have been introduced to any of these languages, you should have little trouble
2.1 Insertion sort 17
10
♣ ♣ ♣
♣
5
♣
♣ ♣
4
♣
2
♣ ♣
♣
♣ ♣
♣
7
♣ ♣
♣
♣
♣ ♣
♣ ♣ ♣ ♣
♣ ♣
10
♣ ♣ ♣
♣ ♣ ♣
5
♣ ♣
2
4
♣ ♣
♣ ♣
7
Figure 2.1 Sorting a hand of cards using insertion sort.
reading our algorithms. What separates pseudocode from “real” code is that in
pseudocode, we employ whatever expressive method is most clear and concise to
specify a given algorithm. Sometimes, the clearest method is English, so do not
be surprised if you come across an English phrase or sentence embedded within
a section of “real” code. Another difference between pseudocode and real code
is that pseudocode is not typically concerned with issues of software engineering.
Issues of data abstraction, modularity, and error handling are often ignored in order
to convey the essence of the algorithm more concisely.
We start with insertion sort, which is an efficient algorithm for sorting a small
number of elements. Insertion sort works the way many people sort a hand of
playing cards. We start with an empty left hand and the cards face down on the
table. We then remove one card at a time from the table and insert it into the
correct position in the left hand. To find the correct position for a card, we compare
it with each of the cards already in the hand, from right to left, as illustrated in
Figure 2.1. At all times, the cards held in the left hand are sorted, and these cards
were originally the top cards of the pile on the table.
We present our pseudocode for insertion sort as a procedure called INSERTION-
SORT, which takes as a parameter an array AŒ1 : : n containing a sequence of
length n that is to be sorted. (In the code, the number n of elements in A is denoted
by A:length.) The algorithm sorts the input numbers in place: it rearranges the
numbers within the array A, with at most a constant number of them stored outside
the array at any time. The input array A contains the sorted output sequence when
the INSERTION-SORT procedure is finished.
18 Chapter 2 Getting Started
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
(a)
5 2 4 6 1 3
(b)
2 5 4 6 1 3
(c)
2 4 5 6 1 3
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
(d)
2 4 5 6 1 3
(e)
2 4 5 6
1 3
(f)
1 3
2 4 5 6
Figure 2.2 The operation of INSERTION-SORT on the array A Dh5; 2; 4; 6; 1; 3i. Array indices
appear above the rectangles, and values stored in the array positions appear within the rectangles.
(a)–(e) The iterations of the for loop of lines 1–8. In each iteration, the black rectangle holds the
key taken from AŒj , which is compared with the values in shaded rectangles to its left in the test of
line 5. Shaded arrows show array values moved one position to the right in line 6, and black arrows
indicate where the key moves to in line 8. (f) The final sorted array.
INSERTION-SORT.A/
1 for jD2 to A:length
2 keyDAŒj 
3 // Insert AŒj  into the sorted sequence AŒ1 : : j 1.
4 iDj 1
5 while i > 0 and AŒi  > key
6 AŒi C1DAŒi 
7 iDi 1
8 AŒi C1Dkey
Loop invariants and the correctness of insertion sort
Figure 2.2 shows how this algorithm works for A Dh5; 2; 4; 6; 1; 3i. The in-
dex j indicates the “current card” being inserted into the hand. At the beginning
of each iteration of the for loop, which is indexed by j , the subarray consisting
of elements AŒ1 : : j 1 constitutes the currently sorted hand, and the remaining
subarray AŒj C1 : : n corresponds to the pile of cards still on the table. In fact,
elements AŒ1 : : j 1 are the elements originally in positions 1 through j 1, but
now in sorted order. We state these properties of AŒ1 : : j 1 formally as a loop
invariant:
At the start of each iteration of the for loop of lines 1–8, the subarray
AŒ1 : : j 1 consists of the elements originally in AŒ1 : : j 1, but in sorted
order.
We use loop invariants to help us understand why an algorithm is correct. We
must show three things about a loop invariant:
2.1 Insertion sort 19
Initialization: It is true prior to the first iteration of the loop.
Maintenance: If it is true before an iteration of the loop, it remains true before the
next iteration.
Termination: When the loop terminates, the invariant gives us a useful property
that helps show that the algorithm is correct.
When the first two properties hold, the loop invariant is true prior to every iteration
of the loop. (Of course, we are free to use established facts other than the loop
invariant itself to prove that the loop invariant remains true before each iteration.)
Note the similarity to mathematical induction, where to prove that a property holds,
you prove a base case and an inductive step. Here, showing that the invariant holds
before the first iteration corresponds to the base case, and showing that the invariant
holds from iteration to iteration corresponds to the inductive step.
The third property is perhaps the most important one, since we are using the loop
invariant to show correctness. Typically, we use the loop invariant along with the
condition that caused the loop to terminate. The termination property differs from
how we usually use mathematical induction, in which we apply the inductive step
infinitely; here, we stop the “induction” when the loop terminates.
Let us see how these properties hold for insertion sort.
Initialization: We start by showing that the loop invariant holds before the first
loop iteration, when jD2.
1 The subarray AŒ1 : : j 1, therefore, consists
of just the single element AŒ1, which is in fact the original element in AŒ1.
Moreover, this subarray is sorted (trivially, of course), which shows that the
loop invariant holds prior to the first iteration of the loop.
Maintenance: Next, we tackle the second property: showing that each iteration
maintains the loop invariant. Informally, the body of the for loop works by
moving AŒj 1, AŒj 2, AŒj 3, and so on by one position to the right
until it finds the proper position for AŒj  (lines 4–7), at which point it inserts
the value of AŒj  (line 8). The subarray AŒ1 : : j  then consists of the elements
originally in AŒ1 : : j , but in sorted order. Incrementing j for the next iteration
of the for loop then preserves the loop invariant.
A more formal treatment of the second property would require us to state and
show a loop invariant for the while loop of lines 5–7. At this point, however,
1When the loop is a for loop, the moment at which we check the loop invariant just prior to the first
iteration is immediately after the initial assignment to the loop-counter variable and just before the
first test in the loop header. In the case of INSERTION-SORT, this time is after assigning 2 to the
variable j but before the first test of whether j A: length.
20 Chapter 2 Getting Started
we prefer not to get bogged down in such formalism, and so we rely on our
informal analysis to show that the second property holds for the outer loop.
Termination: Finally, we examine what happens when the loop terminates. The
condition causing the for loop to terminate is that j > A:lengthDn. Because
each loop iteration increases j by 1, we must have jDn C1 at that time.
Substituting n C1 for j in the wording of loop invariant, we have that the
subarray AŒ1 : : n consists of the elements originally in AŒ1 : : n, but in sorted
order. Observing that the subarray AŒ1 : : n is the entire array, we conclude that
the entire array is sorted. Hence, the algorithm is correct.
We shall use this method of loop invariants to show correctness later in this
chapter and in other chapters as well.
Pseudocode conventions
We use the following conventions in our pseudocode.
 Indentation indicates block structure. For example, the body of the for loop that
begins on line 1 consists of lines 2–8, and the body of the while loop that begins
on line 5 contains lines 6–7 but not line 8. Our indentation style applies to
if-else statements2 as well. Using indentation instead of conventional indicators
of block structure, such as begin and end statements, greatly reduces clutter
while preserving, or even enhancing, clarity.3
 The looping constructs while, for, and repeat-until and the if-else conditional
construct have interpretations similar to those in C, C++, Java, Python, and
Pascal.4 In this book, the loop counter retains its value after exiting the loop,
unlike some situations that arise in C++, Java, and Pascal. Thus, immediately
after a for loop, the loop counter’s value is the value that first exceeded the for
loop bound. We used this property in our correctness argument for insertion
sort. The for loop header in line 1 is for jD 2 to A:length, and so when
this loop terminates, jDA:length C1 (or, equivalently, jDn C1, since
n DA:length). We use the keyword to when a for loop increments its loop
2In an if-else statement, we indent else at the same level as its matching if. Although we omit the
keyword then, we occasionally refer to the portion executed when the test following if is true as a
then clause. For multiway tests, we use elseif for tests after the first one.
3Each pseudocode procedure in this book appears on one page so that you will not have to discern
levels of indentation in code that is split across pages.
4Most block-structured languages have equivalent constructs, though the exact syntax may differ.
Python lacks repeat-until loops, and its for loops operate a little differently from the for loops in
this book.
2.1 Insertion sort 21
counter in each iteration, and we use the keyword downto when a for loop
decrements its loop counter. When the loop counter changes by an amount
greater than 1, the amount of change follows the optional keyword by.
 The symbol “//” indicates that the remainder of the line is a comment.
 A multiple assignment of the form iDjDe assigns to both variables i and j
the value of expression e; it should be treated as equivalent to the assignment
jDe followed by the assignment iDj.
 Variables (such as i , j , and key) are local to the given procedure. We shall not
use global variables without explicit indication.
 We access array elements by specifying the array name followed by the in-
dex in square brackets. For example, AŒi  indicates the i th element of the
array A. The notation “: :” is used to indicate a range of values within an ar-
ray. Thus, AŒ1 : : j  indicates the subarray of A consisting of the j elements
AŒ1; AŒ2; : : : ; AŒj .
 We typically organize compound data into objects, which are composed of
attributes. We access a particular attribute using the syntax found in many
object-oriented programming languages: the object name, followed by a dot,
followed by the attribute name. For example, we treat an array as an object
with the attribute length indicating how many elements it contains. To specify
the number of elements in an array A, we write A:length.
We treat a variable representing an array or object as a pointer to the data rep-
resenting the array or object. For all attributes f of an object x, setting yDx
causes y:f to equal x:f . Moreover, if we now set x:fD3, then afterward not
only does x:f equal 3, but y:f equals 3 as well. In other words, x and y point
to the same object after the assignment yDx.
Our attribute notation can “cascade.” For example, suppose that the attribute f
is itself a pointer to some type of object that has an attribute g. Then the notation
x:f:g is implicitly parenthesized as .x:f /:g. In other words, if we had assigned
yDx:f , then x:f:g is the same as y:g.
Sometimes, a pointer will refer to no object at all. In this case, we give it the
special value NIL.
 We pass parameters to a procedure by value: the called procedure receives its
own copy of the parameters, and if it assigns a value to a parameter, the change
is not seen by the calling procedure. When objects are passed, the pointer to
the data representing the object is copied, but the object’s attributes are not. For
example, if x is a parameter of a called procedure, the assignment x Dy within
the called procedure is not visible to the calling procedure. The assignment
x:fD3, however, is visible. Similarly, arrays are passed by pointer, so that
22 Chapter 2 Getting Started
a pointer to the array is passed, rather than the entire array, and changes to
individual array elements are visible to the calling procedure.
 A return statement immediately transfers control back to the point of call in
the calling procedure. Most return statements also take a value to pass back to
the caller. Our pseudocode differs from many programming languages in that
we allow multiple values to be returned in a single return statement.
 The boolean operators “and” and “or” are short circuiting. That is, when we
evaluate the expression “x and y” we first evaluate x. If x evaluates to FALSE,
then the entire expression cannot evaluate to TRUE, and so we do not evaluate y.
If, on the other hand, x evaluates to TRUE, we must evaluate y to determine the
value of the entire expression. Similarly, in the expression “x or y” we eval-
uate the expression y only if x evaluates to FALSE. Short-circuiting operators
allow us to write boolean expressions such as “x ¤NIL and x:fDy” without
worrying about what happens when we try to evaluate x:f when x is NIL.
 The keyword error indicates that an error occurred because conditions were
wrong for the procedure to have been called. The calling procedure is respon-
sible for handling the error, and so we do not specify what action to take.
