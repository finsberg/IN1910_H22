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

# Dynamic Arrays, aka, Array Lists

We now turn to something different, where we use what we have learned in C++ so far, to implement a data structure.

In Python you are used to using lists, but have you ever thought about how they actually work, behind the scenes? In C++, we claimed a similar object is the *vector*. What we will do now, is assume that python lists/c++ vectors do not exist, and instead build our own from the bottom up.

To make such "list" objects, we will use a technique called *dynamic arrays*, not to be confused with dynamically allocated arrays, which is what we discussed earlier. An alternative name is *array lists*, because we will be using arrays to create a list class.

## Arrays with variable size

One of the most important things we want to be able to do to our list objects, is append new elements to them. However, in C++, arrays are created with a certain size, and once created, cannot change size. So how could we possible append elements to this array?

We cannot resize an array, but we will *fake* it, using some clever encapsulation. When allocating the array, we simply make it much bigger than what we want to store, that way, we have extra memory reserved when we want to append additional elements.

Inside the class, we store the actual data array we use (which is static in size). We also store a private variable `capacity`, that is a measure of how long the actual array is. We also have a public `size` variable, that denotes how many elements are actually stored in the array. From the outside, the array will look like it is this big.

```C++
class ArrayList {
private:
    int *data;
    int capacity;

public:
    int size;
```

## Constructor and Destructor
We now make the constructor. For now, we say a new object will start empty, so we let `size` be 0. The capacity we set to some large number and then we allocate the large array.
```C++
ArrayList() {
    size = 0;
    capacity = 10000;
    data = new int[capacity];
}

~ArrayList() {
    delete[] data;
}
```

## Appending
Next we add a public method for appending a new element to our list. When we append an element, we want it to go to the first unused location in our storage array, this will be `data[size]`, because the indices $0, 1, \ldots, n-1$ are used for actual storage. However, if we go over our allocated capacity we are in danger, so we should check for this explicitly:
```C++
void append(int n) {
    if (size < capacity) {
        data[size] = n;
        size += 1
    } else {
        throw range_error("Capacity full");
    }
}
```
Now we can append elements to our list, and they will be stored in the underlying array. As long as we do not go over our initially allocated capacity, everything works fine.

## Getting
We will also need to have some way of accessing the stored elements, as they are stored in a private array. We define a getter. This getter takes the index of the element you want, and sends a reference to the entry back, so that the variable can be changed if desired:
```C++
int& get(int i) {
    if (0 <= i) and (i < size) {
        return data[i];
    }
}
```
Note that we explicitly check if `i < size`, otherwise the user would be able to access parts of the storage array that are not filled, which goes against the whole point of our class.

## Testing

We have now implemented enough functionality to test our class:
```C++
int main() {
	ArrayList example;
	example.append(0);
	example.append(0);
	example.append(0);
	example.append(0);

	example.get(0) = 10;
	example.get(2) = -10;

	for (int i=0; i<example.size; i++) {
		cout << example.get(i) << endl;
	}
}
```
And we see that our class behaves as we want.

To make future testing easier, we can add a print method:
```C++
void print() {
    cout << "[";
    for (int i=0; i<size-1; i++) {
        cout << data[i];
        cout << ", ";
    }
    cout << data[size-1] << "]" << endl;
}
```

An we can also overload the constructor to take in some initial data if desired:
```C++
ArrayList(vector<int> initial) {
    size = 0;
    capacity = 10000;
    data = new int[capacity];

    for (int e: initial) {
        append(e)
    }
}
```
And then we can do something like
```C++
ArrayList example({0, 5, 10, 15});
example.print();
```

## Indexing

While our `get` method works well for getting out the specific elements, we would like to be able to index specific elements. This we can implement by overloading the `[]` operator. This is like a Python special method, by using a specific name, we can redefine the behavior of square bracket indexing.
```C++
int& operator[] (int i) {
    if (0 <= i and i < size) {
        return data[i];
    } else {
        throw out_of_range("IndexError");
    }
}
```
Note that the contents of this method is identical to our `get`, it just has a different name.

## Capacity Issues

We have so far created a class that from the outside acts much like a `vector<int>` object, in that we can append new integers to it, and interact with it using indexing. It also remembers its own size which we can read out through the `.size` attribute. However, our implementation has some issues, namely the fixed capacity.

The number 10000 was completely arbitrary, and can create issues in either direction. Say we want to create a list with several million elements, this would not work. On the other hand, say we want to create thousands of lists of only a handful of elements, this would be horribly inefficient, as every single list would take up a large chunk of unused memory.

## Dynamic resizing

