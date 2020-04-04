# Date Parsing Exercise

To run the test code, ensure you are in root of this git directory.
Then run the test suite with the following command.

`python -m unittest date_parser_tests`

You will see many failures.
The objective is to fill out the `parse(self)` method body with the correct code to get the test suite to pass.

# Fork this Repository

Making a `fork` of this repo will let you have your own copy of it under your github username.
This is helpful if you want to push changes up. 
The alternative is to do a regular clone,
but then if you try to push changes, the remote will be pointing to `notryanb/parsing_exercise`.
You will not have permissions to do this.
Forking will create a new repo under your github account with the same name but pointing to `your_github_username/parsing_exercise`.

- Fork this repo by clicking the "Fork" button in the upper right-hand portion of the screen.
- Go to "Your repositories"
- Click on "parsing_exercise"
- Click clone
- Ensure your current terminal directory IS NOT inside another git repo.
- You can see if this is true by running any git command such as `git status`.
- If it fails with a "fatal error", you are safe to clone a git repo into that directory.
- If `git status` succeeds, then you are currently inside another repository and should not clone this repository into it.
- Copy and paste the code Github gave you into your terminal once you've verified you are not currently in a git repository.
- If it succeeds, then `cd parsing_exercise` and you may move onto the next section.


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
