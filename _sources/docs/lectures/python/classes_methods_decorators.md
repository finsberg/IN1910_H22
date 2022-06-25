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

# Creating classes in Python

In the previous lecture we started to cover object-oriented programming (OOP) in Python. A big component of OOP is to define your own custom data types or *classes*. Today we will we continue on this topic and focus on how to design and implement classes in Python. We start with a quick recap of the last lecture, then cover some new special methods and finish up by briefly discussing *inheritance*, a useful topic to know about when designing classes.


## Recap of Object-Oriented Programming so far

### What are Objects?
Last week we introduced object-oriented programming, a paradigm where we design programs and code from a basis of *objects*. In Python, all variables are objects and all objects are characterized by
* Their *object type*, which defines how the object behaves and interacts with other objects
* Their *data*. Different objects contain different types of data, some contain a single value (like a `float` object) while others contain a large number of values (like a `list`, `dictionary` or `set`).

### What are Classes?
We can define new object *types* by defining *classes* in Python using the `class` keyword. A class is the definition of a new object type. After we have created a class, we can create new objects of that class, which are called *instances*.
* A class is the definition of a new object type
* An *instance* is a object of a given class

To use an example, in this lecture we will define a `Vector3D` class, which represents a vector in 3D space. This is a general class. After implementing this class, we can then define specific vectors with specific coordinates/values using `u = Vector3D(2, 2, 0)`, and here `u` would be an *instance* of the `Vector3D` class.

### Attributes

A class, and by extension its instances, are defined by its attributes. We can group all attributes into two main categories:
* Data fields contain specific information (e.g., `booleans`, `floats`, `strings`, `floats`, etc)
* Methods are callable functions we can use to interact with the object

### Special Methods

In Python, there are a series of *special methods* we can implement to automate many behaviors. We covered some of these last time, and will cover a lot more today. Last time we covered the following special methods
* The constructor, `__init__`
* The string and representation methods, `__str__` and `__repr__`
* The `__call__` special method, which makes objects callable (very useful for representing functions!)

In addition we covered the `@property` decorator, which can be used to define custom properties in a class. This is easiest to explain with examples, so let us come back to this later in this lecture.



## A 3D vector class

The main component of this lecture will revolve around implementing a specific class. By adding more and more functionality to this class, we illustrate different special methods and possibilities in Python and how these work.

As a specific case example, we will implement a class for three dimensional vectors `Vector3D`. We want objects of this class to behave mathematically as vectors, and we will add functionality to do vector arithmetic.


### The constructor (`__init__`)

The most fundamental method of any class is its *constructor*, which is automatically called when we create a new instance of a class. In Python, the constructor is called `__init__` (short for *initialize*). To define a 3D vector, we need to specify its three cartesian coordinates, which we call $x$, $y$, $z$.

```{code-cell} python
import numpy as np


class Vector3D:
    """A class representing 3D cartesian vectors"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

This constructor doesn't do much other than save the three coordinates as internal attributes. This is necessary so that the object remembers its coordinates and can use them later. The string on line 4 is an example of a *docstring*, which we will describe in more detail next week. If you have not seen such strings before, simply think of it as a comment for now.


### Pretty printing

Next we want to be able to print out vectors, so that we can check our results. We implement this using the string special method (`__str__`). If we were just implementing this in an editor, we would just keep editing our file. In the notebook, we don't want to repeat the whole class for each cell. Instead we just extend our existing class as follows:

```{code-cell} python
class Vector3D(Vector3D):
    def __str__(self):
        return f"({self.x:g}, {self.y:g}, {self.z:g})"


u = Vector3D(0, 4, -2)
print(u)
```

Here, extending the class by writing `Vector3D(Vector3D)` works because of *inheritance*, as we will explain later. For now, you can think of it as adding code to the existing class. Note however, that any vectors defined before we extend the class will *not* be updated. So in the notebook we must remember to define new vector instances when we want to test our code.


### The repr method

Our string special method works nicely and can be used to print out vectors in our code. Recall however that when printing sequences such as lists, they will still look quite rough

```{code-cell} python
print([u, u])
```

The solution to this was to add the `__repr__` method, which should provide the string we can be used to recreate the object if need be. We can add it as follows

```{code-cell} python
class Vector3D(Vector3D):
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


