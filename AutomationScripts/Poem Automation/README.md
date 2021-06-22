# Poem Automation
For Poem Automation we are using `poetpy` which is a python library used to get poems of any author. The `poetpy` library is an unofficial Python wrapper for the PoetryDB API. 

The PoetryDB API allows users to find a vast amount of poetry and poet data and is free to use without any authentication required. 
We can also call it as a fun python library that can be used simply with some lines of code.

**Note:** It requires proper Internet connection for its working.

### Install

Install with `pip` command in any terminal
```python
pip install poetpy
```
### Working

Import the `poetpy` library in the Python file that you are going to get the poems and then use the `get_poetry()` function to easily get poems into your console/application.

For example, we are interested in finding all of William Shakespeare’s poems and sonnets available in the PoetryDB API then

```python
import poetpy

poems = poetpy.get_poetry('author', 'William Shakespeare')

print(poems)

```

### Screenshots

#### In CLI

<img src="">

#### In PyCharm

<img src="">
