# Credit Cards and the Luhn Algorithm

### Objective
Practice using Python string methods to determine whether a string represents a potentially valid credit card number.

### About Luhn
The Luhn algorithm is a simple checksum used to verify credit card numbers. For an account number to pass the Luhn test it must:

* From the rightmost digit moving left, double the value of every second digit. If the result of doubling is > 9 then sum the digits. e.g., 7x2 = 14, 1+4=5
* Take the sum of all digits
* Divide the sum by 10. To pass the Luhn test the remainder from dividing by 10 must be zero



Wikipedia has more information on the [Luhn Algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)

### The Lab

1. Implement the `pass_luhn` method. It should return `True` if the string of numbers passes the algorithm described above or `False` if not. 
2. Implement the `is_visa` method. An account number is a valid Visa if it is either 13 or 16 numbers long, starts with a 4, and passes the Luhn test.
3. Implement the `is_mastercard` method. An account number is a valid MasterCard if it is 16 characters long; starts with a number in the range 51-55 inclusive; and passes the Luhn test.
4. Implement the `is_amex` method. An account is a valid American Express if it is 15 characters long, starts with either a 34 or 37, and passes the Luhn test.
5. Implement the `is_discover` method. An account number is a valid Discover if it is 16 characters long, starts with 6011, and passes the Luhn test.
6. Implement the `is_valid_cc` method. It should return `True` if it is valid for any of the 4 other `is_X` methods or `False` if not.



### Testing

There are unit tests for each method in the `test_luhn.py` file that you can run to check your work.

### Turning In

You'll need to commit and push your code back to GitHub to turn it in. I'd suggest doing that at least after you successfully complete each method and when you've completed the project. 

The unit tests will run again after you've pushed to GitHub and should tell you whether the submission was correct or not. 