u = Vector3D(0, 4, -2)
v = Vector3D(3, 0, 1)

vectors = [u, v]
print(vectors)
```

Here the vectors get written out on the form which can be used to recreate the objects with `eval`, which is exactly what we want. However, there is a small trick we can use to make the `__repr__` a bit more general, which is to use the exploit the fact that all classes in Python "know" their own name. Look at the following code

```{code-cell} python
class Vector3D(Vector3D):
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"
```

So instead of writing the name `Vector3D` directly into the code (known as "hard coding" it), we use the variable `self.__class__.__name__` to refer to the name. This variable exists for any object automatically.

What is the benefit of doing this? Well, if we later want to change the `Vector3D` name to something else, the method will update automatically. Secondly, and perhaps more important is that we can also use `Vector3D` to create new classes through inheritance, and then we want the new classes to automatically have `repr` referring to their own class, not their parent class.


## Vector Arithmetic

The main goal of our `Vector3D` class is to automate vector arithmetic, so let us extend our class to handle this. We start by focusing on addition and subtraction

### Addition

If we want to be able to add two vectors together, we need to add a method that defines how such an operation is to be handled. We could for example define a `add` method, and write `u.add(v)` to compute $u + v$. However, this isn't very elegant. Instead, we want to be able to write `u + v` in our code. A statement like this uses the *binary operator* `+` (binary meaning it acts on two variables/objects). For any such operators in Python, there is one or more special methods associated with it. So when you write `a + b` Python will automatically interpret this behind the scenes as `a.__add__(b)`. Let us implement this method.

The result of adding two vectors together is a brand new vectors. Our `__add__` method therefore needs to create and return a new `Vector3D`-object. If this is confusing, imagine the following code snippet
```{code-cell} python
u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)
w = u + v
```
In this case, adding `u` and `v` to define `w` shouldn't change the values of `u` and `v`, but should instead create a *new vector object*, which we give the name `w`. For `w` to refer to a new object, it must be created somewhere, and we must do this inside `__add__`. The code therefore can look as follows

```{code-cell} python
class Vector3D(Vector3D):
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3D(x, y, z)


u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)
w = u + v

print(f"{u} + {v} = {w}")
```

This works just the way it should, and this code is perfectly fine. However, we have again hard-coded in the name of our class in the method implementation itself. It would be *even better* to do as follows

```{code-cell} python
class Vector3D(Vector3D):
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return self.__class__(x, y, z)


u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)
w = u + v

print(f"{u} + {v} = {w}")
```

This makes our code more general and better suited for extending in the future.


### `self` and `other`

We just defined our addition method with the statement `def __add__(self, other)`, which can be a bit confusing.  To better understand this, it can be helpful to first understand why there must be two arguments. This is because we are talking about *binary* addition, meaning two things are added together. When we write `a + b`, these two objects are being added, so `self` will refer to `a` and `other` will refer to `b`. This can become more clear if we realize what calls are being made behind the scenes:

1. We write: `a + b`
2. Which Python interprets as: `a.__add__(b)`
3. Which in turn actually means: `Vector3D.__add__(a, b)`

So in the method we have written, which has the signature `__add__(self, other)`, we see that `a` is the self, and `b` is the other.

The use of `self` and `other` can be a tricky concept to wrap your head around, but it is fundamental to mastering classes, so it is very worth the time to take time to properly digest this material.

Please note however that the names `self` and `other` are *not* reserved keywords in Python, and it is possible to pick other names for these variables. However, `self` and `other` are very commonly used, and can be considered strict conventions. We therefore recommend you stick to these unless you have a good reason to deviate.


### Vector-scalar addition

We have added a method to add two vectors together, so we can write `u + v`. What happens if we try to add a vector and an integer `u + 1`?
```Python
print(u + 1)
```
We can an error: `AttributeError: 'int' object has no attribute 'x'`.

This error happens because our `other`-object in this case is no longer a `Vector3D`-object, but an `int`. Here we get an `AttributeError` because we try to use `other.x`, but the integer has no `.x` attribute to access. In this case, we should actually be checking what type `other` and treat it differently depending on its type. We know `self` is a `Vector3D`, so we don't need to check this.

Now, what behavior do we want if actually try to add an integer? We could either say we add the number to each component separately, so:
```
if isinstance(other, (int, float)):
    self.x += other
    self.y += other
    self.z += other
