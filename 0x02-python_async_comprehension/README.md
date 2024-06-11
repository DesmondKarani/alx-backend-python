# 0x02-python_async_comprehension

This project involves learning and implementing asynchronous comprehensions in Python.

## Learning Objectives

By the end of this project, you should be able to:
- Write an asynchronous generator
- Use async comprehensions
- Type-annotate generators

## Files

### 0-async_generator.py

Contains the `async_generator` coroutine that loops 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10.

### 1-async_comprehension.py

Contains the `async_comprehension` coroutine that collects 10 random numbers using an async comprehending over `async_generator`, then returns the 10 random numbers.

### 2-measure_runtime.py

Contains the `measure_runtime` coroutine that measures the total runtime of executing `async_comprehension` four times in parallel using `asyncio.gather`.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- PEP 530 – Asynchronous Comprehensions
- What's New in Python: Asynchronous Comprehensions / Generators
- Type-hints for generators
