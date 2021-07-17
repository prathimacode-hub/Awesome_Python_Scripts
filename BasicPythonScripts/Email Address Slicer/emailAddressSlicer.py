def EMAIL_ADDRESS_SLICER():
    """
    Displays the username and domain name of an email address
    : return: None
    """
    # get user's email address
    emailAddress = input('Enter your email address: ').strip()
    try:
        # make a list with the email address
        split_address = emailAddress.split('@')
        # get both the username and domain name
        # using list indexing
        user_name, domain_name = split_address[0], split_address[1]
    except IndexError:
        print('Invalid email address!')
    else:
        print(f'Your username is {user_name}, while the domain name is {domain_name}')

EMAIL_ADDRESS_SLICER()