```
This is how a numpy array works for example. In our case, however, we want the `Vector3D` class to represent a mathematical vector, and for these, adding a vector and a scaler together doesn't make sense because they have different dimensions. Therefore, we should throw an exception instead. Let us generalize this to throw an error if we try to add anything other than another vector object as follows:

```{code-cell} python
class Vector3D(Vector3D):
    def __add__(self, other):
        if isinstance(other, Vector3D):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector3D(x, y, z)
            # or return self.__class__(x, y, z)

        else:
            raise TypeError(f"cannot add vector and {type(other)}")


u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)

print(f"{u} + {v} = {u + v}")

try:
    print(f"{u} + {1} = {u + 1}")
except TypeError as e:
    print(f"{u} + {1} gives 'TypeError: {e}'")
```

You could now argue that one for example should be able to add a `Vector3D` and a list of three numbers, e.g., `u + [1, 3, 1]`. You can try to extend the `__add__` method to account for such a possibility if you want. For now, we move on to other operations.


### Subtraction

Extending our class to also handle subtraction of vectors is very similar to addition, we simply use the subtraction special method instead (`__sub__`).

```{code-cell} python
class Vector3D(Vector3D):
    def __sub__(self, other):
        if isinstance(other, Vector3D):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
            return Vector3D(x, y, z)
            # or return self.__class__(x, y, z)

        else:
            raise TypeError(f"cannot subtract vector and {type(other)}")


u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)

print(f"{u} - {v} = {u - v}")

try:
    print(f"{u} - {1/2} = {u + 1/2}")
except TypeError as e:
    print(f"{u} - {1/2} gives 'TypeError: {e}'")
```

### The unary negative operator (aka "minus")

We have now defined and implemented what `u + v` and `u - v` means for our vectors. From mathematics, we know that `u - (-v)` is equivalent to `u + v`, but will Python understand this? If we were doing test-driven development (such as in Project 0), this would be a good example of a new test to add.

If you try yourself, you will see that the operation `u - (-v)` does *not* work, but instead throws the following error message
```
TypeError: bad operand type for unary -: 'Vector3D'
```
This can be a confusing message, so let us break it down for you.

In the expression `u - (-v)` we have *two* subtraction operators, both represented by `-`. The first one is the normal binary subtraction which acts on the two variables `u` and `(-v)`. This corresponds to `__sub__` which we have already added. The second subtraction however, in `(-v)` does not act on two variables and so is instead a *unary subtraction* (unary meaning "acting on one operand"). This operation is coupled to the special method `__neg__` (for negative). When Python interprets our code it must first resolve the parentheses and compute the negative of `v`, and we have not defined how this is done for our class, which is why we get the error message "bad operand type for unary -".

Let us now define the `__neg__` special method. As this is a unary operator, we only take in the `self` argument, and skip the `other` (as there is no "other" vector in this case)

```{code-cell} python
class Vector3D(Vector3D):
    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)
        # or return self.__class__(-self.x, -self.y, -self.z)


u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)

print(f"{u} - (-{v}) = {u - (-v)}")
```

The code now works. First the `__neg__` method is used to compute `(-v)`, then `u - (-v)` is computed using `__sub__`.

Another small detail you can note here is that if we had implemented our `__neg__` method *first*, then we could have relied on this when implementing `__sub__`. Check this out:

```{code-cell} python
class Vector3D(Vector3D):
    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return self + (-other)
        else:
            raise TypeError(f"cannot subtract vector and {type(other)}")


