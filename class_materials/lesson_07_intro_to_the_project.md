# Introduction to the Project

We will be working on a group project. The project is a Reverse Polish Notation (RPN) Calculator. Each of you will have a chance to add to the project.

The next portion of the workshop is intended to be a free-form chance for you to experiment with what you have learned by adding to the RPN Calculator project.

# Objectives

Through participating in this session, attendees will be able to:

* Practice the skills you've learned thus far
* Contribute to the RPN Calculator project

# Lecture/Demo

**Infix notation** typically places operators like "+" and "-" are placed between the operands: 4 + 5.

**Reverse polish notation**, on the other hand, places the operator after the operands: 4 5 +.

The following is from the [Reverse Polish Notation wikipedia article](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (with minor modifications) and helps describe the difference between infix notation and reverse polish notation.
 
    The infix expression "5 + ((1 + 2) × 4) − 3" can be written down like this in RPN:
    
    5 1 2 + 4 × + 3 −
    
    The expression is evaluated left-to-right, with the inputs interpreted as shown in the following table (the Stack is the list of values the algorithm is "keeping track of" after the Operation given in the middle column has taken place):


|Input	|Action	|Stack	|Notes|
|:--:|:--|--:|:--|
|5	|Operand	|5|	Push onto stack.|
|1	|Operand	|1 5|	Push onto stack.|
|2	|Operand	|2 1 5|	Push onto stack.|
|+	|Operator	|3 5|	Pop the two operands (1, 2), calculate (1 + 2 = 3) and push the result onto stack.|
|4	|Operand	|4 3 5|	Push onto stack.|
|×	|Operator	|12 5|	Pop the two operands (3, 4), calculate (3 * 4 = 12) and push the result onto stack.|
|+	|Operator	|17|	Pop the two operands (5, 12), calculate (5 + 12 = 17) and push the result onto stack.|
|3	|Operand	|3 17|	Push onto stack.|
|−	|Operator	|14|	Pop the two operands (17, 3), calculate (17 - 3 = 14) and push the result onto stack.|

    Result	14	
    When a computation is finished, its result remains as the top (and only) value in the stack; in this case, 14

## The calculator

The calculator is composed of several parts:

* A calculation engine
* A set of functions (addition, subtraction, etc) that the calculation engine can run
* A set of test functions to ensure that the program works correctly

# Hands-on

You are welcome to add to the project in any way that you would like:

* **add code** to the set of functions to add to the calculator
* **write documentation** to improve the usability of the calculator functions
* **provide bug fixes** if any of the functions are incorrectly implemented
* etc

As each of you add functions, you will need to confirm that you have the latest and greatest code updates from your fellow collaborators.

## Suggested functions

### existing
* + (add)
* / (dividie)

### additional possibilities

#### easier
* multiply = (a * b)
* divide  = (a / b)
* zeros = (a) <- add that many zeros to the stack
* mod = (a, b) <- modulo a % b 

#### mediumer

* lt = (a , b)  <- returns 1 if a is less than b else 0
* gt = (a , b)  <- returns 1 if a is greater than b else 0
* eq = (a == b) <- returns 1 if a is exactly equal to b else 0

* min = (a,b) 
* max = (a,b) 
* sum = (a,b) 

* pi = () <- return pi to some number of decimal places

* fact! = (a) a factorial 

* hypotenuse = (a,b)  <- hypotenuse of a triangle given lengths a and b (i.e. h^2 = a^2 + b^2)

* deg_to_rad ()
* rad_to_deg ()

* cel_to_far ()
* far_to_cel ()

* pounds_to_kg ()
* kg_to_pounds ()

* mph_to_kph ()
* kph_to_mph ()

#### harder

* fib = (length) <- return Fibonacci sequence of given length

* min_of_n = (n) 
* max_of_n = (n) 
* sum_of_n = (n) 

* exp = (a, b) <- exponetial function a^b
* log = (a) <- natural logrithm of a
* log10 = (a) <- log base 10 of a

#### expert
* log_fancy = (a,b) <- log base b of a

* (VERY RISKY) hidden_message = (string, depth)  <-- (depth must be at least 5 elements in, to 'be hidden', and not break code that expects number)





## Choose an issue

* Select an issue in the project tracker<br> 
OR
* Identify something you would like to work on and add an issue to the github repo
* Create a submission (addition, deletion, modification to the project)
* Stage your submission
* Commit your submission
* Push your submission to origin
* Issue a Pull Request<br>
AND then
* Do it all over again...
* And again...

# Resources

[Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

|[<<< Previous Lesson: Git overview](./lesson_05_git_overview.md)|
|:--|