To get around these issues, we need to be able to *adjust the capacity* as needed. Let us start of with a smaller capacity, say 10:
```C++
ArrayList() {
    size = 0;
    capacity = 10;
    data = new int[capacity];
}
```
Now we will hit our max capacity much sooner, but when this happens, instead of throwing an error, we will *resize* our capacity.
```C++
void append(int n) {
    if (size >= capacity) {
        resize();
    }
    data[size] = n;
    size += 1;
}
```
But how can this `resize` method work? After all, we are not allowed to change the size of the underlying storage array. What we can do however, is create a brand new storage array of larger capacity, and copy all the stored values over to the new array. Let us double the capacity every time we resize:
```C++
void resize() {
    capacity *= 2;
    int *tmp = new int[capacity];
    for (int i=0; i<size; i++) {
        tmp[i] = data[i];
    }
    delete[] data;
    data = tmp;
}
```
Here we first create a new storage array with double the capacity, called `tmp`. Next we copy over all the stored values to the new array. Then we delete the old storage array, to free the memory, as it was dynamically allocated. Lastly, we point the `data` pointer to the new storage array. The pointer `tmp` is gone when the function exists.

The resizing fixes both of our problems with our original implementation. As our initial capacity is so small it takes next to no space, we can make many short lists without issue. And if we want to make a very long list, the list will resize automatically, behind the scenes, without our user having to think about it whatsoever.


## Dynamic Arrays, Vector and Python Lists

The `ArrayList` class we have just gone through and described is an example of a *data structure*, which will be topic in the coming two weeks of IN1910. We will go through more of the terminology then. For now, let us take a step back and look at what we have done.

We took arrays, a very low-level and fundamental structure of C++, and used it to implement something that behaves like a list. You might think this was a strange exercise to perform, we already have lists, why would we want to make them from arrays?

The reason we have taken time to cover dynamic arrays, or array lists as we called them, is that this is *precisely how Python lists are implemented*. It is also how the C++ vector class is implemented. They both rely on arrays behind the scenes, which they resize whenever needed.

In both cases, you can go into the documentation or the source code and check this for yourself, but we can also verify it through how the classes behave. For the vector class this is quite easy actually, because the `capacity` variable is public in this class. So we can simply append elements (with the `push_back` method) and see how the capacity grows.

```C++
vector<int> example;

cout << setw(10) << "Nr Elements";
cout << setw(10) << "Capacity" << endl;
cout << setw(10) << example.size();
cout << setw(10) << example.capacity() << endl;

for (int i=0; i<1200; i++) {
    example.push_back(i);
    cout << setw(10) << example.size();
    cout << setw(10) << example.capacity() << endl;
}
```
Which prints the following:
```C++
Nr Elements  Capacity
         0         0
         1         1
         2         2
         3         4
         4         4
         5         8
         6         8
         7         8
         8         8
         9        16
        10        16
        11        16
        12        16
        13        16
        14        16
        15        16
        16        16
        17        32
       ...       ...
```
And so on. So we see that the C++ vector class starts of with a capacity of 0. When adding the first element, it goes to a capacity of 1, and from there it doubles every time more space is needed. We state this by saying it has a growth factor of 2, because every time the capacity increases, it doubles.

Note that if you are compiling with Microsoft's Visual C++ instead of gcc or clang, you will most likely get a different result, as Microsoft's implementation of vector uses a growth factor of 1.5, instead of 2.

In Python, it is a bit more tricky to verify, because we cannot directly access the capacity of the list. However, we can use the `sys.getsizeof` function, which returns the size of an object, in number of bytes.

```{code-cell} python3
import sys

example = []

print("Nr Elements   Bytes")
print(f"{len(example):11} {sys.getsizeof(example):6}")
for i in range(20):
    example.append(i)
    print(f"{len(example):11} {sys.getsizeof(example):6}")
```

So we see the amount of memory used for the list object does not increase with each append, but instead stays constant, and then makes larger steps. This happens when going for 0 to 1, 4 to 5, 8 to 9, 16 to 17. Which indicates that the capacity of the Python list grows as:

$$0, 4, 8, 16, ...$$

While this might look like growth factor of 2, it turns out that the Python list implementation has a more complicated growth factor that changes as the list grows.

You can read more about dynamical arrays on the [wikipedia page](https://en.wikipedia.org/wiki/Dynamic_array), where there is also a table of common implementation and their growth factors.



## Vector vs List

We have stated that C++ are similar to Python lists, and now you can see why we said this, they are both built on the same underlying data structure, dynamic arrays. There is a different data type in C++ called lists, which you can access through:
```C++
#include <list>
```
But this list implementation does *not* use a dynamic array structure, it instead relies on a different structure, called a *linked list*. Which is the topic of the next lecture.
