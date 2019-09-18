from flask import Flask, render_template, request
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
      result = request.form

      mock_result = {'Mutual-Fund': 'HSBC Equity Fund', 'Insurance': 'HSBS high value Insurance'}

      return render_template('result.html',result = mock_result)

if __name__ == '__main__':
  
   app.run(debug = True)