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

# Linked Lists

This lecture marks the start of a new topic in IN1910, namely the Algorithms and Data Structures part of the course, which we will spend the next two weeks on. We have spent the *previous* two weeks of IN1910 learning some C++. As mentioned, the main goal of learning C++ was to familiarize you with C-style programming syntax. We are through covering new material in C++, but will spend the next two weeks using it for our exploration of data structures, so you will get further possibility to learn to use the language more.

## Data Structures and Algorithms

A data structure is how data is organized and managed. More precisely, it is about how a collection of data items are stored collectively, how they relate to each other, and what operations we can perform on them. Understanding data structures is important when trying to make efficient programs, because different problems and implementations calls for different data structures.

Algorithms are tightly connected to data structures, because to implement a data structure, we need to understand the algorithms needed to get that data structure to work. But also because implementing an algorithm to solve some problem will rely on what data structure you choose to work with, different underlying structures call for different algorithms.

Data structures and Algorithms is one of the fundamental topic of computer programming, and if you want to work as a software developer, you really need to know it. This is reflected in the fact that there are numerous books and university classes called precisely "Data Structures and Algorithms", or alternatively: "Algorithms and Data Structures". We only have a few weeks dedicated to this topic, so it is obvious that we cannot give you a proper introduction into the topic. However, we aim to give you a small taste, and an understanding of what a data structure actually is and why it is important.

## External Resources

