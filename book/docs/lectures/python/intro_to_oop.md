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

# Introduction to Object-Oriented Programming

In this lecture we will start looking at object-oriented programming (OOP). This is one of the major components of IN1910. In this lecture we will start to look at what OOP is, and how to program object-oriented in Python. In later lectures we will cover some more theory of object-oriented programming and also touch on it in C++.


## Other references

Object-oriented programming in Python is fairly well covered by *Langtangen*. Especially so in:
* **Chapter 7: Introduction to Classes** Gives a good introduction to defining classes and Python syntax.
* **Chapter 9: Object-Oriented Programming** Gives a better overview of theory and gives more technical examples.

If you want a different introduction to OOP in Python, these two lectures from MIT Open courseware might be a good place to start
* [Lecture 8: Object-Oriented Programming](https://youtu.be/-DP1i2ZU9gk)
* [Lecture 9: Python Classes and Inheritance](https://www.youtube.com/watch?v=FlGjISF3l78)


## What is Object-Oriented Programming?

Object-oriented programming (OOP for short), is a [*programming paradigm*](https://en.wikipedia.org/wiki/Programming_paradigm). Put simply, a paradigm is a way to think about, organize, and write code. Paradigms are used to classify and describe languages and programming styles. Many other paradigms exists, and you might have heard of some of them. Some examples are: procedural programming, functional programming, imperative programming, and symbolic programming. Most programming languages don't belong to a single, specific paradigm. Instead most languages, including Python and C++, are described as *multi-paradigm*, meaning it is possible to structure and write your code in different ways.

Object-oriented programming is a way of solving problems, or building software, by defining data as *objects*, and specifying how those objects behave and interact. It is one of the most popular programming paradigms, and is often used when developing software. When done correctly, OOP leads to code that is usually quite easy to understand, use and extend.

### The origins of OOP

Object-oriented programming was invented in Norway by Ole-Johan Dahl and Kristen Nygaard in 1967. They made a new programming language, and called the first object-oriented language *Simula*. While Simula was revolutionary and historically an important language, it didn't see widespread adoption. Inspired by Simula, the language *Smalltalk* came on the scene in 1972 and saw a wider use, pushing the use of OOP. Smalltalk still sees some use today, mainly as a means of teaching OOP and introductory programming. In 1983 *C++* arrived on the scene, and can be described as the first "industrial" object-oriented language. C++ was invented by Bjarne Stroustrup. He thought Simula had some nice features for large software development, but considered it to be to slow to be practical. He therefore started developing *"C with classes"*, which would eventually become C++.


```{figure} fig/oop_drake_meme.png
---
width: 300px
name: oop_drake_meme
alt: oop_drake_meme
---
You might have thought the ostehøvel was the greatest Norwegian invention, but Simula is where it's at
```


### What are objects?

So what are *objects*? You probably already have some intuition around what objects are. In Python, all variables are objects. So in a sense an object is similar to a variable. All objects have a few characteristics we can associate with them.

1. All objects have a given object *type*. We for example have integers, strings, lists and dictionaries. Objects of these types will behave differently, but they are all examples of objects
2. Objects behave in certain pre-defined ways. We can for example perform calculations with numbers, we can sort lists, or we can split a string. The type defines what actions we can perform, and what we can't do. It wouldn't make sense to divide a list by another list for example
3. Objects typically have information or data stored in them. For integers and floats this would be their numerical value, for a list it is all the elements and so on. In certain cases however, we define empty lists/dictionaries and so on.

One of the reasons OOP is so popular is that it is quite intuitive, because it mirrors real life. To make sense of the world around us when we think or talk we tend to divide everything into specific concepts or *objects*. Cars are objects and so are buildings. People are objects too, in the software sense. It isn't only physical things that are objects either. A given calendar date is an object, defined by its day, month and year. This course is IN1910, which could be described as an abstract object. We can think of a job as an object. In this sense an object is a data abstraction that attempts to capture some important property or feature.

**Everything in Python are objects**. When you are programming in Python, you are defining and using objects all the time. Does this mean you are programming object-oriented? Not necessarily. As we mentioned in the introduction the important thing is *thinking* and *solving problems* in an object-oriented manner. Meaning to do OOP properly one should ask what kind of objects are best for organizing a program and solving problems. Probably the most important task of programming object-oriented is therefore to define new data types, and defining how objects of that type should be represented and interact.

### Example: A contact list

Think about the contact list on your phone. For each contact, you can store information of different types: name, different phone numbers, emails, etc. For some contacts you have many pieces of information about, some you only have a single piece of information.

Let us say we want to implement such a contact list for a new phone system we are making. We might start thinking how to solve this problem. It makes sense to think of each individual contact as an individual *object*. Each piece of information belongs to a given contact, so it should be part of that object in the code.

To begin with, we only want to store information about each contact, and so dictionaries would be a natural choice for this. We can use key-value pairs to store the information we want, and ignore the pieces of information we don't want. Other parts of the software system can then go in and access information from the contact dictionary as needed

```{code-cell} python
contact = {"name": "Lisa", "email": "lisa@python.org", "mobile_number": "767828292"}

print(contact["email"])
```

However, our dictionary can only store information on the contact, we cannot add new functionality. A more general way to do this would instead be to define a custom Contact-*class*. Classes are way to define new data types. That way we can create variables that are of type *contact*, instead of dictionary. The upside is that we  can choose exactly how our contact datatype should behave.

```{code-cell} python
class Contact:
    def __init__(self, name, email=None, cellphone=None):
        self.name = name
        self.email = email
        self.cellphone = cellphone
```

With this class defined, we can now create new contact object as follows


```{code-cell} python
contact = Contact("Lisa", email="lisa@python.org", cellphone="767828292")
print(contact.email)
```

Our contact object is no longer a dictionary, but a `Contact`-object, a new data type we defined ourself. We can check this by writing out the type:

```{code-cell} python
print(type(contact))
```

So far we have only added the same information as the dictionary, but we could now go ahead and change how this object behaves. We could for example add a method that starts a new call to the person, so that we could do `contact.initiate_call()`, or a button to start an email to the person, and so on.


## Attributes, Fields, Methods

Classes are custom data types, and are extremely central to object-oriented programming. When you are developing object-oriented, most of your development will go into defining classes and how they interact.

When defining a new class, you need to specify what data an object of that type should contain, and what functionality it has. We call these the *attributes* of the class/object, and these can be split into two main groups:
* *fields* are pieces of data stored in the object
* *methods* are functions we can call

In Python we use the dot-syntax to access an objects attributes. For example

```{code-cell} python
x = complex(4, 3)

print(x.real)
print(x.imag)
print(x.conjugate())
```

Here we create a `complex`-type object, which represents a complex number. We can then access its real and imaginary components using the names `x.real` and `x.imag`. These are examples of attributes of object, in this case these are `float` attributes, which in turn are examples of data fields.

Last we use `x.conjugate()`, and this is also a class attribute - but in this case the attribute is callable and will behave as a function. Such attributes we call *methods* in Python. In this case the method returns the complex conjugate of the object.

```{code-cell} python
print(type(x.real))
print(type(x.conjugate))
```


## Class vs Instance

When we define a class, we are defining a new data type. To actually use it, we have to define a new object of that type, we call this an *instance* of the class. In our contact-list example, the `Contact` class is the general class we defined, then we can implement specific instances of the class, one for "Lisa", one for "Frank" and so on. The class is thus the abstract *concept* of a contact, and objects are the specific cases of that type. A different example: A Nissan leaf is a given type of car, and can be represented as a class. A specific car with the license plate "EM93277" (courtesy of random.org) is an *instance* of the Nissan leaf class. The specific car is an object of the *type* Nissan leaf. In this sense, the class is like the blue-print, it specifies how objects of that type should be built and how they should behave.

### Naming Conventions

According to the [PEP8](https://www.python.org/dev/peps/pep-0008/?#class-names) style-guide (more on this next week), class names should use the CapWords convention. This means every word in the class name should be capitalized, and the words should **not** be separated by underscores.

Some examples: `Person`, `Polynomial`, `Vector3D`, `BankAccount`, `FileReader`.

Specific instances of a class however, should always be lowercase. So when we define a variable of a given class, we would write for example:
```
u = Vector3D()
poly = Polynomial()
acc9302100 = BankAccount()
```
You should be strict about this rule, as it makes it much easier to differentiate the *classes* themselves (the general datatype) from instances of that class (the specific objects) in your code.


### Example: A deck of cards

Time for another example. Let us say we are implementing some card games. Now, we can easily represent a deck of cards using lists of strings in Python, no problem. However, for most card games, we need to use the exact same operations: get a new deck, shuffle the deck, draw cards, etc. It would be useful to implement the code to do this one time, and then just use that functionality each time we implement a new card game.

We do this by implementing a `Deck` class. After having implemented our class, we can then define an instance of this class (`deck = Deck()`). Our actual game code will then be much simpler, because we can now simply call `deck.shuffle()` or `deck.draw(5)` and so on. This adds a layer of abstraction to our code, and hides away the ugly implementation details "behind the scenes". This is called *encapsulation*, and is one of the motivations for using OOP. We can say we hide the implementation, but expose an easy-to-use and easy-to-understand *interface* that is used to manipulate the object

```{code-cell} python
import random


class Deck:
    def __init__(self):
        """Create a standard 52-card deck."""
        self.cards = []
        for s in ("D", "H", "C", "S"):
            for v in range(1, 14):
                self.cards.append((s, v))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        return [self.cards.pop() for _ in range(n)]

    def shuffle_into_deck(self, cards):
        self.cards.extend(cards)
        self.shuffle()
```

Here we implement a class that has four methods. The first method is the constructor (called `__init__`, we explain why later), this is run every time we create a new object of the class. In this case we initialize a deck of cards by adding all the cards in the deck using a double-loop. We also add a `shuffle` method that shuffles the deck, a `draw` method that draws $n$ cards from the deck, and a `shuffle_into_deck` for when we want to shuffle cards back into the deck. These are just simple examples of functionality that makes sense for a deck of cards, and we could add plenty more.

Once we have taken the time to build the `Deck`-class, we can easily create decks of cards, and use them, without having to think too much about the underlying details of the implementation. Implementing a class therefore represents adding a new layer of abstraction to our code. For example, we can now create a random 5-card poker hand as follows:

```{code-cell} python
deck = Deck()
deck.shuffle()

hand = deck.draw(5)
print(hand)
```

### The use of `self`

In our class examples so far, we have simply used the `self`-syntax without explaining it. It is a normal point of confusion for those learning Python, and even those who learn how to define the classes and method using `self` might not really understand *why* it works like it does.

When we call a method on a given instance of a class, like for example
```
deck.shuffle()
```
This is interpreted behind the scenes by Python as
```
Deck.shuffle(deck)
```
And so the method `Deck.shuffle`, even though it is written inside the class, actually just acts like a stand-alone function, the object is simply passed in and manipulated. And so when we define the function we call the first input-argument `self`, because this is the *object itself* (in this case `self = deck`). Note that you can, technically, call this argument something other than `self`, it is just a function argument, like any other. However, it is considered good code style to always use `self` and it will be confusing for others if you use something else. (Most languages use either "self" or "this".)

So for most class methods you define, you both define the method with `self` as the first argument. And you use `self` inside the method to manipulate the data within the object. Let us look back at the `Deck.shuffle` method:
```{code-cell} python
class Deck:
    ...

    def shuffle(self):
        random.shuffle(self.cards)
```
When we intend to use this on a specific deck we simply write `deck.shuffle()`, i.e., without arguments. We still define the function with a `self` argument, and the method shuffles the internal list attribute of the deck, i.e., `self.cards`.


## Interfaces

In our deck of cards example, we have specific methods the user can use to interact with the deck of cards, and we can call this the *interface* (På norsk: grensesnitt) of the class. To put it simply, the interface is what is "visible" or usable from outside the class. If you build a large and complex class, all anyone really needs to interact with it is a good understanding of its interface. In this sense, the interface itself is an abstraction tool. Take a car for example, the interface used for driving that gar is the steering wheel, the pedals and the gear stick. However, under the hood there is an engine and lots of complicated machinery.

The act of hiding dirty implementation or technical details under the hood is called *encapsulation*. Encapsulation is useful for keeping code nice and tidy and user friendly. Also, it means that the details under the hood can change without issue, as long as the external interface remains the same. A mechanic can replace the engine in your car, but you will still be able to drive it as before, because the interface is the same.

In some languages, like Java and C++, you can explicitly define interfaces that define what a class must contain.  These are often described as "contracts", as they state what a given class that follows that interface must contain.



## Special Methods

In Python, defining classes often involve implementing *special* methods, also known as *magic* methods (or dunder methods). These are methods we do not expect to call explicitly. Rather, we expect Python to call them for us as needed, depending on the situation. They are extremely useful to learn how to use, and they lead to elegant, understandable and usable code. Becoming adept at special methods is crucial if you want to make good Pythonic code.

Special methods have specific names, so Python knows what to call. They all use two leading and two trailing underscores. You have already seen an example of this, the constructor: `__init__`.


### The constructor (`__init__`)

You have already seen the most important example of special methods, the constructor, or initialization special method (`__init__`). This function is called every time you define a new instance of a class.

```{code-cell} python
from math import pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.area = 4 * pi * radius**2
        self.volume = 4 * pi * radius**3 / 3


football = Sphere(11)
print(f"A football of radius {football.radius:.0f} cm")
print(f"Has a surface area of {football.area:.0f} cm^2")
print(f"And a volume of {football.volume:.0f} cm^3")
```

Once we define a new instance of the class, the `__init__`-method is called behind the scenes. As usual, the first argument is called "self", because this will be the object itself. In addition we send in any additional arguments we need to define an object of the given class. In this example we define a sphere-object, and so we send in the radius as an argument. In our constructor we then choose to store the radius as a data attribute by writing
```{code-cell} python
self.radius = radius
```
This code line might look a bit weird, but here we are defining the instance property `football.radius`, and setting the value to be the same as the function argument (`11`). In addition to storing the radius, we have chosen to also compute the area and volume of the sphere, and store these as attributes as well.


### Printing out instances of custom classes

If you attempt to call `print` on a custom object, you'll find that it doesn't produce output that is super helpful.

```{code-cell} python
print(football)
```

Reading the output we get out the type, in this case `__main__.Sphere` (main because we defined it in our main script, and didn't import it), it tells us it is an object, and then it specifies where in memory the object is stored. The object type can in many cases be useful information, but you could already get this information by using the `type()` function.

To print more useful information, we can implement the string special method (`__str__`). This special method is called automatically for us when we try to turn our custom object into a string by writing `str(u)`. In addition, when we call `print(u)`, Python actually first converts the object to a string behind the scenes before printing it (unlike for example `sys.stdout.write`, where you have to do it manually). So if we implement `Football.__str__` we would get the following happening behind the scenes

* `print(football)` -> `print(str(football))` -> `print(football.__str__())`

This means: if we implement a `__str__` that returns a nicely formatted string, we can print our object exactly the way we want it.

```{code-cell} python
from math import pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.area = 4 * pi * radius**2
        self.volume = 4 * pi * radius**3 / 3

    def __str__(self):
        return f"Sphere({self.radius})"


football = Sphere(11)
print(football)
```

A different special method that is similar to the string method is the representation special method (`__repr__`). The main difference is that `__str__` is meant to be human readable, so that it works with `print()`. This means that `__str__` can be informal, and ambiguous, as long as it is somewhat informative.

On the other hand we have `__repr__`, which is meant to be unambiguous and more formal. It should be a unique representation of the object so that it could be used to recreate that object later. When calling `repr(u)` we should get a string that we for example can write to a file, then later load in and execute that statement to get the object back. So `eval(repr(u))` should give `u`.

The repr special method is also called when printing out elements inside a list for example, so if we write out our football inside a list, the output will be as before, despite having implemented a str-method. To fix this we would need to add a repr instead, or in addition to, the str-method.

```{code-cell} python
list_of_spheres = [Sphere(0), Sphere(5), Sphere(10)]
print(list_of_spheres)
```

Now let us implement the `__repr__` method

```{code-cell} python
from math import pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.area = 4 * pi * radius**2
        self.volume = 4 * pi * radius**3 / 3

    def __str__(self):
        return f"Sphere({self.radius})"

    def __repr__(self):
        return str(self)
```

Here we use a quick little trick. Because we don't really want `__repr__` and `__str__` to produce any different output, we simply let `__repr__` use the string special method by writing `self(str)`. Using methods internally when defining classes is very common, and can save us a lot of hassle

```{code-cell} python
list_of_spheres = [Sphere(0), Sphere(5), Sphere(10)]
print(list_of_spheres)
```

### Making callable objects

Another important special method is the *call* method (`__call__`). If a class has an implemented call method, we can call a given object as though it were a function. This is because Python automatically will use the call-method behind the scenes. This is extremely useful when we want to create objects that represent mathematical functions.

Say for example we want to make a class for quadratic functions, which can be written as

$$
f(x) = ax^2 + bx + c.
$$

Here, there a three free parameters, the coefficients $a$, $b$, and $c$. We therefore let the constructor take these in. We then implement the mathematical function itself as the call special method:

```{code-cell} python
class Quadratic:
    def __init__(self, a, b, c):
        self.coefficients = a, b, c

    def __call__(self, x):
        a, b, c = self.coefficients
        return a * x**2 + b * x + c


f = Quadratic(1, 2, 1)
print(f(4))
```

Here, when we assign `f = Quadratic(1, 2, 1)`, we are creating a new object of the class that represents the function $f(x) = x^2 + 2x + 1$. It isn't actually a Python function, but it is *callable*. We can therefore use it as if it were a normal function and call it by writing `f(4)`. When we write this, Python interprets it behind-the-scenes as

* `f(4)` -> `f.__call__(4)` -> `Quadratic.__call__(f, 4)`

We can now easily create quadratic functions and use them as normal functions:

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt

f = Quadratic(1, 2, 1)
g = Quadratic(-1, 4, 4)
h = Quadratic(0, -2, 3)

x = np.linspace(-4, 4, 101)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.plot(x, h(x))
plt.show()
```

There are several advantages to implementing these quadratic functions as actual Quadratic-objects, rather than as normal Python functions. For one, they now have a custom type, which we can check using `isinstance(f, Quadratic)`. Thus, other parts of our code can *know* that the function is a quadratic function. We can also extend the class adding plenty of useful functionality. We could for example add functionality for adding or subtracting functions, producing new Quadratic-objects. This cannot be done with normal functions. Or we could add a method for returning the derivative. If you do this week's exercises, you will get the chance to implement all of these for a general degree polynomial.


## Polymorphism

The fact that we can use callable objects as if they were functions is very useful in Python, and it is an example of [*polymorphism*](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)). Polymorphism is another of the pillars of OOP, but the concept is a bit tricky to define or understand. The term itself comes from greek and means "many forms". It is a means of generalizing code, in that we can write different code that behaves the same under given circumstances, and thus we can use those objects as long as they have a given property we need. In this case, we can create objects that acts and feels like functions, and we can use them for any purpose were we need a Python function.

This is an example of Python's [*duck typing*](https://en.wikipedia.org/wiki/Duck_typing). This term comes from the saying:

* *If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.*

What we mean by this is that what *type* a given object is isn't that important, what is important is how it behaves. In Python we therefore shouldn't check whether a given input is a Python function, instead we should check whether it is *callable*. This can be done with the built-in function:
```Python
callable(f)
```
This function returns `True` if the object `f` is callable, and `False` if it is not. It doesn't care whether `f` is a Python function, a custom class or a given class method. It only cares if `f` quacks like a duck.


### Example: The derivative class

In mathematics, Newton's method is a numerical method for finding the roots of a mathematical function (a root is the point where the function is equal to zero). Normally to use Newtons method you need the function itself ($f(x)$), it's derivative ,$\frac{\rm d}{{\rm d}x} f(x)$. which also is a function, and an initial guess $x_0$.

Let us now assume we are given a function `newton(f, x0, dfdx)` that implements Newton's method. The SciPy library for example has the function `scipy.optimize.newton(func, x0, dfdx)`. We want to use this function to find the roots of a function $f(x)$. However, we don't know the derivative $f'(x)$ that must be sent in, and we cannot find it analytically. What do we do?

One solution would be to implement the derivative function numerically. We can approximate the derivative function in any point using the central finite difference for example,

$$
\frac{\rm d}{{\rm d}x} f(x) \approx \frac{f(x+\Delta x) - f(x - \Delta x)}{2\Delta x}.
$$

Typically we compute this for a given array of values or something like that. However, for `newton` to work, we can't send in an array of values, we must send in a callable function. To create such a callable function we can create a `Derivative` class that automatically creates a callable object for $f'(x)$.

```{code-cell} python
class Derivative:
    def __init__(self, f, dx=1e-6):
        if not callable(f):
            raise ValueError("Input must be callable.")

        self.f = f
        self.dx = dx

    def __call__(self, x):
        dx = self.dx
        return (self.f(x + dx) - self.f(x - dx)) / (2 * dx)
```

Here we create the class from a given function `f`, which we double check is *callable*. We store the function as an attribute so we can use it later. We also store the step size $\Delta x$, which defaults to $10^{-6}$ if we do not supply it.

We can now implement the derivative of any callable function as its own callable object as follows

```{code-cell} python
import numpy as np

f = np.sin
dfdx = Derivative(f)
```

Here `f` represents the function $f(x) = \sin(x)$, while `dfdx` will be its derivative. Let us check if it works. As we know the derivative of $\sin(x)$ is $\cos(x)$ we can test our implementation as follows

```{code-cell} python
x = 0.8281

print(dfdx(x))
print(np.cos(x))
```

With the `Derivative` class implemented, we can now easily use the `newton` method on any function, simply use  the `Derivative`-class to automatically define the derivative function, and then call Newton, as follows

```{code-cell} python
from scipy.optimize import newton


def f(x):
    return x**2 + 4 * x + 4


dfdx = Derivative(f)
x0 = 0

print(newton(f, x0, dfdx))
```

Here we simply used Newton's method as an example, and do note that `scipy.optimize.newton` actually doesn't need us to supply the derivative function, because if we do not supply it, it does pretty much the same as we have done behind the scenes automatically.

```{code-cell} python
newton(f, x0)
```

Implementing the `Derivative` class ourselves does hopefully make it more apparent how SciPy can use Newton's method without having the derivative function - it is also a good example of how OOP can be used in scientific computing.


## More Special Methods

So far, we have shown the following special methods
* `__init__`
* `__str__`
* `__repr__`
* `__call__`

These are just a few of many, many possible special methods you can implement. We will look at more example in the next lecture. For a more comprehensive list and more examples, you can check out [this site](http://www.diveintopython3.net/special-method-names.html).


## Properties

The final topic we will cover today are what we call *properties*, which is a very handy topic to know about when implementing and using your own custom classes, and we therefore go back to our example with the sphere-class

```{code-cell} python
class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.area = 4 * pi * radius**2
        self.volume = 4 * pi * radius**3 / 3

    def __str__(self):
        return f"Sphere({self.radius})"
```

Here we set the radius of the sphere once we create the object, and the area and volume are automatically computed. This works quite well, but it has a few issues as well. For one thing, there is nothing that prevents us from changing one of these fields directly. If we do this, the other fields do **not** change automatically


```{code-cell} python
ball = Sphere(5)
print(f"{ball} has a volume of {ball.volume:.0f}")

ball.radius += 5
print(f"{ball} has a volume of {ball.volume:.0f}")
```

So here we create a `Sphere`-object, which we call `ball`. We can update the radius of the ball by changing the `ball.radius` attribute directly. However, when we do this, the volume does not change. This is because the volume is only computed in the constructor (the `__init__` method), which is called only when the object is first created.

How big of a problem this is of course dependent on how the code is to be used. But for now, let us say we want to make the code more intuitive, user-friendly and foolproof. Our goal is therefore to make it possible to change the radius attribute directly, and have the area and volume auto-update.

A simple solution is to make the `area` and `volume` attributes methods instead of data fields

```{code-cell} python
class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * pi * self.radius**2

    def volume(self):
        return 4 * pi * self.radius**3 / 3

    def __str__(self):
        return f"Sphere({self.radius})"
```

We can now update the `radius` property, and when we call the `area()` or `volume()` methods, they will recompute using the new radius

```{code-cell} python
ball = Sphere(5)
print(f"{ball} has a volume of {ball.volume():.0f}")

ball.radius += 5
print(f"{ball} has a volume of {ball.volume():.0f}")
```

By making the `area` and `volume` attributes methods, they will always be recomputed as they are needed, which is nice. It will also make it easier for the user to understand that they are derived quantities from `Sphere.radius` and not independent attributes.

However, this implementation can also be a bit confusing. For one, radius, area and volume are simply all different properties of a Sphere, and all represented as numbers - so why should one be a number variable, and the other methods that must be called?

```{code-cell} python
print(type(ball.radius))
print(type(ball.area))
print(type(ball.volume))
```

Let us therefore look at a different way to set up this class using *properties* in Python. To do this, we use the built-in *decorator* `@property`. A decorator is something you place right before a function/method definition, and it will change the functionality of that function/method in some way. You will (or have) see an example of a decorator in Project 0.

When we add the `@property` decorator to a method in a class, that method will behave from the outside as if it is a data field, and not a method.

```{code-cell} python
class Sphere:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 4 * pi * self.radius**2

    @property
    def volume(self):
        return 4 * pi * self.radius**3 / 3

    def __str__(self):
        return f"Sphere({self.radius})"


football = Sphere(11)
print(football.area)
print(type(football.area))
```

Here, both `Sphere.area` and `Sphere.volume` are defined in the exact same manner as before, but we have added the code `@property` right before the method definitions. By adding this decorator we can now treat `football.area` as if it was a data field, i.e., a number variable. This means we can print it right out, without calling it like a method, and if you print out the type, it confirms that it is indeed a float.

Using the property decorator allows us to implement a method that compiles or computes the data behind the scenes in some way, but allows the user to treat that property as a data field on the outside. We can now change the radius, and the `area` and `volume` properties will also change. The user does not have to think about this themselves.

```{code-cell} python
ball = Sphere(5)
print(f"{ball} has a volume of {ball.volume:.0f}")

ball.radius += 5
print(f"{ball} has a volume of {ball.volume:.0f}")
```

Let us now look at what happens if we try to change the `area` and `volume` properties directly, instead of changing the radius. If you try this yourself, you will get an error as follows
```Python
football.area = 1200
```
You would get the following error:
```
AttributeError: can't set attribute
```
Thus, by defining an attribute using `@property`, we have effectively made the attribute "read-only".


### Setters and Getters

In Python, we can access class attributes directly using the dot notation, e.g., `ball.radius`, and we can also change these directly if we so desire. This is not considered bad practice if the Class is defined to do this. In many other languages however, one either cannot access attributes directly, or it is considered bad practice to access them directly. In such languages, it is often common to define "setter" and "getter" methods. Here we would define a `Sphere.get_radius` method, which would return the value of the radius, and we would define a `Sphere.set_radius` to redefine it.

In Python, such setters and getters are usually not implement explicitly, but we can use the same logic. In our previous example, we defined
```{code-cell} python
@property
def area(self):
    return 4 * pi * self.radius**2
```
And this method is effectively a *getter* for the area. It isn't called `get_area`, but that is what the function does.

Similarly, we can define a *setter* method for the area property using the decorator `@area.setter`. Let us show with an example


```{code-cell} python
from math import pi, sqrt


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 4 * pi * self.radius**2

    @area.setter
    def area(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.radius = sqrt(area / (4 * pi))

    def __str__(self):
        return f"Sphere({self.radius})"
```

Here we first define the `Sphere.area` property using `@property` which allows us to access `Sphere.area` as if it were a number variable. After this we also define a setter, which allows us to redefine (or "set") the area. To do this we have to use the area formula in reverse to find the equivalent radius and redefine `self.radius`.

With the `@area.setter` method defined, we can now both access `Sphere.area` *and* redefine it if we want. For example:

```{code-cell} python
ball = Sphere(10)
print(f"{ball} has an area of {ball.area:.0f}")

ball.radius = 5
print(f"{ball} has an area of {ball.area:.0f}")

ball.area = 1000
print(f"{ball} has an area of {ball.area:.0f}")
```

So we now have a `Sphere`-class that allows us to either set the radius, and have the area automatically update, *or* we can set the surface area, and the radius automatically updates. Hopefully it is apparent why this could be useful. Another nice detail about this is we can build in some controls on the input of the setter function. Note that we in the `@area.setter` method have a check to see if the area is negative. If `Sphere.area` was a simple float attribute, we would have no way of restricting what value it was set to in this manner.

```{code-cell} python
ball.area = -1
```
now gives
```
ValueError: Area cannot be negative
```


Note that we haven't added the volume method in the last example primarily to save some space in the lecture notes, you can now try to define the `@volume.setter` method yourself.


### Avoiding repeated computations

Our sphere class now works quite well and is user friendly. We can now the radius, surface area and volume as floats, and can set any of them directly and the others change automatically. However, this implementation might not be that efficient, as every time the user accesses `.area` or `.volume`, the actual values are computed from the radius behind the scenes.

For such a simple computation as this, recomputing the area or volume isn't a big deal. But say these computations were more complicated and took something like a minute to complete. It would be annoying an inefficient to repeat such computations again and again.

The way we would get around this would be to store the computed values as *internal* data in the class that the user should not interact with from outside the class. Such attributes are typically called *private attributes*. In Python there is no way to implement actual private variables, but you can designate that variables should be considered private by giving them name with a leading underscore.

Let us show by an example (again we skip the `volume` property, which you can add yourself)

```{code-cell} python
class Sphere:
    def __init__(self, radius):
        self._radius = radius
        self._area = 4 * pi * radius**2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = r
        self._area = 4 * pi * self.radius**2

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self._radius = sqrt(area / (4 * pi))
        self._area = area
```

We now store the area of the sphere as a private attribute called `sphere._area`. The underscore means this variable should never be accessed from outside the class. In addition we add the property `sphere.area` which can be used from outside.

The code will now behave exactly the same as before from outside the class, but by using `sphere._area` we avoid unnecessarily recomputing the area many times.

Note that we have also made the radius into a private variable `sphere._radius` and external property `sphere.radius`. We had to do this do ensure that the `sphere._area` attribute is recomputed if the radius is set (using `@radius.setter`).

The code is now *a lot* more complex than what we started out with. And in many simple use cases you wouldn't go through the hassle of using private internal attributes like this and make properties and setters for these. For the sphere for example, recomputing the area a few times consumes close to no resources and can easily be done to get a simpler code. We simply use this as an example for how to handle cases that would be more complex.


### Private and Public variables

In our final example, the user has the properties `football.radius` and `football.area` they can interact with, while the class itself stores the internal data in the fields `_radius` and `_area`. We call the first two *public* properties or variables. Here, public means that they are accessible from outside the class. The latter two variables are *private*, meaning they should only be accessed from inside the class and are not meant to be used from outside.

Note that we give the private variables leading underscores in their name, which indicates they are private. In Python, there is no way to enforce private variables however, and the leading underscore is just a convention. Thus the user can go inn and change these directly: `football._radius = 9`, however, this is breaking the *convention* that one should change a private variable, and if this breaks the object, it is the users fault. Other languages, such as Java and C++ however, *do* enforce private and public variables. If you attempt to access a private variable from outside, an error is thrown.
