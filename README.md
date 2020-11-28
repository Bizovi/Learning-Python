# Learning Modern Python

Python does a lot of things reasonably well, and grace to the **simplicity**, **introspection** capabilities, and **interactivity** is a perfect tool to get a job done. Add to that the amazing ecosystem for scientific computing and data science, and it becomes not just a **glue language**. 

However, despite the Zen of Python and having a way of writing idiomatic code, there is a forest of options to achieve the same goal. Not having a compiler guide the development, it is important to well design and rigorously test the programs. Therefore, the **goals of this repository** are: 

* Explore the principles, metaphors, language design, and modern tooling
* Focus on learning the **first principles**, such that the right decision can be made in the right context
* Explore different programming paradigms, tradeoffs of choosing a particular style in python, SOLID and Design Patterns
* Emphasis on **modern** approaches and latest developments in the python ecosystem
* Evolve the repository into a resource "I wish I had when was getting started"


# Outline

## Getting started

The repository targets `python 3.8^`, a text editor or IDE like `VSCode` and terminal. There are no jupyter notebooks yet, as they deserve their own "chapter". My setup involves `pyenv` for managing python versions and virtual environments, `poetry` + `pip` for dependency management, and `Docker` + `micropipenv` for containerization. 


```bash
pyenv install 3.8.5               # install an isolated python
pyenv virtualenv learning-python  # create environment & activate
pip install --upgrade pip         # update pip if not up to date

pip install -r requirements.txt   # install the packages
```


## James Powell - So you want to be a python expert

* Python Data Model: if I want to implement some behavior, `top-level function` and corresponding `protocol` (dunder method)
* Metaclasses: Understanding the metaphor of library - user and use cases.
* Generators: More than eager vs lazy
* Decorators: Wrapping stuff up
* Context Managers: the set up - tear down metaphor


## Asyncronous programming in Python

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

## Python type hints

Python type hints are great. But there are a lot of libraries for which stubs aren't available. There is an **implicit** contract, but the problem is maintenance. I have to re-establish the types. `Monkeytype` runs a script/test and identifies the types used, then dumps them.

```bash
# for type checking
pip install mypy typing-extensions monkeytype
mypy 01_items.py  # bunch of errors

monkeytype run mytests.py
monkeytype stub some.module
monkeytype apply some.module
```


## Python testing

* A brilliant [workshop](https://www.youtube.com/watch?v=LX2ksGYXJ80&t=3750s) by John Leeman and Ryan May. The course page is [here](https://leemangeophysicalllc.github.io/testing-with-python/). See the coverage module: `pytest --cov`.
* **Data testing** (processing) with `TDD` and [datatest package](https://datatest.readthedocs.io/en/stable/) from a pydata workshop.