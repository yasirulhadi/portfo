from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_website():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
         data = request.form.to_dict()
         write_to_csv(data)
         return redirect('/thankyou.html')
        except:
            return 'database did not save'
    else:
     return 'Something went wrong. Please try again'


if __name__ == '__main__':
    app.run(debug=True)

