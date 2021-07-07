def menu():
    '''
    function holding the menu
    Returns: string
    '''
    return (
    '''
----------------------------------------------------------
Welcome to the Number Base converter!
The system will ask you for:
- The Number to convert
- What base you want to convert FROM
- What base you want to convert TO

** REMEMBER: All numbers must be integers!(unless HEX) **
----------------------------------------------------------
    ''')

def validate_bin(check_number):
    '''
    function that checks if the input consists of either 0 or 1.
    Binary numbers can only be 0 or 1, so we need to validate this
    before doing any math on it.

    returns: True/False
    '''
    check_list = [int(item) for item in (sorted(set(list(str(check_number)))))]

    for number in check_list:
        print (f'checking {number} - {type(number)}')
        if number not in [0,1]:
            print (f'invalid binary number')
            return False
    return True

def validate_input(input_number):
    '''
    function that checks if the input consists of legal characters.
    Binary numbers can only be 0 or 1, so we need to validate this
    before doing any math on it.

    returns: True/False
    '''
    legal_char = '0123456789abcdef'
    for number in input_number:
        if number not in legal_char:
            return False
    return True

def validator(input_number,input_base,output_base):
    if validate_input(input_number) and input_base.isdigit() and output_base.isdigit():

        if int(input_base) == 2:
            if not validate_bin(input_number):
                print ('ERROR: Invalid Binary Number. Must contain 0s or 1s')
                return False

        if input_number.isdigit() and input_number.isalpha():
            if int(input_base) != 16:
                print ('ERROR: Hexadesimal numbers requires base FROM to be 16')
                return False

        if int(input_base) == 1 or int(output_base) == 1:
            print (f'can not convert to or from Base-1')
            return False
        return True




def convert_number_system(input_number, input_base, output_base):
    '''
    function that calculates numbers from one base to the other

    returns: int, converted number
    '''

    #list that holds the numbers to output in the end
    remainder_list = []

    #start value for sum_base_10. All calculations go thorugh base-10.
    sum_base_10 = 0

    #validate_input


    if output_base == 2:
        binary_repr = bin(input_number)
        return (binary_repr[2:])

    # we coulc use python's built in hex(), but it is more fun not to...
    #if output_base == 16:
        #hex_repr = hex(input_number)
        #return hex_repr[2:]

    # we want to convert to base-10 before the actual calculation:
    elif input_base != 10:

        # reverse the string to start calculating from the least significant number
        reversed_input_number = input_number[::-1]

        #check if user typed in letter outside HEX range.
        hex_helper_dict = {'a' : 10 , 'b' : 11 , 'c' : 12 , 'd' : 13 , 'e' : 14 , 'f' : 15}


        for index, number in enumerate(reversed_input_number):
            for key,value in hex_helper_dict.items():
                if str(number).lower() == key:
                    number = value

            sum_base_10 += (int(number)*(int(input_base)**index))

    # if the number is already in Base-10, we can start the convertion
    elif input_base == 10:
        sum_base_10 = int(input_number)


    # we loop through until we hit 0. When we hit 0, we have our number.
    while sum_base_10 > 0:

        #find number to pass further down the loop
        divided = sum_base_10// int(output_base)

        #find remainder to keep
        remainder_list.append(str(sum_base_10 % int(output_base)))

        # the new value to send to the next iteration
        sum_base_10 = divided


    #fix the list and send a number:
    return_number = ''

    # if the user asked for a Hexadesimal output, we need to convert
    # any number from 10 and up.
    if output_base == 16:
        hex_dict = {10 : 'a' , 11 : 'b' , 12 : 'c' , 13 : 'd' , 14 : 'e' , 15 : 'f'}

        #loop through remainder_list and convert 10+ to letters.
        for index, each in enumerate(remainder_list):
            for key, value in hex_dict.items():
                if each == str(key):
                    remainder_list[index] = value

    #return the number:
    else:
        for each in remainder_list[::-1]:
            return_number += each

        return (return_number)
    #else:
        #return ('invalid input... Please Try Again')

def execute_converter():
    '''
    procedure that interacts with the user and sends it to get converted.
    '''
    user_number = ''
    user_input_base = ''
    user_output_base = ''

    proceed = 'y'

    while proceed.lower() == 'y':
        valid_input = False
        while valid_input == False:
            user_number = input('\nPlease type the number you wish to convert: ')
            user_input_base = input('Please type the base you wish to convert FROM (e.g. 10): ')
            user_output_base = input('Please type the base you wish to convert TO (e.g. 2): ')

            valid_input = validator(user_number,user_input_base,user_output_base)

        print (f'\nTrying to convert The Number {user_number} from a Base-{user_input_base} to a Base-{user_output_base}: ')
        print (f'>> RESULT: {convert_number_system(user_number, user_input_base, user_output_base)} <<')

        print (f'\nDo you wish to convert another number? Type y/n: ')
        proceed = input('')


    print (f'quitting converter...')

if __name__ == '__main__':
    #print the menu:
    print(menu())
    #execute the actual converter:
    execute_converter()