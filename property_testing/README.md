# Property-based testing in Python: Hypothesis


## Setup and Getting Started

A tooling which simplifies a lot of my workflows and smooths out the transition from development/exploration to production.

* `pyenv` for python versioning and virtual environments
* `poetry` as the package manager
* `micropipenv` for a more lightweight solution than poetry
* `Docker` for APIs and backend development
* `pypi` for a private package server


> Note, when working in VS code, a window reload is needed to pick up a newly created virtual environment.


```bash
pyenv virtualenv 3.8.5 venv_property  # create a virtual environment
poetry init  # follow the command line
poetry install  # install the packages
micropipenv req --method poetry > requirements.txt  # thin wrapper around pip
```