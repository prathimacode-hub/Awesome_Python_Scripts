# install quote library using pip install quote 
# import quote from quote library
from quote import quote
import random

try:
    print("Tell me the author or person name?")
    
    # taking the name as input to get the quotes related to that author/person 
    q_author = input()
    
    # getting the quotes into quotes variable
    quotes = quote(q_author)
    
    # selecting a random quote from multiple quotes
    quote_no = random.randint(1, len(quotes))
    
    # displaying the quote with author name
    print("Author: ", quotes[quote_no]['author'])
    print("-->", quotes[quote_no]['quote'])

except Exception as e:
    pass