u = Vector3D(2, 0, -2)
v = Vector3D(2, 4, 2)

print(f"{u} - {v} = {u - v}")
```

This `__sub__` method behaves just as before, but the implementation now relies on `__neg__` (and `__add__`) by saying that `u - v` is equivalent to `u + (-v)`. Tricks like these can be nice when implementing arithmetic methods.


### Multiplying vectors

We now want to add functionality for multiplying vectors. For 3D vectors, several type of multiplication exists. We want to be able to do both the dot product, and the cross product. Let us implement these as normal methods (not special methods) first. Just to remind you, the two multiplications are defined as follows

$$u \cdot v = (x_1, y_1, z_1) \cdot (x_2, y_2, z_2) = x_1x_2 + y_1y_2 + z_1z_2.$$

$$u \times v = (x_1, y_1, z_1) \times (x_2, y_2, z_2) = (y_1z_2 - z_1y_2, z_1x_2 - x_1z_2, x_1y_2 - y_1x_2).$$

An important point here is that the dot-product should return a number (i.e., `int` or `float`), while the cross product should return a new vector object. The two methods can look as follows


```{code-cell} python
class Vector3D(Vector3D):
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)
```

We can now use `u.dot(v)` and `u.cross(v)` in our code, which is quite a nice syntax as it spells our exactly what kind of vector multiplication we are computing. We can of course *also* add them as special methods if we want, in fact it is quite easy because we can simply call the `dot` and `cross` methods (this is called "aliasing")

Let us decide that we want `u*v` to be interpreted as the dot product. This multiplication operator is associated with the special method `__mul__`. So we can write

```{code-cell} python
class Vector3D(Vector3D):
    def __mul__(self, other):
        """Interpret u*v as the dot product"""
        return self.dot(other)
```

We have now "used up" the asterisk multiplication operator in Python, what syntax can we then choose for our cross product? Well, one option is to use the code syntax `u @ v` to mean the cross product. You might not have seen (or used) the `@` operator in Python code before, but it is a binary operator associated with the special method `__matmul__` (short for "matrix multiplication). It actually isn't used by any of the built in Python objects, but it is available for mathematics where we want to have access to more operators. (Note that for numpy arrays, `@` is implemented, but will correspond to the dot-product for 1D-arrays, while `*` means component-wise multiplication).

```{code-cell} python
class Vector3D(Vector3D):
    def __matmul__(self, other):
        """Interpret u @ v as the cross product"""
        return self.cross(other)


u = Vector3D(1, -1, 0)
v = Vector3D(1, 4, 2)

print(f"{u} * {v} = {u * v}")
print(f"{u} @ {v} = {u @ v}")
```

A useful property of the dot product is that two vectors are perpendicular if, and only if, the dot product is equal to zero ($u \cdot v = 0 \Leftrightarrow u \perp v$). Let us therefore add a `perpendicular` method, which checks if two vectors are perpendicular

```{code-cell} python
class Vector3D(Vector3D):
    def perpendicular(self, other):
        return np.isclose(self * other, 0)


u = Vector3D(1, -1, 0)
v = Vector3D(1, 4, 2)
print(u.perpendicular(v))
```

Note that we use `np.isclose` because the coordinates of the vectors can easily be `floats`, and comparing floating points to zero is a common pitfall due to floating point errors.


From linear algebra you can prove that if you define a vector as the cross product of two vectors, i.e.,

$$
w = u \times v
$$

Then the new vector $w$ will be perpendicular to both $u$ and $v$. This can be used to test our code.

```{code-cell} python
w = u @ v

# Printing answer
print(f"Is u ⊥ v? {u.perpendicular(v)}")
print(f"Is w ⊥ u? {w.perpendicular(u)}")
print(f"Is w ⊥ v? {w.perpendicular(v)}")

