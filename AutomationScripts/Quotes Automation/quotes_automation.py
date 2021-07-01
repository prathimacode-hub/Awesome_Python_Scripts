from quote import quote
import random

try:
    print("Tell me the author or person name?")
    
    q_author = input()
    
    quotes = quote(q_author)
    
    quote_no = random.randint(1, len(quotes))
    
    print("Author: ", quotes[quote_no]['author'])
    print("-->", quotes[quote_no]['quote'])

except Exception as e:
    pass
