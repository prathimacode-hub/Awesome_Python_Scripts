# Jokes Automation
In this we are using pyjokes which is a python library used to get jokes for programmers. 
We can also call it as a fun python library that can be used simply with some lines of code.    

**Note:** It requires proper Internet connection for its working.

#### Install

Install with pip using any terminal
```python
pip install pyjokes
```

#### Working
Import the `pyjokes` module in the Python file that you are going to get the jokes and then use the `get_joke()` function to easily get a random joke into your console/application.

```python
import pyjokes

joke = pyjokes.get_joke()

print(joke)
```
To get jokes in a specific language and for a particular category though there are not many categories and language but we can use those that are available.

```
import pyjokes

joke = get_joke(language="es",category="neutral")

print(joke)
```

#### Options available for Languages

|Value|Language Name|
|---|---|
|en|English|
|de|German|
|es|Spanish|
|it|Italian|
|gl|Galician
|eu|Basque|
    
#### Options available for Category
|Values|Category|
|---|---|
|neutral|Neutral geeky jokes|
|twister|Tongue-twister|
|all|All types of joke|

#### Screenshots

##### In CLI

![image](https://user-images.githubusercontent.com/83420185/121780953-3b101080-cbc0-11eb-8c8c-b109f4a6f014.png)

![image](https://user-images.githubusercontent.com/83420185/121781088-d73a1780-cbc0-11eb-96d9-97f7990dccb3.png)

![image](https://user-images.githubusercontent.com/83420185/121781022-8d513180-cbc0-11eb-9b4b-0a40bb481f4b.png)

#### In PyCharm