# Asserting answer
assert w.perpendicular(u)
assert w.perpendicular(v)
```

### Scalar multiplication

We have now defined vector-vector multiplication, but it is also possible to multiply vectors by scalers (i.e., numbers). We can for example compute $3u$, which corresponds to multiplying each component of the vector by the number 3 separately.

We now want to be able to write `3*u` or `u*3` in our code to capture this mathematical operation. Let us first see what happens if we try this with our current code

```{code-cell} python
print(3 * u)
```
```
TypeError: unsupported operand type(s) for *: 'int' and 'Vector3D'
```
This error tells us multiplication isn't defined between integer and vector objects. We is a bit interesting is what happens if we flip the operators, we get a different error message!
```{code-cell} python
print(u * 3)
```
```
AttributeError: 'int' object has no attribute 'x'
```
The second error is similar to the one we got for addition earlier. When we write `u*3`, this is interpreted as `u.__mul__(3)`, which in turn is `Vector3D.__mul__(u, 3)`, and so `self` is `u` is `other`. Because we defined `__mul__` to be the dot-product we try to use `other.x` which is then `3.x` which doesn't exist. Let us fix this first, and then get back to the first error message after.

To fix this, we should rewrite our `__mul__`-method to do different things depending on if the `other` variable is a vector or a scalar. In programming, this is known as [*function overloading*](https://en.wikipedia.org/wiki/Function_overloading), which is when we define a function or method to do different things depending on context. In this case we overload the `*` operator to mean either vector-vector multiplication or vector-scalar multiplication, depending on context.

```{code-cell} python
class Vector3D(Vector3D):
    def __mul__(self, other):
        if isinstance(other, Vector3D):
            # Vector-vector multiplication
            return self.dot(other)

        elif isinstance(other, (int, float)):
            # Vector-scalar multiplication
            return Vector3D(self.x * other, self.y * other, self.z * other)

        else:
            # Unknown
            raise TypeError(f"cannot multiply vector and {type(other)}")


u = Vector3D(1, -1, 0)
v = Vector3D(1, 4, 2)

print(f"u = {u}")
print(f"3*u = {u*3}")
print(f"u*u = {u*u}")
```

We now see that we can compute `u*3`, and we also check that we can compute the dot-product as before. You should always recheck that you haven't broken old functionality when you go back and change a function or method---if you have implemented proper tests, this will automatically get checked when you run `pytest`. Here we have to do it manually.

From our implementation of `__mul__`, we now check the second operand and choose the right behavior from this. But what about for `3*u`? If you now try, this still throws a `TypeError: unsupported operand type(s) for *: for 'int' and 'Vector3D'`. So `u*3` does work, but `3*u` does not. Let us try to understand why one works and the other fails. When we write these statements, they are interpreted as follows
* `3*u` -> `3.__mul__(u)` -> `int.__mul__(3, u)`
* `u*3` -> `u.__mul__(3)` -> `Vector3D.__mul__(u, 3)`

So, the major point is that it is the operand to the left of the multiplication sign (`*`) which decides which class's `__mul__` method is called. So in `3*u` it isn't our method that is used at all, but `int`'s. And the built-in `int` hasn't been written to interact with our custom class.

Mathematically speaking, it is much more common to write $3u$ than $u\cdot 3$, and so saying we should just write `u*3` in our code is not satisfactory. So what can we do? It turns out this problem is so common that Python has a built-in work around in the form of the special method called `__rmul__` (for right multiply). This method is called automatically if the first operands `__mul__` throws an error. So if we implement `__rmul__` we get the following cascade
* `3*u` -> `3.__mul__(u)` -> Throws an error -> `u.__rmul__(3)` -> `Vector3D.__rmul__(u, 3)`

Effectively, `__rmul__` can be thought of as a "backup" method. One important thing to notice in this cascade is that the operands effectively get flipped when this backup is used. To implement `__rmul__` we can therefore simply use the `__mul__` we already implemented as follows

```{code-cell} python
class Vector3D(Vector3D):
    def __rmul__(self, other):
        return self * other


