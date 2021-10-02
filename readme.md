Welcome to this project that explores the difference between a functional paradigm and an object oriented paradigm using
Python.

# Requirements

Both "paths" of code will attempt to do the following:

- Create and read objects
- Describe properties on those objects
- Read from two 3rd parties with different APIs
- Write to two 3rd parties with different APIs
- Represent data using Pydantic and dataclass objects

Shared goals:

- Minimize coupling between dependencies
- Write clear code
- Make testing easier

# Shapes - Object-Oriented

The Shapes API and implementation will follow object-oriented patterns.

It will use:

- Classes
- Factories
- Dependency Injection

# Colors - Functional

It will use:

- Modules with functions
- Dynamically loaded implementations

# Symbols - Single File

It uses a single file to meet the requirements but closely couples everything (being that it's in the same file).

Provided as an example to summarize the end-to-end implementation without the abstraction layers.
