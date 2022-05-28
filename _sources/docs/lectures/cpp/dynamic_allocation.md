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
# More on pointers and arrays and dynamic allocation

In this lecture we will continue looking a bit more at pointers and how they relate to arrays. We will also use what we have learned about object oriented programming to design a few classes for making list objects.


## Som repetition

Recall that we can create *pointer* variables, that store the memory address of some data. We can for example create an *integer pointer* as follows:
```C++
int a = 12; // integer variable
int *b; // integer pointer
```
Here, `b` will be a pointer, because we use the asterisk (\*) when declaring it's type. To make `b` point at `a`, meaning the variable is storing the memory address of `a`, we use the address-of operator:
```C++
b = &a; // make b point at a
```
Now `b` points at `a` and we can use it to access and change `a`, however, recall that we cannot do so directly, if we for example attempt to print it out:
```C++
cout << b << endl;
```
We do not get the value of `a` (which is 12), but instead the *value* of `b`, which is the memory address, which will look something like:
```
0x7ffc072c388c
```
To actually get the variable a pointer is pointing to, we use the dereference operator:
```C++
cout << *b << endl;
```

| expression | can be read as   |
| ---------- | ---------------- |
| int i      | integer variable |
| int *p     | pointer variable |
| *x         | pointed to by x  |
| &x         | address of x     |


Also recall that we can set a pointer to point at "nothing":
```C++
b = nullptr;
```

## Pointers to objects

Let's say we create a struct
```C++
struct GridPoint {
    int x;
    int y;
    int z;
};
```
We can then create an instance of this struct, and access its members using dot-notation:
```C++
GridPoint start{10, 10, 0};
cout << start.x << endl;
cout << start.y << endl;
cout << start.z << endl;
```
We can also make a pointer to the object:
```C++
GridPoint *sp = &start;
```
Now, if we want to access one of the member attributes of the underlying object, we first need to dereference the pointer, and then use dot-notation:
```C++
cout << (*sp).x << endl;
```
We need the parenthesis to get the right order of operations. This syntax works, but people thinks it looks ugly, so there is an alternative syntax that is more common to use, instead of dot syntax, we draw an arrow:
```C++
cout << sp->x << endl;
```
The arrow (`->`) means the member attribute of the object pointed at, and thus is equivalent to writing `(*sp).x`.

| expression | can be read as                     |
| ---------- | ---------------------------------- |
| x.y        | member y of object x               |
| x->y       | member y of object pointed to by x |
| (*x).y     | member y of object pointed to by x |


## Arrays and Pointers

We have briefly shown how arrays can be created, for example:
```C++
int x[100];
```
Here, `x` will be an array of 100 ints. We can access these by indexing: `x[0]`, `x[1]`, $\ldots$, `x[n-1]`.

Earlier, we stated that an array will be *contiguous* in memory, i.e., each element follows each other directly. We can check this statement by writing out the memory addresses:
```C++
cout << &x[0] << endl;
cout << &x[1] << endl;
cout << &x[2] << endl;
cout << &x[3] << endl;
```
Which prints out:
```C++
0x7ffed0407920
0x7ffed0407924
0x7ffed0407928
0x7ffed040792c
```
Note that the memory address increases by 4 every step (it goes 8->c because it is hexadecimal), this is because memory addresses are in terms of byte (8 bits), and integers are 32-bit variables.

Now comes the "crazy" part, if we write out the array variable itself:
```C++
cout << x << endl;
```
we get:
```
0x7ffed0407920
```
Not only is this a memory address, it's the same address as the first element: `x[0]`. This fact indicates that the array variable `x`, is almost the same as a pointer to the first variable of the array.

Let us highlight this in another way. Look at the following code snippet:
```C++
int x[] = {2, 4, 6, 8, 10, 12};
int *y = &x[2];
```
Here we make an array, and then make an integer pointer and set it to point at the third element, with a value of 6. However, because array variables behave much like pointers to the first element, the reverse is also true. Now `y` will behave like an array:
```C++
cout << y[0] << " ";
cout << y[1] << " ";
cout << y[2] << " ";
cout << y[3] << endl;
```
This is because the square bracket indexing indicates looking at the next elements in memory, and so will behave just like an array. We could also have accessed the elements using *pointer arithmetic*:
```C++
cout << *(y) << " ";
cout << *(y + 1) << " ";
cout << *(y + 2) << " ";
cout << *(y + 3) << endl;
```
Here, dereferencing `y` itself gives the first element, by computing `y + 1` we go the the next integer in memory, which would be element 2, and so on.


Thus, a pointer is variable that stores the memory address of some data type, but if these data lie contiguously in memory, then having the address of the first element is all we need to reference the whole set. Thus, an `int *` pointer, can point to a single integer, or to a whole sequence of them. Note that the pointer itself does not know how many elements it points at, like an array does not know how many elements it contains—meaning you won't get an `IndexError` if you go out of bounds, you get undefined behavior. Be careful!


