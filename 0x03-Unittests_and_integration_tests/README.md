# 0x03. Unittests and Integration Tests

## Overview

This project focuses on the creation and execution of unittests and integration tests for Python code. Unit testing ensures that individual functions return expected results for various inputs, while integration testing verifies the interaction between multiple components of the code.

## Learning Objectives

By the end of this project, you should be able to:
- Understand the difference between unit tests and integration tests.
- Apply common testing patterns such as mocking, parameterization, and fixtures.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- Modules, classes, and functions must have proper documentation.
- Functions and coroutines must be type-annotated.

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/48431559/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Testing

### Unit Tests

Unit tests verify that a specific function returns expected results for different sets of inputs. These tests should focus on the logic defined within the function and mock external calls, such as network or database interactions.

**Command to execute unit tests:**
```sh
$ python -m unittest path/to/test_file.py
```

### Integration Tests

Integration tests check the interactions between various parts of the code. They mock low-level functions that make external calls and aim to test the code path end-to-end.

## Project Files

- `utils.py`
- `client.py`
- `fixtures.py`

## Common Testing Patterns

- **Mocking:** Replace parts of your system under test and make assertions about how they have been used.
- **Parameterization:** Use different sets of parameters for testing.
- **Fixtures:** Setup necessary preconditions and cleanup afterward.

## Important Notes

- A `README.md` file is mandatory.
- Ensure all your functions, classes, and modules have proper documentation.
- All your functions and coroutines must be type-annotated.

Let's create and test robust Python code using unittests and integration tests!
