---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Type annotations


## Dynamic vs static typing

In python everything has is an object, however you probably have at this point a clear model of some of the types in python, e.g integers, floats, strings, lists, dictionaries and so on. In python you can check the type of a variable by use the `type` function
```{code-cell} python3
x = 42
y = "42"
print(f"{type(x) = }")
print(f"{type(y) = }")
```
You can also check that if a instance is of a certain type using `isinstance`
```{code-cell} python3
print(f"{isinstance(x, int) = }")
print(f"{isinstance(x, str) = }")
```
You can also check for several types by passing in a tuple of types as the second argument ot `isinstance`. The return value will be true if any of the types matches
```{code-cell} python3
print(f"{isinstance(x, (str, int)) = }")
```
This information about the types are known when the program runs, i.e at runtime. In many other programming languages, such as C++, we need to know this information before the program run, i.e at compile time. Such languages typically use a compiler to translate the source code (i.e the code you write) into machine instructions which is stored in some binary file that you can run. Languages where you need to specify the type before the program runs are called statically typed languages. Static here refers to that once you have declared a variable to have a certain type then it is in general not allowed to change the type. In python, on the other hand there is nothing preventing you from doing this. For example the following code runs without problem
```{code-cell} python3
x = "Hello"
x = 42
x += 1
```
Python is what is called a dynamically typed language, meaning that the variables can change type during a programs lifetime

## Introducing type annotations
In [PEP484](https://peps.python.org/pep-0484/) type hits were introduced to the python language (starting at python version 3.5) allowing developers to add type information to python code. Here is one example

```
pi: float = 3.142

def circumference(radius: float) -> float:
    return 2 * pi * radius
```


## Why do we want types?


## Static type checking with `mypy`
