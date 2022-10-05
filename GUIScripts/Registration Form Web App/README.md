## Overview:
With the help of the PyWebIO module, we'll create a registration form. This Python library is mostly used to build simple, interactive web interfaces locally. Username, name, password, email, and website link information will be entered into this form. In relation to passwords, it will also double-check your password to see whether it is accurate. Your phone number, website URL, and email address will also be verified.

## Form Elements
* input_group: Used to get the inputs in the group.
* input: Used to take all kinds of inputs from the user.
* type: This depends on user choice whether the user wants a number in the input or a text in the input.
* required: If required is true, that means you have to input something, we can’t leave blank.
* validate: Receives input as a parameter, when the input value is valid, it returns True.
* cancelable: Whether the form can be canceled. Default is False.
* PlaceHolder: This element is used only in the input_group function.
* radio: Only a single can be selected.
* select: You can also select multiple options by setting the “multiple” parameter to True.

## Working
This form will take your username, name, password, email, and website link as input. Speaking of passwords, it will also check your password again to confirm whether it is correct or not. It will also validate your phone number, website link, and email address. 

After that, you will get the radio button consisting of gender, and you will also get the comment section so that you can write your feedback. As you can see in the below image, first we have to pass the username, then we will pass the password, and then to check whether the password is correct or not, we will confirm it by reentering the new password. The name, phone number, and phone number will then be verified to see if they are valid.

When we pass the email, it will be verified using the re-module. Finally, pass the website link, so that we can access that site. And when we press the reset button, the whole content will refresh. When we press the submit button, it will be submitted and will show you the whole content.

## Output:
<img width=50% src="../Registration Form Web App/Images/form.jpg">
