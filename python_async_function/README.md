# Python - Async

This project explores asynchronous programming in Python using coroutines and tasks.

## Tasks

### 0. The basics of async

In this task, you will create an asynchronous coroutine called `wait_random` that takes an integer argument `max_delay` (with a default value of 10) and waits for a random delay between 0 and `max_delay` (inclusive and as a float value) seconds before eventually returning the delay.

You should make use of the `random` module.

Example usage:
```python
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

### 1. Let's execute multiple coroutines at the same time with async

In this task, you will import the `wait_random` coroutine from the previous Python file and create an async routine called `wait_n`. `wait_n` takes two integer arguments, `n` and `max_delay`, and spawns `wait_random` `n` times with the specified `max_delay`.

`wait_n` should return a list of all the delays (float values). The list of delays should be in ascending order without using `sort()` due to concurrency.

Example usage:
```python
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

### 2. Measure the runtime

In this task, you will import the `wait_n` coroutine into `2-measure_runtime.py`. Create a `measure_time` function that takes integers `n` and `max_delay` as arguments. This function measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n` as a float.

You should use the `time` module to measure an approximate elapsed time.

Example usage:
```python
n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

### 3. Tasks

In this task, you will import `wait_random` from `0-basic_async_syntax`. Write a function, `task_wait_random`, that takes an integer `max_delay` and returns an asyncio.Task.

Example usage:
```python
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4. Tasks

In this task, you will take the code from `wait_n` and create a new function, `task_wait_n`. The code is nearly identical to `wait_n`, except it calls `task_wait_random`.

Example usage:
```python
import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

---

This README provides an overview of the tasks in the "Python - Async" project and includes example usages for each task. You can run the provided test scripts to check the functionality of each task.

## Authors
This project was realized Christophe Ngan (@Sirothpech)
