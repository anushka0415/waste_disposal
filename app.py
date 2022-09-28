from email.policy import default
from tokenize import Name
from flask import Flask,request, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///waste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 
db = SQLAlchemy(app)

class Waste(db.Model):
    sno= db.Column(db.Integer,primary_key =True)
    firstname= db.Column(db.String(200),nullable= False)
    lastname= db.Column(db.String(200),nullable= False)
    city= db.Column(db.String(200),nullable=False)
    date= db.Column(db.String(20),nullable=False)
    time= db.Column(db.String(20),nullable=False)
    zip= db.Column(db.Integer,nullable=False)
    address= db.Column(db.String(200),nullable=False)
    email= db.Column(db.String(200),nullable=False)
    waste_type= db.Column(db.String(200),nullable=False)
    quantity= db.Column(db.Integer,nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.firstname}"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule2',methods=['GET','POST'])
def schedule2():
    if request.method=='POST':
        firstname = request.form['firstname']       
        lastname = request.form['lastname']
        city = request.form['city']
        zip = request.form['zip']
        address = request.form['address']
        time = request.form['time']
        date = request.form['date']
        email= request.form['email']
        waste_type = request.form['waste_type']
        quantity = request.form['quantity']
        waste = Waste(firstname=firstname,lastname=lastname,city=city,zip=zip,address=address,time=time,date=date,email=email,waste_type=waste_type,quantity=quantity)
        db.session.add(waste)
        db.session.commit()
        allWaste = Waste.query.all()
        print(allWaste)
    return render_template('schedule2.html')

@app.route('/collection_request')
def collection_requests():
    allWaste= Waste.query.all()
    return render_template('collection_request.html',allWaste=allWaste)


if __name__=="__main__":
    app.run(debug=True)