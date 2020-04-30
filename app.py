from flask import Flask, render_template , request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Gokul/.vscode/Donation Website/templates/post.db'
db = SQLAlchemy(app)

class Donate(db.Model):
    Fname = db.Column(db.String(10), nullable=False)
    Lname = db.Column(db.String(10), nullable=False)
    Email = db.Column(db.String(20), nullable=False)
    Contact = db.Column(db.Integer, primary_key=True)
    Amount = db.Column(db.Integer, nullable=False)

  
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post_Fname = request.form['Fname'] 
        post_Lname = request.form['Lname'] 
        post_Email = request.form['Email'] 
        post_Contact = request.form['Contact'] 
        post_Amount = request.form['Amount']
        new_post = Donate(Fname=post_Fname,Lname=post_Lname,Email=post_Email,Contact=post_Contact,Amount=post_Amount)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    else:  
        return render_template("index.html")

@app.route("/Support")
def Support():
    return render_template("Support.html")

    
if(__name__=='__main__'):
    app.run(debug=True)
