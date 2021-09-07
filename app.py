#importing the libraries
import pickle
import numpy
from flask import Flask, request, render_template

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('car_price.pkl', 'rb'))

#User defined Functions
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/prediction', methods= ['POST'])
def predict():
    Max_Power = int(request.form['Max_Power'])
    Torque = int(request.form['Torque'])
    Engine = int(request.form['Engine'])   #name shoul match with html page
    year = int(request.form['year'])

    prediction = loadedModel.predict([[Max_Power, Torque, Engine, year]])
    prediction    
    
    return render_template('index.html', Predictd_Price=prediction)

#main function
if __name__ == "__main__":
    app.run(debug = True)
