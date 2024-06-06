# 0x00. Python - Variable Annotations

## Project Overview

This project focuses on advanced Python concepts, specifically on type annotations. The goal is to understand and implement type annotations in Python 3 to specify function signatures and variable types, utilize duck typing, and validate code with mypy.

## Learning Objectives

By the end of this project, you will be able to:
- Explain type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand and apply duck typing.
- Validate your code with mypy.

## Resources

To achieve these objectives, refer to the following resources:
- [Python 3 Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Requirements

### General

- **Editors:** You may use `vi`, `vim`, or `emacs`.
- **Environment:** Your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- **File Formatting:**
  - All files should end with a new line.
  - The first line of all files should be `#!/usr/bin/env python3`.
  - Use the `pycodestyle` style (version 2.5).
  - All files must be executable.
  - File lengths will be tested using `wc`.
- **Documentation:**
  - All modules should have documentation.
  - All classes should have documentation.
  - All functions (inside and outside classes) should have documentation.
  - Documentation should be a complete sentence explaining the purpose of the module, class, or method.

## Project Deadlines

- **Project Start:** June 6, 2024, 6:00 AM
- **Project End:** June 7, 2024, 6:00 AM
- **Checker Release:** June 6, 2024, 12:00 PM
- **Auto Review:** An auto review will be launched at the deadline.

## Getting Started

1. **Clone the repository** and navigate to the project directory.
2. **Create your Python files** ensuring they meet the formatting and documentation requirements.
3. **Implement type annotations** in your functions and variables.
4. **Validate your code** using mypy.
5. **Ensure compliance** with `pycodestyle`.

## Example Usage

Here is a simple example to get you started with type annotations:

```python
#!/usr/bin/env python3
"""
This module demonstrates type annotations in Python 3.
"""

from typing import List

def sum_of_list(numbers: List[int]) -> int:
    """
    Calculate the sum of a list of integers.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        int: The sum of the list of integers.
    """
    return sum(numbers)

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4]
    print(f"The sum of {sample_list} is {sum_of_list(sample_list)}")
```
