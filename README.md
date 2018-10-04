# The Recursion Theorem: Illustration and examples

The Recursion Theorem states that a program can in effect "handle" its own source code.
Sipser first makes a compelling argument why this challenges our intuition.
It seems that a program would not be able to self reproduce,
since a program that produces a program B must be more complex than program B.
But this is intuition incorrect.

First sipser shows a special case illustrating a similar concept to the Recursion Theorem.  He shows that a program
can in fact print its own source code (or representation),
by having the program SELF be composed of two parts, A and B.
A stores a representation R of B, and B uses this stored representation R<sub>1</sub>
to build a representation R<sub>2</sub>of a program that would store a representation of <sub>R</sub>.
But this is what the representation of A!  So B combines R<sub>1</sub>and R<sub>2</sub>,
which represent A and B respectively, to get a representation of the program SELF as a whole, and prints this.

This is almost identical to the notion of a [quine](https://en.wikipedia.org/wiki/Quine_%28computing%29).
I've implemented an example of Sipser's construction of SELF in `self.py`,
it works in as similar way as python seems to allow.
