# Redis basic

## Tasks

### 0. Writing strings to Redis

Create a `Cache` class with the following methods:

- `__init__(self)`: Initializes the Cache object with a Redis client instance and flushes the database.
- `store(self, data: Union[str, bytes, int, float]) -> str`: Stores the input data in Redis with a randomly generated key and returns the key.

Example usage:
```python
cache = Cache()
data = b"hello"
key = cache.store(data)
print(key)
```

### 1. Reading from Redis and recovering original type

Implement a `get` method in the `Cache` class that retrieves data from Redis given a key and optionally converts it back to the desired format using a provided function. Additionally, implement `get_str` and `get_int` methods for automatic conversion.

Example usage:
```python
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

### 2. Incrementing values

Implement a `count_calls` decorator that counts the number of times a method of the `Cache` class is called. Decorate the `store` method with this decorator.

Example usage:
```python
cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

### 3. Storing lists

Create a `call_history` decorator to store the history of inputs and outputs for a particular function. Decorate the `store` method with this decorator.

Example usage:
```python
cache = Cache()

s1 = cache.store("first")
s2 = cache.store("second")
s3 = cache.store("third")

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

### 4. Retrieving lists

Implement a `replay` function to display the history of calls of a particular function.

Example usage:
```python
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
```

This should output:
```
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```