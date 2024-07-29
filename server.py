from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

print(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_contact', methods=['POST', 'GET'])
def submit_contact():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            error = 'Failed to save to database'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('contact.html', error=error)


def write_to_file(data):
    with open("database.txt", "a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open("database.csv", "a") as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']

        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(
            {'email': email, 'subject': subject, 'message': message})

        # csv_writer = csv.writer(csvfile, delimiter=',',
        #                         quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # csv_writer.writerow(email, subject, message)
