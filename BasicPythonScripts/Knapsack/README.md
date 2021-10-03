# Title:-
A naive recursive implementation of 0-1 Knapsack Problem

## Short Description:-
This overview is taken from:
https://en.wikipedia.org/wiki/Knapsack_problem

The knapsack problem is a problem in combinatorial optimization: Given a set of items,each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possibl

## Detailed explanation:-

This module uses docstrings to enable the use of Python's in-built `help(...)` function.
For instance, try `help(Vector)`, `help(unitBasisVector)`, and `help(CLASSNAME.METHODNAME)`.

Example: 
```sh
    $ python3 -i knapsack.py
    >> help(knapsack)
```

Output:
```sh
    Help on function knapsack in module __main__:

    knapsack(capacity: int, weights: List[int], values: List[int], counter: int) -> int
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val.
    
    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack(cap, w, val, c)
    220
    
    The result is 220 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
```

## Tests:-

`.` contains Python unit tests which can be run with `python3 -m unittest -v`.
## Output Test:-
    
```sh
    $ python3 test_knapsack.py 
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

```

## Author(s):-
[Danang Haris Setiawan](https://github.com/danangharissetiawan)

