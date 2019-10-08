# Learning Python

This repository contains code and experiments useful for scientific computing, data analysis, API development, databases, and web applications. The focus
 is on features of the language and various frameworks.


### Object-oriented programming

The nitty-gritty details of OOP starting from the basics/fundamentals and
 ending up with more advanced concepts.

* Learning Python - Chapter 27 on **default methods**
* Fluent Python - Chapter 1 on the power of **default methods** and
 understanding Python's **data model**
* Corey Schafer - Method decorators and logging
* Callables, Deep Copies


### James Powell - So you want to be a python expert

* Python Data Model: if I want to implement some behavior, top-level function
 and corresponding protocol (dunder method)
* Metaclasses: Understanding the metaphor of library - user and use cases.
* Generators: More than eager vs lazy
* Decorators: Wrapping stuff up
* Context Managers: the set up - tear down metaphor


### Asyncronous programming in Python

* [An Introduction to Asynchronous Programming in Python](https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb)
* [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
* [Python Type Hints](https://www.youtube.com/watch?v=pMgmKJyWKn8)


An exploration of features provided by `asyncIO` *(concurrent programming
 being a superset of parallel programming)* and implications on
  performance for various tasks. Also implies some research and take-aways for
  when is it useful to implement it, for example **multiprocessing** would be
  suitable for CPU-bound tasks.

> Async IO takes long waiting periods in which
  functions would otherwise be blocking and allows other functions to run during
  that downtime.

> A coroutine is a function that can suspend its execution before reaching
> return, and it can indirectly pass control to another coroutine for some time.

### Python type hints

The **implicit** contract, but the problem is maintenance. I have to re
-establish the types. Monkeytype runs a script/test and identifies the types
 used, then dumps them.

```bash
# for type checking
pip install mypy typing-extensions monkeytype
mypy 01_items.py  # bunch of errors

monkeytype run mytests.py
monkeytype stub some.module
monkeytype apply some.module
```

```python
def process(self, items):
    for item in items:
        self.append(item.value.id)
```

### Python testing

A brilliant [workshop](https://www.youtube.com/watch?v=LX2ksGYXJ80&t=3750s) by John Leeman and Ryan May. The course page is [here](https://leemangeophysicalllc.github.io/testing-with-python/).


### Getting started
Given an installation of Python 3.7, packages can be isolated in a virtual
 environment on MacOS/Linux:

```bash
#!/bin/bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
