"""
This module will take an input string and print the search result. 
"""
import requests


def main():
    
    while True:
        try:
            print('\n\n')
            search_for = input('search for: ')      # Input string to search 

            response = requests.get(f'http://api.duckduckgo.com/?q={search_for}&format=json')   # Will send request with search_for variable
            response = response.json()      # The result will be in json format

            # Printing search result here
            print('Heading:',response['Heading'])
            print('\nAbstract:',response['Abstract'])
            print('\nAbstract source:',response['AbstractSource'])
            print('\nAbstract text:',response['AbstractText'])
            print('\nDefinition:',response['Definition'])
            print('Related Topic:')
            
            related_no = 2          # Will show only no of text in realted topics
            for i in response['RelatedTopics']:     # Will loop through Text in RelatedTopics
                if related_no <= 0:
                    break
                print(i['Text'])
                related_no = related_no - 1
                
        
        except KeyboardInterrupt:       # ctrl+c will call KeyboardInterrupt and while loop will stop
            print('\nExiting..')
            break
    

if __name__ == '__main__':
    main()
