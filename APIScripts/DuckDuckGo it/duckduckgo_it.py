import requests # This module will help extract data

def main():
    
    while True:
        try:
            print('\n\n')
            search_for = input('search for: ')      # Input string to search 

            response = requests.get(f'http://api.duckduckgo.com/?q={search_for}&format=json')   # Send request with {search_for} variable
            response = response.json()      # The result will be in json format
                                            # it will be in key, value pair which will be easy to find answers

            # Printing search result here we will print the values of keys inside brackets
            print('Heading:',response['Heading'])    
            print('\nAbstract:',response['Abstract'])  
            print('\nAbstract source:',response['AbstractSource'])
            print('\nAbstract text:',response['AbstractText'])    
            print('\nDefinition:',response['Definition'])    
            print('Related Topic:')
            
            related_no = 2          # Show only no of text in realted topics
                                    # Sometimes tere are less related topics so keep related no low
            for i in response['RelatedTopics']:     # Loop through Text in RelatedTopics
                if related_no <= 0:
                    break
                print(i['Text'])
                related_no = related_no - 1
                
        except KeyboardInterrupt:       # ctrl+c will call KeyboardInterrupt and while loop will stop
                                        # it will stop execution of code and will print Exiting..
            print('\nExiting..')
            break
    

if __name__ == '__main__':
    main()
