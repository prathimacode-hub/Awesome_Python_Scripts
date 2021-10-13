from flask import Flask, request, render_template
app = Flask(__name__)
import sys
from io import StringIO

@app.route('/', methods=['GET', 'POST']) # Create a route at the root page that accepts get and post requests
def input():
    if(request.method == "POST"): # Check if request is a post request (If the person has submitted something through the form)
        try:
            inp=str(request.form.get('inp')).split("; ") # Get form input and split it up if multiple commands are entered
            response = ""
            for x in inp: # Loop through all commands
                old_stdout = sys.stdout
                sys.stdout = mystdout = StringIO() # This is to start recording of output in the console
                eval(x) # Evaluate expression
                sys.stdout = old_stdout # End recording of output
                response+=mystdout.getvalue() + "<br>" # Save output and add <br> tag to make a new line so the output is seperated
            return "Response: <br>" + response # Return the response to show on website
        except Exception as e:
            return "Error: " + str(e) # Show if any errors happend
    else:
        return render_template("input.html") # Render website template in the templates folder

if __name__ == '__main__':
    app.run()