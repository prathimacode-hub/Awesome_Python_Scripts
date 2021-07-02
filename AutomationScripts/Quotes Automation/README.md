# Quotes Automation
For quotes automation we are using `quote` library which is a python wrapper for the Goodreads Quote API. 
To generate a random quote we will be using the quote function from the quote module.

### Installation

Install with `pip` command in any terminal
```python
pip install poetpy
```

OR

```python
pip install -r requirements.txt
```

### Working

It is simple to use and `quote` library can also be used from the command line tool.

```python
from quote import quote

author = 'Albert Einstein'

result = quote(author, limit=2)

print(result)
```

### Output
#### In PyCharm

<img src="https://github.com/Umesh-01/Awesome_Python_Scripts/blob/patch-7/AutomationScripts/Quotes%20Automation/Images/quotes_img1.png">

<img src="https://github.com/Umesh-01/Awesome_Python_Scripts/blob/patch-7/AutomationScripts/Quotes%20Automation/Images/quotes_img2.png">

#### In CLI

<img src="https://github.com/Umesh-01/Awesome_Python_Scripts/blob/patch-7/AutomationScripts/Quotes%20Automation/Images/quotes_img3.png">

<img src="https://github.com/Umesh-01/Awesome_Python_Scripts/blob/patch-7/AutomationScripts/Quotes%20Automation/Images/quotes_img4.png">

### Contributor

<a href="https://github.com/Umesh-01">Umesh Singh</a>
