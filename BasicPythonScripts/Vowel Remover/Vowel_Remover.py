import re

def vowel_remover(string):
    new_str = re.findall("[^aeiouAEIOU]+", string)
    for txt in (new_str):
        print(txt, end = '')

input_text = input('Enter input text: ')
vowel_remover(input_text)