# Option 2 Code Review

## Correctness

<br>Line 26:<br>
This line calls the `reverseString` method which does has not been declared. 
This is meant to be a recursive method so correct the method call below to match the `reverse_string` method signature or change the signature.
```java
return reverseString(myStr.substring(1)) + myStr.charAt(0);}
```

<br>Line 30:<br>
variable `maxNumber` is already defined in the method signature and can be re-assigned by dropping the `int` type declaration.
However, a value is passed into the `maxNumber` parameter when the method is called so there is no reason to re-assign `maxNumber`.

<br>Line 28:<br>
Parameter `maxNumber` would need to be converted to an int to be used in the loop that follows.
Rather set the type of `maxNumber` to int.

<br>Line 21 & 25:<br>
The print statements appear to be for debugging and can be commented out in the final implementation.

<br>Line 11:<br>
The print output hardcodes the first 10 fibonacci numbers. This is incorrect.
The solution must programmatically solve the problem.

<br>Line 28 - 47: <br>
The `function` method is supposed to output the Fibonacci numbers recursively. This method uses the iterative approach.

<br>Line 37 - 45:<br>
The loop outputs 18 values but the first value (0) is the 0th term. For the first 18 terms and additional iteration of the loop would be required.
Setting the iterator `i` to start at 0 like below, or adjusting the conditions for exiting the loop.
See [list of fibonacci numbers](https://planetmath.org/listoffibonaccinumbers).

```java
for (int i = 0; i <= maxNumber; ++i){
```


## Efficiency

<br>Line 18 - 26: <br>
In Java, String is immutable. The recursive `reverse_string` method uses `String.substring()` creates copies of the string.
A more efficient approach would be to operate over a character array but for the scope of this program this method is acceptable.
<br>

<br>Line 18 - 26: <br>
This should be a recursive solution according to the problem specification.
FYI: many programming languages optimize recursive methods into iterative forms so an iterative solution may be correct in terms of efficiency.

## Style

Line 1: <br>
The class name `recursion` does not follow the title case naming conventions.
Lowercase classnames and filenames won't affect compilation, but following naming conventions ensures your code is more readable.
See [Java Naming Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).
<br>

Line 18: <br>
Methods should be verbs, in mixed case with the first letter lowercase, with the first letter of each internal word capitalized.
The `reverse_string` should be refactored to `reverseString` in this case.
<br>

Line 28: <br>
Methods names should be descriptive. The `function` method doesn't allow another to infer what the method is doing.
<br>
Example:<br>
It's unclear what result is being printed out below.
```java
System.out.println(function(7));
```

<br>Line 6:<br>
Variable names should be descriptive. The variable `myStr` doesn't give any indication of what the string would be used for.


## Documentation

Line 17:<br>
The end-of-line comment on line 17 is best used within methods or attached to class properties. Block comments would be more appropriate for commenting a method signature.
See [Code Conventions for Java Comments](https://www.oracle.com/java/technologies/javase/codeconventions-comments.html)