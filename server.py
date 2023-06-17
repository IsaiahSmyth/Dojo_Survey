from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def form():
    return render_template('index.html')


@app.route("/submit", methods=['POST'])
def submit():
    session['YourName'] = request.form['YourName']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/result_form')


@app.route("/result_form")
def result_form():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