At UiO, the course [IN2010 – Algorithms and Data Structures](https://www.uio.no/studier/emner/matnat/ifi/IN2010/index-eng.html) (previously INF2220) focuses more in-depth on the topic, and comes highly recommended for anyone who wants to become a better programmer, and it's pretty much a prerequisite course to take if you want to go further into computer science. Note that IN2010 uses Java as its language, but having learned some C++, the course will build on what we do in IN1910 quite nicely.

As mentioned, there are also hundreds of books on this subject, some probably better than others. Not only are there many to choose from, there are probably several to choose from dedicated for each programming language you might want to use. We will recommend the book used by IN2010, [*Algorithm Design and Application* by Goodrich and Tamassia](https://www.wiley.com/en-us/Algorithm+Design+and+Applications-p-9781118335918) as that is probably the best choice if you want to get a dedicated book and might be taking IN2010 in the future.

```{figure} fig/goodrich_and_tamissa.jpg
---
width: 175px
name: goodrich-and-tamissa
---
Book used by IN2010, [*Algorithm Design and Application* by Goodrich and Tamassia](https://www.wiley.com/en-us/Algorithm+Design+and+Applications-p-9781118335918)
```

Another excellent resource to use are the teaching materials for the [MIT course 6.006 *Introduction to Algorithms*](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/). The course materials are openly available through Open CourseWare, with recorded video lectures. This course covers the theory behind many data structures and algorithms, and so works well with any programming language, but mostly uses Python for example code. Note that 6.006 goes into many topics we won't cover, but they also have lectures that cover what we do in IN1910.


## Data Structures vs Abstract Data Types

In the previous lecture, we covered [Dynamic Arrays](https://en.wikipedia.org/wiki/Dynamic_array), also known as Array Lists. And this is an example of a data structure, as it is a specification on how data values are to be stored, and interacted with. In that lecture, we implemented a class, and then had to continuously swap to think between how things worked "inside the class", and how they looked from "outside the class", i.e., how the class is actually used.

We now want to formalize these concepts a bit. The term *data structure* refers to the specific and concrete implementation of how data is represented and stored. It is a low-level construct, that we mostly have to think about when *implementing* something.

When using the class however, we instead talk about the *data type*, or even the [*abstract data type*](https://en.wikipedia.org/wiki/Abstract_data_type) (ADT). An abstract data type is, as the name implies, a more abstract definition and is a mathematical model for the behavior of the construct from the *users* perspective. Specifically it is the collection of possible values to be stored in the construct, the possible operations on that data, and the behavior of those operations.

So data structure is the low-level construct from the perspective of the implementer, while the abstract data type is the high-level construct, built on top of the data structure, which is what the user actually interacts with.

An example of an abstract data type is the [list ADT](https://en.wikipedia.org/wiki/List_(abstract_data_type)). This is a specification that a *list* is something which can store a sequence of elements, has methods to find the number of elements stored, methods for inserting or appending new elements, etc. You should be familiar with this ADT, because Python lists for example, would be a specific implementation of this list ADT. Another example of an ADT is the [associative array](https://en.wikipedia.org/wiki/Associative_array), while the name might be unfamiliar to you, you have probably used this ADT, because python dictionaries are associative arrays.

Note that if we want to implement to specific ADT, say for example a list, there will often be many different underlying data structures we can choose when we implement it. In the case of the list, dynamic arrays would be a natural choice, as we have already seen. Another option would be *linked lists*, a data structure we will cover in this lecture.

```{figure} fig/data_structure_vs_adt.png
---
width: 400px
name: data-structure-vs-adt
---
An abstract data type is the interface the user has to interact with, it defines the possible operations on the data and how they behave. The underlying data structure is more specific to how data is represented and stored in memory, it is mostly the implementer who has to think about the data structure. As shown, different data structures can be used to implement a given ADT, lists can for example be made with dynamic arrays *or* with linked list. This will be different from the perspective of the implementer. But when using the class, we won't really need to think about the underlying data structure, as the same operations will be supported.
```



## Linked Lists

We now turn to look at linked lists, which is an alternative data structure to dynamic arrays for implementing lists. Unlike dynamic arrays, linked lists do not rely on storing data in arrays, but instead store each element of the list in an individual structure we call a *node*.

A node object stores the value of the element itself, but it also contains a pointer to another node. We can use this pointer to *link* different nodes to each other and create a *linked list*. In this lecture we will only consider lists that store *integers*. However, the value field of the nodes could simply be changed to store any kind of object. In C++, it would be best to use *templating* to define a single list class that can contain any type of data, but we disregard this here to keep things as simple as possible.


```{figure} fig/single_node.png
---
width: 175px
name: single-node
---
A single node object.
```

When link a series of nodes, they form a linked list. We let the list end by having the final node point at a nullptr. In Figure 3, we have a chain of linked nodes, which would correspond to a list `[47, 3, 12, 99, 23]`.


```{figure} fig/node_chain.png
---
width: 800px
name: node-chain
---
A chain of node objects.
```


To simplify our drawings of linked list, we change to drawing our nodes as simple circles, writing their value inside, and the pointer as an arrow.



```{figure} fig/simplified_node_chain.png
---
width: 800px
name: simplified-node-chain
---
A simplified drawing of a linked list.
```

This structure defines a clear sequence of integer values. We can also iterate over this list, if we have a reference to the first value, we can do something to this value, for example print it, and then use the `next` pointer to move to the next element in the list, and thus iterate our way through it.


### Making the Nodes

Implementing the node itself is very simple, we can do it as a simple struct:
```C++
struct Node {
    int value;
    Node* next;
};
```
Note especially the asterisk, making `next` a node *pointer*.

In addition, to ease our use, we can implement two constructors. The first takes just a value, and then initializes the `next` field to be a nullptr.
```C++
Node(int n) {
    value = n;
    next = nullptr;
}
```
While the next initializes both values:
```C++
Node(int n, Node* p) {
    value = n;
    next = p;
}
```
Note that we implement the constructor as a call-by-pointer, i.e., we will need to send a pointer into the constructor. Alternatively we could have used a call-by-reference here.

### Linking Nodes

With the `Node` struct defined, we can try to create a few nodes and link them as follows:
```C++
Node a(12);
Node b(57);
Node c(36);

a.next = &b;
b.next = &c;
```
However, this is *not* how we want to use our linked list, instead we want to build a list class based on the nodes. So let us define a `LinkedList` class.


### Creating a list class based on linked list

To interact with our linked list, we need to have a reference to the first node of our linked list. This node is often referred to as the *head* of the list. If our list is empty, the head of the list must not point at anything. We can then set up the class as follows:
```C++
class LinkedList {
  private:
    Node* head;

  public:
    LinkedList() {
        head = nullptr;
};
```


#### Appending to LinkedList

Now, let us try to make an `append` method, for adding an element at the end of the list. Let us first consider how to do this for a completely empty list.

For an empty list, the `head` pointer, is pointing at `nullptr`. We want it to instead point to a new node. To do this, we need to use the `new` keyword to dynamically allocate memory for a new node. So for an empty list, we would do:

```C++
void append(int val) {
    if (head == nullptr) {
        head = new Node(val);
    }
}
```
However, what do we do if there already are some elements in the list? In this case we *shouldn't* change the `head` pointer, because appending should add the new element to the end of the list, the front of the list should be unchanged.

What we want to do, is get the `next` pointer of the final node in the list to point to the new list, so first need to get access to this final node. We can do this by iterating through all nodes in the list, using `next` on each node to move on step down the list. How do we know we have reached the end? The first node to point at a nullptr must be the end. So we can use a while-loop:
```C++
void append(int val) {
    if (head == nullptr) {
        head = new Node(val);
        return;
    }

    // Iterate to end of list
    Node* current;
    current = head;
    while (current->next != nullptr) {
        current = current->next;
    }

    // Link new node to end of list
    current->next = new Node(val);
}
```
Take a minute to go through this code. Especially verify that it works if the list has 0 elements before appending, if it has exactly 1 before appending, and if it has more than 1 element before appending.


#### Printing a linked list

Now, let's add a `print`-method to print out the contents of the list. To do this we need to iterate through the list, printing out the value of each node. We keep going until we reach the end of the list:
```C++
void print() {
    Node* current = head;
    cout << "[";
    while (current->next != nullptr) {
        cout << current->value;
        cout << ", ";
        current = current->next;
    }
    cout << current->value << "]" << endl;
}
```
We can now test our program by appending a few elements, and then printing out the list:
```C++
LinkedList primes;
primes.append(2);
primes.append(3);
primes.append(5);
primes.append(7);

primes.print();
```
```
[2, 3, 5, 7]
```

#### Destroying the list

As we are dynamically allocating the nodes with the `new` keyword, we should also deallocate the nodes when they are no longer useful. Let us add a destructor method to our class. This method should go through the list, deallocating each node, one by one. When we destroy a node, we also loose access to its `.next` attribute, so we should copy this reference over to a temporary object, before we delete the node itself.
```C++
~LinkedList() {
    Node* current;
    Node* next;

    current = head;

    while (current != nullptr) {
        next = current->next;
        delete current;
        current = next;
    }
}
```

This seems reasonable, we have used one `new` for each node in the list, and this while-loop should have a `delete` for each node, meaning no memory should be leaked. But, as is always smart in programming, we should plan for mistakes and human error. So how can we verify we are not leaking any memory?

One method is to use a simple tool to check the memory use on execution, one such tool is *valgrind* (see also [debugging section](cpptools.md)). This tool is available on Unix systems, for Windows, you will need to look somewhere else, for example the Visual Leak detector made for Visual C++.

After installing valgrind, you can run
```C++
valgrind --tool=memcheck <your executable>
```
To run an executable and see if it seems reasonable. Running our simple example above, with 4 appends and a print, *before* adding the destructor method, we get the following (slightly simplified) report:
```
$> valgrind --tool=memcheck ./example

==8382== Memcheck, a memory error detector
==8382== Command: ./example
[2, 3, 5, 7]
==8382== HEAP SUMMARY:
==8382==     in use at exit: 64 bytes in 4 blocks
==8382==   total heap usage: 6 allocs, 2 frees, 73,792 bytes allocated
==8382==
==8382== LEAK SUMMARY:
==8382==    definitely lost: 16 bytes in 1 blocks
==8382==    indirectly lost: 48 bytes in 3 blocks
==8382==      possibly lost: 0 bytes in 0 blocks
==8382==    still reachable: 0 bytes in 0 blocks
==8382==         suppressed: 0 bytes in 0 blocks
```
In this case we get information that some memory is leaked. This is because when the program is finished and wrapping up, it starts deallocating and destroying variables. When the `primes` list is deleted, the dynamically allocated nodes are *not* (because we ran this before implementing the destructor method). So we see that we have "16 bytes in 1 blocks" marked as "definitely lost", this is our `head` node. In addition we have "indirectly lost" 46 bytes in 3 blocks, these are the other three nodes. These aren't directly lost, but lost because we needed our `head` pointer to get to them.

After implementing the destructor `~LinkedList` method, we rerun the analysis and get:
```
$> valgrind --tool=memcheck ./example

==8926== Command: ./example
[2, 3, 5, 7]
==8926== HEAP SUMMARY:
==8926==   in use at exit: 0 bytes in 0 blocks
==8926==   total heap usage: 6 allocs, 6 frees, 73,792 bytes allocated
==8926== All heap blocks were freed -- no leaks are possible
```
Which tells us that all memory which was used was also freed at the end of execution, as desired. And thus no leaks exist in our simple test case. Note that this not guarantee that no leaks are possible in other use cases of the list, but it is a simple test that have supported our implementation.

### Length

Another important aspect of a list is that is has some given *length* or *size*, which is the number of elements stored in the list. For our implementation, we could define a method that finds the number of elements through iterating through them:
```C++
int length() {
    Node* current = head;
    int count = 0;

    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;
}
```
This would work nicely, but it is not very efficient to have to iterate through the entire list every time we want to know the number of elements we have. To improve this, and make the `length` method more efficient, we could simply add a `size` or `count` field to the class itself, initializing it to 0 (for an empty list) and be sure to update it manually every time an element is added or removed. Say we define a private attribute `int size;`, then we can make our length method as:
```C++
int length() {
    return size;
}
```

### Indexing

An important aspect of lists is that we can use indices to go in and get or set elements. Let us implement this for our linked list. Here we could add a method called `get`, but let us instead overload the `[]` operator, so we can use square bracket indexing, as we are used to with sequences.
```C++
int& operator[](int index) {
    if (index < 0 or index >= size) {
        throw range_error("IndexError: Index out of range");
    }

    Node* current = head;
    for (int i=0; i<index; i++) {
        current = current->next;
    }
    return current->value;
}
```
So, to get element $i$, we start at the head of the list and iterate to element $i$, before returning it. If we are accessing elements high up in the list, this might seem really inefficient. However, what other option do we have? We have to start at the head, as this is the only reference we have in our list, and we have to use the `next` pointers to move along the list.

Note also that we return `current->value`, i.e., the value stored in the given node, not the node itself. This is because if our list is storing integers, then it is the integer we want when we index. If you forget the `->value` part and only write `return current;`, your compiler will complain, because the function definition says `int& operator[]`, but you are returning a node pointer, not an integer reference.

It might be nice to also make a `Node* get_node(int index)` method, but this we would prefer to make private, as we do not want the user of our class to have to think about or interact with the nodes. Recall the difference between the data structure (nodes and linked list), which is for the implementer, and the abstract data type (list), which is for the user.

(Private)
```C++
Node* get_node(int index) {
    if (index < 0 or index >= size) {
        throw range_error("IndexError: Index out of range");
    }

    Node* current = head;
    for (int i=0; i<index; i++) {
        current = current->next;
    }
    return current;
}
```
If we implement this method, we can simplify the public `int& operator[]` method to:
```C++
int& operator[](int index) {
    return get_node(index)->value;
}
```

### Iterating over the Linked List

So far, we have iterated over the linked list a few times using the `next` of each node to take the next step, inside a while-loop:
```C++
Node* current = head;
while (current != nullptr) {
    current = current->next;
}
```

Outside the loop however, we cannot iterate in the same way, because we have set `head` to private. And for good reason, we don't want a user of the list to have to think about the structure of the linked list and its implementation details, if they had access to `head` or had to use the nodes directly, it wouldn't be as elegant and foolproof.

Instead we might think, we just implemented indexing, so we can just do
```C++
for (int i=0; i<example.size(); i++) {
    example[i];
}
```
To iterate through some list called `example`. However, if you recall how we implemented the get-operation, this is far from perfect, because to index element $i$, we started at the front of the list and iterated through it to reach $i$. In our for-loop here, we first refer to element 0, then element 1, then element 2. Every time we iterate over a new element, the get-operator will start iterating all the way at the head. This is far from perfect!

To get around this, we would like to implement our class in such a fashion that we could for example write:
```C++
for (int p: primes) {
    cout << p << endl;
}
```
For a given list `primes`. This is the same syntax we can use on the `vector` class for example. To get this functionality, we have to create a custom *iterator* for our `LinkedList` class, and this *iterator* would keep track of the last visited node, and just use `next` to iterate one element, making the whole process effective.

However, we have not covered *iterators* in IN1910, and making them is finicky enough that we won't take the time to do this here.

### Inserting into front of the list

Sometimes, we might not want to insert elements at the end of the list, i.e., we do not want to "append" elements, instead we want to "pre"pend, or insert at the front. For our linked list, this is actually very simple! We simply need to make the new element our `head` and then point from our new node to the old head.

Because we overloaded the `Node` constructor, we can actually manage this in a single line:
```C++
void push_front(int val) {
   head = new Node(val, head);
}
```
### Inserting into middle of the list

Now, what if we instead want to insert into the middle of the list, say at index $i$? Well, then we need the node before it, i.e., node $i-1$ to point to the new node, and the new node to point at the node that was previously node $i$.

When performing these steps, we do not want to use `get_node` more than once, because iterating from 0 to $i$ more than once is really inefficient. So let us do as follows:
```C++
void insert(int val, int index) {
    Node* prev = get_node(index-1);
    Node* next = prev->next;
    prev->next = new Node(val, next);
}
```
Before moving on, we should verify that this also works if we are trying to insert at the last node of the list, as this might be an edge-case we got wrong that might lead to an error at a later time. We leave this as an exercise to the reader.

#### Different inserts

If the different insert methods: `append`, `push_front` and `insert` got you confused, that is understandable. Let us compare them a little. First, the `insert` method inserts at any index in the list. If we do insert at index 0, this is the same as using `push_front`, if we do insert at the end of the list, i.e., index $N$ for a list with $N$ elements, we are effectively appending an element.

We draw the three situations below. If you are still confused, we recommend you draw up a linked list, and then try to insert elements by drawing in new nodes and moving pointers around yourself.

```{figure} fig/insert_linked_list.png
---
width: 250px
name: insert-linked-list
---
Different way of inserting elements into the linked list
```

### Linked List Variants

The linked list data structure we have created so far is only the very simplest kind of a linked list. We call it a *singly* linked list, because each node connects to the next one with a *single link*. We could for example also make a *doubly linked* list, where each node has a `next` pointer, but also a `previous` pointer, so that we can iterate the list in either direction. Similarly, there are *circularly linked lists*, where we connect the final node to the first node again. For even more examples, take a look at the [Linked List Wikipedia article](https://en.wikipedia.org/wiki/Linked_list).

We will come back to some of these variants, to understand how they differ from our implementation in the next lecture.


## Comparing Dynamic Arrays and Linked List

We have now taken some time to look at linked lists in detail, and in the last lecture, we look at dynamic arrays. As we have seen, both can be used to implement the list abstract data type. Now, we want to take a step back and look at how the choice in the underlying data structure affects the *performance* of the final list object.

However, before we do this, we need to learn a little more about algorithm analysis. We therefore spend the rest of this lecture on algorithm analysis, and return to comparing the data structures in the next lecture.
