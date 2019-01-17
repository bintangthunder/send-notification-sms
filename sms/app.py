import nexmo
from flask import Flask, flash, redirect, render_template, request, url_for

from util import extract_error

app = Flask(__name__)

#@app.route('/')
#def hello():
#    return "Hello World!"

# Load in configuration from environment variables:
NEXMO_API_KEY = "d489436c"
NEXMO_API_SECRET = "O4SfU8PEkqAWoC59"
NEXMO_NUMBER = "6281262000095"

# Create a new Nexmo Client object:
nexmo_client = nexmo.Client(
    key = NEXMO_API_KEY,
    secret = NEXMO_API_SECRET
)

app = Flask(__name__)
app.config['SECRET_KEY'] = "asasdasfasdf235424efg43terg"

@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('test.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """ A POST endpoint that sends an SMS. """

    # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']

    # Send the SMS message:
    result = nexmo_client.send_message({
        'from': NEXMO_NUMBER,
        'to': to_number,
        'text': message,
    })

    # Set a message for the user to see on the next view:
    err = extract_error(result)
    if err is not None:
        flash("There was a problem sending your message: " + err, 'error')
    else:
        flash("You just sent a message to " + to_number)

    # Redirect the user back to the form:
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()