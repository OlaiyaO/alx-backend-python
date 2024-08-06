# alx-backend-python

## 0x02-python_async_comprehension

This repository contains tasks related to asynchronous programming and comprehensions in Python. The tasks are designed to practice writing asynchronous generators, comprehensions, and measuring execution time for asynchronous operations.

### Tasks

#### 0. Async Generator
**File:** `0-async_generator.py`

Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

**Usage:**
```python
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