| expression | can be read as                 |
| ---------- | ------------------------------ |
| x[0]       | first object pointed to by x   |
| x[1]       | second object pointed to by x  |
| x[n]       | (n+1)th object pointed to by x |


## Dynamic Memory Allocation

So far we have seen how to create a pointer object, and how to make it point at something. We have also seen how to point it at "nothing" (aka null). However, we have only pointed it at things that already exist. However, it is possible to get a pointer to point at something brand new. Take a look at the following example:
```C++
int *x;
x = new int;
*x = 5;
```
Here we first create an integer pointer. Then we say we want a new integer object to be made, and its address to point to it. An interesting consequence of this is that we have a variable that *is not named*. We can only access it through our pointer.

Using the `new` keyword in this way is referred to as *dynamic memory allocation*.

### Lifetime of Variables

In C++, things are automatically destroyed once they go out of scope. If you for example define a vector inside a function, then that vector simply ceases to exist once that function finished. Any dynamically allocated memory however, sticks around. Let us look at an example.

We have discussed how arrays are so efficient because they are contiguous in memory, but we find it annoying that they don't remember their size. We therefore decide we want to make a class called `Array` that stores both the data array and the size of it as a single object. We first define the object as
```C++
class Array {
public:
    int *data;
    int size;
};
```
Where `data` is a pointer to the first element of the underlying array, and `size` the number of elements.

Next we turn to making the constructor. When we make the constructor we want to take in the number of elements we want as an integer. The constructor should then allocate the memory of the array, set all the elements to zero, and point the `data` pointer to this array. You might try to do the following, but it won't work:

