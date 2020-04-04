# Date Parsing Exercise

To run the test code, ensure you are in root of this git directory.
Then run the test suite with the following command.

`python -m unittest date_parser_tests`

You will see many failures.
The objective is to fill out the `parse(self)` method body with the correct code to get the test suite to pass.

# How to get started solving this exercise

When running the test suite, you will see a lot of error output in your terminal indicating the tests are failling.

example:

```
======================================================================
FAIL: test_can_parse_yyyy_mm_dd_as_underscore (date_parser_tests.TestDateParser)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "date_parser_tests.py", line 23, in test_can_parse_yyyy_mm_dd_as_underscore
    self.assertEqual(expected, result)
AssertionError: datetime.datetime(2020, 4, 11, 0, 0) != None
```

The most important part is the Assertion error where it tells you what the expected value and result values are.
Your objective is to write code to make the result values be the same as the expected.

Instead of trying to solve all the tests at once,
pick the first test failure case and solve them one at a time.

When you have made all the code in the test suite pass,
you can now use your `DateParser` class in your project!
