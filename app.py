from flask import Flask,render_template,url_for
app=Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html',title='Home')

@app.route('/students')
def students():
    return render_template('students.html',students='Students')


if __name__=="__main__":
    app.run(debug=True )
