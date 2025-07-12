# tnp-chinese
With the introduction of RP and the removal of the O-levels for the Raffles schools, the annual school rankings for both RI and RGS have hit all-time lows, since the only O-level subject left is Mother Tongue. The teachers have decided that drastic action is required, and without considering the welfare of the students have demanded that remedial Higher Chinese lessons be conducted every night. However, if a teacher works above a certain number of minutes 0 < x ≤ 1,000 per day, the school has to pay that teacher overtime pay, at the rate of $100 per extra minute, since Higher Chinese is a particularly tiring and frustrating subject to teach.

Assume, for just a while, that you're actually trying to help put this nefarious scheme into action. Given a list of the durations (in minutes) of 0 < n ≤ 1,000 day shifts and n night shifts, help to pair up these day and night shifts such that the total amount of overtime pay that the school has to fork out is minimised. Of course, the number of minutes a teacher has to work each day is the sum of the length of his/her day and night shift.

Input

The first line of the input contains the integer 0 < n ≤ 1,000. The second line contains n integers, 0 ≤ D1, D2, ..., Dn ≤ 1,000, representing the lengths of each day shift. The third line contains n integers, 0 ≤ N1, N2, ..., Nn ≤ 1,000, representing the lengths of each night shift. The fourth and last line contains the integer 0 < x ≤ 1,000.

Output

Output the total amount of overtime pay required, in dollars.

Sample Input 1

5
1 2 3 4 6
1 2 3 4 2
5

Sample Output 1

300

Explanation for Sample Output 1

One possible way of arranging the shifts is as such:

1 2 3 4 6
4 3 2 1 2

which would result in 4 shifts of 5 minutes, and 1 shift of 8. Overtime pay is only required for the shift of 8 minutes - which, in this case, is 3 minutes over the limit, and hence $300 must be paid.

Input Format

NA

Constraints

NA

Output Format

NA

Sample Input 0

5
1 2 3 4 6
1 2 3 4 2
5
Sample Output 0

300
Sample Input 1

3
1 2 3
1 2 3
10
Sample Output 1

0



# tnp-LVM


You are designing a virtual machine for a new programming language called Lombok. The Lombok Virtual Machine (LVM) runs an assembler-like machine code. It operates on a stack and a single register.

In detail, the instructions work as follows:

PUSH x: This instruction pushes a given integer onto the stack. If the stack for example looks like this: [2, 3] and the machine executes the instruction PUSH -11,the stack looks like this afterwards: [-11, 2, 3]

STORE: This instruction takes the topmost integer from the stack and stores it in the register. If the stack for example looks like this: [3, 9, 4], the register contains any integer, and the machine executes the instruction STORE, the stack looks like this afterwards: [9, 4] and the register contains the integer 3.

LOAD: This instruction copies the content of the register and pushes it onto the stack. If the register for example contains the integer 6, the stack looks like this: [8, 7], and the machine executes the instruction LOAD, the stack looks like this afterwards: [6, 8, 7], and the register still contains the integer 6.

PLUS: This instruction takes the two topmost integers from the stack, adds them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction PLUS, the stack looks like this afterwards: [5, 4]

TIMES: This instruction takes the two topmost integers from the stack, multiplies them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction TIMES, the stack looks like this afterwards: [6, 4]

IFZERO n: This instruction removes the topmost integer from the stack, and checks if it is equal to 0. If that is the case, it jumps to the nth instruction (start counting at 0). If not, the machine continues as usual with the next instruction. See example below.

DONE: Finally, the DONE instruction prints out the integer on top of the stack, and terminates the program regardless of the following instructions.

Computation starts with the first instruction. Initially, the stack is empty and the register contains the number 0.

Input Format

14
PUSH 5
STORE
LOAD
LOAD
PUSH -1
PLUS
STORE
LOAD
IFZERO 13
LOAD
TIMES
PUSH 0
IFZERO 3
DONE

Constraints

NA

Output Format

120

Sample Input 0

14
PUSH 5
STORE
LOAD
LOAD
PUSH -1
PLUS
STORE
LOAD
IFZERO 13
LOAD
TIMES
PUSH 0
IFZERO 3
DONE
Sample Output 0

120