u = Vector3D(4, -6, 2)
print(2 * u)
```

This brings up an important point about operators in programmering. While some operators are generally considered commutative in mathematics, meaning the order can be changed without changing the result ($a+b = b+a$), we see that this is not the case in Python. We could for example add different function in the `__add__`-method and in the `__radd__` method, and then `a+b` and `b+a` would behave differently. In fact, you might already know several examples of this, for example adding strings or lists together:

```{code-cell} python
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(b + a)
```

### Adding 'properties' to our class (Length)

Often we are interested in the length of a vector, or we want a unit vector with the same orientation as a given vector, let us add this as well. Let us now use Python-properties to do this, which we introduced in the previous lecture. The main point was that there were decorators we could use (`@property`).

A quick note: In Python there is a length special method (`__len__`), that is called by Python when we write `len(u)`. This is typically meant for sequences such as lists where the length equals the number of elements. Because of this, the `__len__` method *has* to return an integer. For our case, a general vector often has a decimal length, and so the `__len__` method wouldn't work. Which is why we use a property instead.

Let us first add the length property. To compute the length of a vector we first take the dot-product of the vector with itself and then take the square root, i.e., $|u| = \sqrt{u \cdot u}$.

```{code-cell} python
class Vector3D(Vector3D):
    @property
    def length(self):
        return np.sqrt(self * self)


u = Vector3D(2, -2, 1)
print(f"{u} has a length of {u.length}")
```

Here the length-property is very easy to add, because we have already defined the dot product for a vector in `__mul__`, so we can simply write `sqrt(self*self)` and the dot product is computed. Recall that the `@property` makes it so the method looks like a `float` variable from the outside, so we write `u.length` instead of `u.length()`.

Let us now make a `@length.setter` method as well, so that we can *scale* the length of the vector. When we say we scale a vector we typically mean shifting all three vectors so that the length changes while the orientation stays the same. We can therefore scale all three components by the same ratio

```{code-cell} python
class Vector3D(Vector3D):
    @property
    def length(self):
        return np.sqrt(self * self)

    @length.setter
    def length(self, new_length):
        ratio = new_length / self.length
        self.x *= ratio
        self.y *= ratio
        self.z *= ratio


u = Vector3D(2, -2, 1)
print(f"{u} has a length of {u.length}")

# Rescale u
u.length *= 2

print(f"{u} has a length of {u.length}")
```

So we see we can double the length of the vector, which automatically scales each component the appropriate amount.


**Unit vector**

The last functionality we want to add is a method which automatically finds the unit vector for a given vector. So if `u` is a vector, `u.unit()` will be a new vector that points in the same direction as `u`, but has a length of 1.

When we make the `.unit` method it should first create a new `Vector3D` object, as the original should be unchanged. If we make this new vector by copying the original, we know it points in the right direction, so we can then just scale the length. We can implement this as follows

```{code-cell} python
class Vector3D(Vector3D):
    def unit(self):
        new = Vector3D(self.x, self.y, self.z)
        new.length = 1
        return new


u = Vector3D(2, -2, 1)
v = u.unit()

print(f"u = {u} has a length of {u.length}")
print(f"w = {v} has a length of {v.length}")
```

Here we create a copy by writing `Vector3D(self.x, self.y, self.z)`, which is straight-forward, and works. But there is a much simpler way to create a copy, which is to lean on our already defined `__repr__` method. Recall that `repr(u)` should give a string such that `eval(repr(u))` should recreate the original. However, note that the "recreated" vector will be a new object, but with identical values, i.e., a copy of the original

```{code-cell} python
u = Vector3D(5, -3, 5)
v = eval(repr(u))

print(f"u = {u}")
print(f"v = {v}")
print(f"Are u and v the same object? {u is v}")
```

Here `u is v` is an operation which checks whether two objects are the *exact* same object in memory. And here we get `False`, as expected. In this case, making a copy is easy, because it is easy to make a proper `__repr__` function. For more complex classes and objects, this gets a bit trickier, then the `copy` package might help. Here we just showed how to make the copy, so let us rewrite the `.unit` method:

```{code-cell} python
class Vector3D(Vector3D):
    def unit(self):
        new = eval(repr(self))
        new.length = 1
        return new
