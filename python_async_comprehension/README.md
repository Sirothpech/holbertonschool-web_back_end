# Python - Async Comprehension

## Table of Contents

0. [Async Generator](#async-generator)
1. [Async Comprehensions](#async-comprehensions)
2. [Run time for four parallel comprehensions](#run-time-for-four-parallel-comprehensions)

## Async Generator

**Mandatory**

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously waiting for 1 second, then yielding a random number between 0 and 10. Use the `random` module.

```python
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

Expected output:

```
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

## Async Comprehensions

**Mandatory**

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

```python
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

Expected output:

```
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

## Run time for four parallel comprehensions

**Mandatory**

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

```python
import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(
    asyncio.run(main())
)
```

Expected (approximate) output:

```
10.021936893463135
```

In this output, the total runtime is approximately 10 seconds because the four executions of `async_comprehension` are performed in parallel. Each execution waits for 1 second, and since they are executed concurrently, the total time is approximately 4 seconds (the maximum of the four 1-second waits). However, due to concurrency management and other factors, the total time may vary slightly, which is why it's approximately 10 seconds in this example.

## Authors
This project was realized Christophe Ngan (@Sirothpech)
