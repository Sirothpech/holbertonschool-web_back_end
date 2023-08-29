
---

# Advanced Python

This project contains exercises in advanced Python programming with a focus on type annotations. Type annotations are an essential practice to improve the readability, maintainability, and robustness of Python code.

## Tasks

### 0. Basic annotations - add

In this task, we need to create a function `add` that takes two arguments of type `float` and returns their sum as a `float`.

Example usage:
```python
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

### 1. Basic annotations - concat

In this task, we need to create a function `concat` that takes two arguments of type `str` and returns a string resulting from their concatenation.

Example usage:
```python
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
```

### 2. Basic annotations - floor

In this task, we need to create a function `floor` that takes an argument of type `float` and returns the integer part of the float.

Example usage:
```python
import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
```

### 3. Basic annotations - to string

In this task, we need to create a function `to_str` that takes an argument of type `float` and returns its string representation.

Example usage:
```python
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
```

### 4. Define variables

In this task, we need to define and annotate different variables with specific values, including an integer, a float, a boolean, and a string.

Example usage:
```python
a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))
```

### 5. Complex types - list of floats

In this task, we need to create a function `sum_list` that takes a list of floats as input and returns their sum as a float.

Example usage:
```python
sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
```

### 6. Complex types - mixed list

In this task, we need to create a function `sum_mixed_list` that takes a list of integers and floats as input and returns their sum as a float.

Example usage:
```python
sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
```

### 7. Complex types - string and int/float to tuple

In this task, we need to create a function `to_kv` that takes a string `k` and an integer or float `v` as input and returns a tuple where the first element is `k`, and the second element is the square of `v`, annotated as a float.

Example usage:
```python
to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
```

### 8. Complex types - functions

In this task, we need to create a function `make_multiplier` that takes a float `multiplier` as input and returns a function that multiplies a float by `multiplier`.

Example usage:
```python
make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
```

### 9. Let's duck type an iterable object

In this task, we need to annotate the parameters and return values of the `element_length` function with the appropriate types.

Example usage:
```python
element_length = __import__('9-element_length').element_length

print(element_length.__annotations__)
```

---

## Author
This project was realized Christophe Ngan (@Sirothpech)
