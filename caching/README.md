### Caching

#### Parent class BaseCaching

All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item to the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

#### Task 0: Basic dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- This caching system doesn’t have a limit.

```python
class BasicCache(BaseCaching):
    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
```

#### Task 1: FIFO caching

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the first item put in the cache (FIFO algorithm) and print `DISCARD: with the key discarded` and a new line.

```python
class FIFOCache(BaseCaching):
    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_in = list(self.cache_data.keys())[0]
                del self.cache_data[first_in]
                print("DISCARD: {}".format(first_in))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
```

#### Task 2: LIFO Caching

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the last item put in the cache (LIFO algorithm) and print `DISCARD: with the key discarded` and a new line.

```python
class LIFOCache(BaseCaching):
    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_in = list(self.cache_data.keys())[-1]
                del self.cache_data[last_in]
                print("DISCARD: {}".format(last_in))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
```

#### Task 3: LRU Caching

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least recently used item (LRU algorithm) and print `DISCARD: with the key discarded` and a new line.

```python
class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Add an item to the cache
       

 """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order_used.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order_used.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None
```

#### Task 4: MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the most recently used item (MRU algorithm) and print `DISCARD: with the key discarded` and a new line.

```python
class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order_used.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order_used.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None
```

**Repository Structure:**
- GitHub repository: [holbertonschool-web_back_end](https://github.com/username/holbertonschool-web_back_end)
- Directory: caching
- Files: 
  - `0-basic_cache.py`
  - `1-fifo_cache.py`
  - `2-lifo_cache.py`
  - `3-lru_cache.py`
  - `4-mru_cache.py`