```

```{code-cell} python
u = Vector3D(2, -2, 1)
v = u.unit()

print(f"u = {u} has a length of {u.length}")
print(f"v = {v} has a length of {v.length}")
```

#### Other Special methods

Here we have shown different special methods, but there are plenty left to cover. Virtually any possible behavior of an object can be decided through good use of special methods. For a more detailed walkthrough, see [this guide](https://rszalski.github.io/magicmethods/).

Here are some that might be of special interest:
* `__eq__`, for defining when two objects should be considered equal (What does `a == b` mean?).
* You can also define `__lt__` (less than, $<$), `le` (less or equal, $\le$) and so on. If you implement all the six comparison operators it is typically called *rich comparisons* and it will make your objects automatically sortable with `sort()`.
* `__bool__` defines what `if x:` means for our object
* `__abs__` defines what `abs(x)` means

* We can also implement `lt`, `le`, `gt`, `ge`, `ne` for $\lt, \le, \gt, \ge, \ne$. Implementing all of these is called *rich comparisons*, and automatically makes our objects sortable with `sort()`
* `__bool__` defines what `if x:` means for our object
* `__abs__`, defines what `abs(x)` means. For `Vector3D` we could for example define it so that `abs(u)` returns `u.length`.
* `__getitem__` and `__setitem__` can be used to make our object indexable, i.e., define what `x[0]`, `x[1]` and so on means
* (**Advanced**) `__hash__` makes it possible to compute a [hash value](https://www.programiz.com/python-programming/methods/built-in/hash) from your object with `hash(u)`. This is needed if you want to use your object as a key in a dictionary.

(dataclasses)=
## Dataclasses

Dataclasses is a fairly new concept that was added in python 3.7. When writing the `Vector` class we note that there is a lot of boilerplate code that we have to write. Here we also add [type annotations](type-annotations) because these are needed in dataclasses.

```{code-cell} python
class VectorNormalClass:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(x={self.x}, y={self.y}, z={self.z})"
        )

v1 = VectorNormalClass(1, 2, 3)
print(v1)
```
In the constructor we first take `x`, `y` and `z` as arguments and then set them as attributes on the instance. In the `__repr__` we get the name of the class and basically copy the constructor declaration. As a result the argument `x` is written three times in the constructor and two times in the representation. This seems a bit redundant, and indeed we can solve write the same code using dataclasses as follows

```{code-cell} python
from dataclasses import dataclass

@dataclass
class VectorDataClass:
    x: float
    y: float
    z: float

v2 = VectorDataClass(1, 2, 3)
print(v2)
```

Notice that we have now added a decorator on the class it self. We will see later how to construct you own decorators.


## Short introduction to inheritance

For the last portion of this lecture, we will give a very brief introduction to *inheritance*, which we will come back to in more detail next week. For now we will just one simple example.

Inheritance is a term we use to describe how we can use one class to build another. In Python we let a class inherit from another when we define it. When we do this, the *parent* class gives its functionality, i.e., all its attributes to the newly created class, typically called the *daughter* class. Instead of saying parent/child, one can also say superclass and subclass.

When we create a class through inheritance we start with a class that has all the attributes of its parent, but we can extend this by implementing new methods to add on, or we can overwrite existing methods to change how they work. In general we make a subclass to specialize a class. So the parent/superclass will be a more *general* case, while the subclass will be more specialized/specific.

Let us look at a somewhat silly example, taken from the mobile game Pokémon Go. If you've haven't played that game, the example is hopefully still easy to follow. Either way, the details about the specific calculations we implement are not the important point here, try to focus more about the big picture, and focus on how we implement the class and use inheritance in this case.


### Example: Pokémon Go

In the game Pokémon Go, the goal is for the players to catch different *Pokémons* (pocket monsters). Many different types of Pokémon exist, some common, some rare. Each Pokémon you catch have different stats and, at least in principle, players want to catch Pokémons with good stats, i.e., high numbers.

As you walk around, the game generates random Pokémon that can be found, and it also randomizes its stats. And we will now implement a code that replicates this.

The stats of a specific Pokémon is dependent on its species/type, because each species has specific base stats. In addition each individual Pokémon caught has a randomized bonus to its stat, called the *individual value*. These individual values are random numbers between 0 and 15 for all pokemon, regardless of species.

Because some properties vary by species, and some do not, we want to use inheritance. We now want to create a `Pokemon` superclass that has all functionality that is general to all `Pokemon`, and then we can implement specific species as subclasses afterwards.


We now make the `Pokemon` class. Each time a new pokemon is generated, we must draw its individual values randomly. There are three separate stats in the game: `ATK`, `DEF` and `STA`. We implement these as properties.

```{code-cell} python
import numpy as np


