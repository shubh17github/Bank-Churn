from flask import Flask,render_template,request
from utils.function import bank


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('predict.html')

@app.route('/predict',methods=['GET','POST'])
def get_data():
    if request.method=='POST':
        data=request.form
        Credit_score=float(data['Credit_score'])
        Geography=int(data['Geography'])
        Gender=int(data['Gender'])
        Age=int(data['Age'])
        Tenure=int(data['Tenure'])
        Balance=float(data['Balance'])
        NumOfProducts=int(data['NumOfProducts'])
        HasCrCard=int(data['HasCrCard'])
        IsActiveMember=int(data['IsActiveMember'])
        EstimatedSalary=float(data['EstimatedSalary'])

        bank_predict_obj=bank(Credit_score,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary)
        res= bank_predict_obj.predict()

        return render_template('predict.html',pred=res)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)



        





