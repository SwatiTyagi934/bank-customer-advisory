from flask import Flask, render_template, request
from modelfunctions import applyall
import pandas as pd
import pickle
from product import getProductSuggestion
app = Flask(__name__)

@app.route('/new_customer')
def new_customer():
   return render_template('new_customer.html')

@app.route('/existing_customer')
def existing_customer():
   return render_template('existing_customer.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      val=request.form.to_dict()
      data = {'age' : int(val['Age']), 'job' : 'blue', 'marital' : val['Marital Status'],'education':val['Education'],'default':val['Default'],'balance':int(val['Account Balance']),'housing':val['Housing Loan'],'loan':'no'}
      df=pd.DataFrame(data, index=[0])
      df=applyall(df)
      filename = 'finalized_model.sav'
      loaded_model = pickle.load(open(filename, 'rb'))
      ans=loaded_model.predict(df)
      print(getProductSuggestion(data['age'],data['balance'],ans[0]))
      mock_result = {'Mutual-Fund': 'HSBC Equity Fund', 'Insurance': 'HSBS high value Insurance'}

      return render_template('result.html',result = mock_result)

if __name__ == '__main__':
  
   app.run(debug = True)