class Pokemon:
    def __init__(self):
        self.IV_ATK = np.random.randint(16)
        self.IV_STA = np.random.randint(16)
        self.IV_DEF = np.random.randint(16)
```

We have no implemented a general constructor that will work for all Pokémon. When a new pokemon is created, three random stats are drawn from the range $[0, 15]$. Let us also add properties to find the total ATK, DEF and STA stats of a given Pokémon. We also add a `__str__` method for pretty printing.

```{code-cell} python
class Pokemon(Pokemon):
    @property
    def ATK(self):
        return self.BASE_ATK + self.IV_ATK

    @property
    def DEF(self):
        return self.BASE_DEF + self.IV_DEF

    @property
    def STA(self):
        return self.BASE_STA + self.IV_STA

    def __str__(self):
        return f"{self.__class__.__name__}({self.ATK}, {self.DEF}, {self.STA})"
```

Two things to notice here are that
1. We use the variables `self.BASE_ATK` and so on. These are not defined anywhere! If you thus try to create a general "Pokemon" and check its stats, you will get an error message. This is intentional, as the general `Pokemon` class is not created to be used directly, only to be inherited from. Such classes are quite common in programming and are typically called *abstract classes*
2. Note that we in the `str` special method use the `self.__class__.__name__` variable. This will make it so that the `str` method of any class who inherits from `Pokemon` automatically updates it `str` method. Which is nice.


Now, let us implement a few specific Pokemon types. Lets start with the two most iconic ones:

```{code-cell} python
class Pikachu(Pokemon):
    BASE_ATK = 112
    BASE_DEF = 101
    BASE_STA = 70


class Charizard(Pokemon):
    BASE_ATK = 223
    BASE_DEF = 176
    BASE_STA = 156
```

Here we write `Pikachu(Pokemon)`, this syntax means the class is inheriting from the class within the parentheses and becomes a subclass. Thus `Pikachu` is a subclass of `Pokemon`, i.e., a specialized sub-case. The same is true for `Charizard`. In either case we do not define any new methods for the class, but instead define the base stats as *class attributes* because they are the same for all pikachus (more on class attributes next week).

Now we have very easily made two distinct species of Pokemon, without having to re-implement their general behavior. Inheritance has simplified our overall code considerably.

```{code-cell} python
for i in range(5):
    pokemon = Pikachu()
    print(pokemon)

print()

for i in range(5):
    pokemon = Charizard()
    print(pokemon)
```

One last detail we want to mention is that a subclass is considered a specialized cased of its superclass. In this case, `Pikachu` and `Charizard` are specific examples of Pokémons. We can check that they are indeed considered to be Pokémons as follows

```{code-cell} python
pikachu = Pikachu()
charizard = Charizard()

print(f"Is Pikachu a Pokemon? {isinstance(pikachu, Pokemon)}")
print(f"Is Charizard a Pokemon? {isinstance(pikachu, Pokemon)}")
print(f"Is Pikachu a Charizard? {isinstance(pikachu, Charizard)}")
```

That was it for this example. The point was to illustrate how the goal of inheritance is to put all the general behavior in the superclass, and then only implement the *specifics* in the subclasses to specialize them.

If you are interested in Pokemon Go, you can now extend the Pokemon class to for example calculate the CP, tier and so on.
