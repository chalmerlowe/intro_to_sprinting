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

## Awesome functions

Functions are great! They get things done, but the calculator only has a couple of existing functions!

Let's give it some more power!

### Existing

Name	| Operator	| Description
-----|:--------:|------------|
add | + | adds **a** and **b**
divide | / | divide **a** by **b**

Here **a** and **b** are shorthand for 'the most recent numbers on the stack'.

The function's output will replace **a** and **b** in the stack.

### Additional possibilities..

#### Easier

Name	| Operator	| Description
-----|:--------:|------------|
multiply | * | multiply **a** and **b**
subtract | - | take **b** from **a**
zeros | zeros |  push **n** zeros to the stack
modulo | % | **a** mod **b**

(pro tip) modulo might be a [new concept](https://en.wikipedia.org/wiki/Modular_arithmetic) but is easy to implement

#### Mediumer

Some of these functions are asking 'logical questions' which have
yes or no answers (yes = 1 and no = 0).

Name	| Operator	| Description
-----|:--------:|------------|
less_than | lt | is **a** less than **b**?
greater_than | gt | is **a** greater than **b**?
equal_to | eq | is **a** equal to **b**?
minimum | min | return smallest value, i.e. either **a** or **b**
maximum | max | return largest value, i.e. either **a** or **b**
pi | pi | return pi (e.g. to 6 decimal places)
factorial | ! | **a** factorial 
hypotenuse | hyp | hypotenuse of a triangle given lengths **a** and **b**
deg\_to\_rad | deg\_to\_rad | convert degrees to radians
rad\_to\_deg | rad\_to\_deg | convert radians to degrees
cel\_to\_far | cel\_to\_far | convert celsius to farenheit
far\_to\_cel | far\_to\_cel | convert farenheit to celsius
pounds\_to\_kg | pounds\_to\_kg | convert pounds to kilograms
kg\_to\_pounds | kg\_to\_pounds | convert kilograms to pounds
mph\_to\_kph | mph\_to\_kph | convert miles-per-hour to kilometers-per-hour
kph\_to\_mph | kph\_to\_mph | convert kilometers-per-hour to miles-per-hour

#### Harder

Name	| Operator	| Description
-----|:--------:|------------|
fibonacci | fib | return Fibonacci sequence of length **a**
min\_of\_n | min\_of\_n | return minumum number in last **n** elements on stack
max\_of\_n | max\_of\_n | return maximum number in last **n** elements on stack
sum\_of\_n | sum\_of\_n | return sum of numbers in last **n** elements on stack
exponential | exp | exponential function **a**^**b**
logarithm | log | natural logarithm of **a**
logarithm10 | log10 | log base 10 of **a**

#### Expertest


Name	| Operator	| Description
-----|:--------:|------------|
log_fancy | log_fancy | log base **b** of **a**
hidden_message | secret | see notes below

secret = hide message in stack using numeric alphabet (e.g. a = 1, b = 2, etc.)..

* extra bonus points if you write a function to retrieve your message
* double bonus points if you find someone else's message 
* triple bonus points if you find their message and change it :)


## Choose an issue

* Select an issue in the project tracker<br> 
OR
* Identify something you would like to work on and add an issue to the Github repo
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

|[<<< Previous Lesson: Prepping for the Project](./lesson_07_project_prep.md)|
|:--|
