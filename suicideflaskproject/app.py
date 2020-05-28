from flask import Flask,request, url_for, redirect, render_template
import pickle
import db
import numpy as np
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login',methods=['POST','GET'])
def login():
    login_details=[i for i in request.form.values()]
    if(len(login_details)!=0):
        email=login_details[0]
        pwd1=login_details[1]
        doc=list(db.db.collection.find({"email":email}))
        print(doc)
        lst=doc[0]
        if(pwd1==lst['pwd']):
            print("success")
            return render_template("suicidepred.html",name=lst['name'],id=lst['_id'])
    return render_template("login.html")

#------------------------------------------------------------------


#------------------------------------------------------------------
@app.route('/register',methods=['POST','GET'])
def register():
    details=[ i for i in request.form.values()]
    if(len(details)>=1):
        print(len(details),details[6],details[7])
        if(details[6]==details[7] and len(details[6])>8 and len(details[2])==10):
            db.db.collection.insert_one({
                "name": details[0],
                "email":details[1],
                "phno":details[2],
                "gender":details[3],
                "age":details[4],
                "place":details[5],
                "pwd":details[6]
            })

            return render_template("login.html")
    return render_template("Registration.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    all_features=[x for x in request.form.values()]
    int_features=[]
    if(len(all_features)!=0):
        int_features=[float(all_features[i]) for i in range(5)]
    else:
        return render_template('suicidepred.html')
    print(all_features)
    if(len(int_features)!=0):
        final=[np.array(int_features)]
        print(int_features)
        print(final)
        prediction=model.predict(final)
        print(prediction)
        db.db1.chemicals.insert_one({
            "id": all_features[5],
            "name": all_features[6],
            "serotonin": all_features[0],
            "dopamine": all_features[1],
            "glutamate": all_features[2],
            "cotisol": all_features[3],
            "five-hiaa": all_features[4],
            "suicide_percentage":prediction[0][0]
        })
        status=''
        prob=prediction[0][0]
        reasons='Drugs,Alcohal,Smoking,Depression,Stress'
        sides='Insomnia,Adrinalin Malfunctionality,Hyper activity,Short Temper,High Blood Pressure'
        classes=''
        ms='High!!! Need to consult a pshyciatrist as soon as possible'
        if prob>=70:
            status='Very Poor'
            classes='A'
        elif prob<70 and prob>30:
            status='Okay,but still need a check'
            classes='B'
        else:
            status="Healthy and Fine"
            classes='c'
        return render_template('suicidepred.html', prob=str(prob),status=str(status),classes=str(classes),reasons=reasons,sides=sides,ms=ms)
    return render_template('suicidepred.html')

if __name__ == '__main__':
    app.run(debug=True)