**(NB: Doesn't actually work)**
```C++
Array(int n) {
    int tmp[n];
    for (int i=0; i<n; i++)
        tmp[i] = 0;
    data = tmp;
    size = n;
}
```
While this looks reasonable, there is a big problem. Whenever a function finishes, everything created inside that function is automatically destroyed. As the array is created inside the constructor, it is destroyed too. Our pointer is set to point at this array, but if the thing pointed at is destroyed, the pointer won't be much good.
If we try to run the following code
```C++
Array a(10);
for (int i = 0; i < a.size; i++)
{
    cout << a.data[i] << " ";
}
```
it produces the output
```
0 1 31872064 1 31872064 1 30535429 1 31872064 1
```
and this output will change every time you run the program.

However, when using dynamic memory allocation, the data is not destroyed at the end of the function, and so will survive. To dynamically allocate an array, we do the following:
```C++
Array (int n) {
    data = new int[n];
    size = n;
    for (int i=0; i<n; i++) {
        data[i] = 0;
    }
}
```
Now we see that we get the expected results.

### Scope and lifetime
A scope is a the region or section where a variable can be accessed and you can think of the scope as the inner most curly braces (`{}`) that encapsulates the variable declaration. This could be in a function, but you can also simple create a scoped variable inside a function. The lifetime of an object is the portion of the program execution during which store is guaranteed to be reserved for it.

Consider the following code
```c++
int main()
{
    int *p;
    {
        int x = 5;
        p = &x;
    }
    cout << *p << "\n";

    return 0;
}
```
Here we define an integer pointer `p` and then inside a local scope (which we just create using curly braces) we create an integer variable `x` and points `p` at it. The problem with this code is that when we exit the scope and prints out the value that `p` points to, `x` does not exist anymore, and so `p` points at some address in memory that are now owned by the program anymore. Note that, you will probably still see `5` printed out on the console, but there is no guarantee that the value stored at this memory address will remain `5`. We call this *Undefined behavior* and this is the root of some of the most tricksiest bugs to debug.

## Deallocating Memory and Garbage Collection

In Python, you are used to having built-in garbage collection. Garbage collection is a term for automatic processes that collects unused variables and destroys them for us, freeing the underlying memory. In Python, any variable that no longer has a name referencing it, is flagged for garbage collection and destroyed.

In C++, there is no garbage collection. Instead, data will be destroyed when it goes out of scope. However, as we just showed you, dynamic memory allocation survives even when it goes out of scope. This means dynamically allocated objects will continue to take memory until we ourselves destroy the objects.

If we *don't* de-allocate memory we have created dynamically, it will continue to take space until our program finished. Often, this isn't a problem, but in certain situations, it can actually lead to program-crashing bugs.

### Memory Leaks

Earlier, we showed this snippet:
```C++
int *x;
x = new int;
*x = 5;
```
If we now do a new dynamic allocation:
```C++
x = new int;
```
Then `x` will point to a new object, but the old one is never freed. The other integer has no name, and we no longer have any pointer to it. We have reached a point where a piece of memory is locked down until the entire program terminates and we have no way of accessing or using that variable.
This is referred to as a memory leak.

A small memory leak is of no issue and not noticeable. However, if you get a large memory leak, the machine will run out of memory and the program and OS will grind to a halt, most likely requiring termination of the program or even a full reboot of the system.


Let us create a program that on purpose leaks a lot of memory:
```C++
void doomsday() {
    while (true) {
        new int;
    }
}
```
Here we define an infinite loop. For each iteration we allocate a new integer in memory, but they are never deallocated. This means, for each iteration of the loop, our program will use a bit more memory (32 bits to be exact).

If we compile our `doomsday.cpp` code, you probably won't get any warnings. But if you now run it, you definitely will get some problems. The program will ask for more and more memory from the system, and never give any back. The program never aborts itself or stops, so it is up to the system to recognize that this program is not acting right and terminate it. Wether or not that actually happens depends on your system. In the worst case, all memory will be hogged by the doomsday program, leaving non for the system. The only way to regain control in this scenario is now a hard reboot of the machine. Not ideal!

When I compile and run my doomsday.cpp program, the memory use of the computer skyrockets. When it maxes out the computer freezes for a few seconds and becomes unresponsive. Turns out my OS is successfully in terminating my program, freeing the memory.



```{figure} ../../figures/armageddon.png
---
width: 100px
name: armageddon
alt: armageddon
---
```


If you want to know how to debug such memory leaks, please consult the [debugging section](cpptools.md)

### Memory leaks in Practice

In practice, memory leaks are hard to detect. The leak doesn't build up as fast as here, but does so over hours or days. When testing software, we often opt for small, efficient tests. And so often everything will seem fine, until we start a long simulation and we get an issue.

Memory leaks, and other similar bugs, sneak into a surprising amount of professional software, and is a major contributor to [*software aging*](https://en.wikipedia.org/wiki/Software_aging), where things seem to become unresponsive or stop functioning when running over a longer time, but return to normal after a reboot.

The wikipedia article on memory leaks has a [good example](https://en.wikipedia.org/wiki/Memory_leak#An_example_of_memory_leak) for how a seemingly "trivial" program for an elevator could contain a memory leak.


### Freeing memory

So if dynamically allocated memory has to be freed, how do we do so? It is quite simple, we use the `delete` keyword:
```C++
int *x;
x = new int;

delete x;
```

Note that `delete x` will free the thing pointed at by `x`, the pointer will still exist and be usable. If we are freeing an allocated array, we instead use `delete[]`:
```C++
int *x;
x = new int[200];

delete[] x;
```

### Rule of Thumb

An easy rule of thumb to remember to avoid memory leak is that your code should have a `delete` statement for every `new` statement you use. Because `new` is the keyword used to dynamically allocate objects, we need to delete them.

Another technique that is recommended in the C++ community is known as *Resource Acquisition Is Initialization* or RAII which says that you should only acquire resources in the constructor and release them in the destructor.

```{admonition} Smart pointers
:class: tip
To prevent memory leaks, [*smart pointers*](https://en.cppreference.com/book/intro/smart_pointers) where introduced in C++11. This is the preferred what to deal with dynamic memory allocation in modern C++ projects, but is beyond the scope of this course.
```

## The Destructor

Returning to our `Array` class example. We defined the following class:
```C++
class Array {
public:
	int *data;
	int size;

	Array(int n) {
		data = new int[n];
		size = n;
		for (int i=0; i<size; i++) {
			data[i] = 0;
		}
	}
};
```
This class works well, and we can now use it inside other functions where we need arrays, however, at the end of those functions, our newly created `Array` object will automatically be destroyed. However, the dynamically allocated memory inside the object won't be!

To ensure that the dynamic memory is deallocated with the object, we need to define a *destructor*, which is called automatically when an object goes out of scope and is destroyed. Where as the constructor is named the same as the class, the destructor is named the same with a tilde (~) in front:
```C++
~Array() {
    delete[] data;
}
```
You could try this yourself with the simple test program:
```C++
void create_and_destroy_array() {
	Array a(100);
}

int main() {
	while (true) {
		create_and_destroy_array();
	}
}
```
If you run this program without implementing the deallocator, the memory usage of the program will skyrocket. If you do implement the deallocator, then everything is fine, as every function call properly destroys the object and all the underlying data.

## Stack vs Heap

In C++, and many other programming languages, we refer to two different forms of memory: the stack and the heap. Everything you create lives in one of these two memory spaces. Variables you create normally will live on the stack. Every function has its own stack space, and when the function finished, the stack is emptied and the variables destroyed. When you declare variables dynamically, you create them on the heap instead, where nothing is automatically deallocated.

We won't talk much about stack and heap, but you might run across it in other sources, or if you ever learn more about C++ in more dedicated courses.
