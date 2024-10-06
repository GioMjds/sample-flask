from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    fullname = f"{firstname} {lastname}"
    student_id = request.form['student_id']
    course = request.form['course']
    block = request.form['block']
    subject = request.form['subject']
    return render_template('user.html', fullname=fullname, student_id=student_id, course=course, block=block, subject=subject)

if __name__ == "__main__":
    app.run(debug=True)