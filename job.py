# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__,template_folder='C:/Users/smizk/Documents/data science notes/Data analyst Job Prediction')


@app.route('/',methods=['GET'])
def Home():
                                  return render_template('job1.html')
                                    


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
                                        from ipynb.fs.defs.job import Prediction
                                        if request.method == 'POST':
                                                    
                                                    Size=str(request.form['Number of Employees'])
                                                    # nested if to convert string to numeric.
                                                    if Size ==  '501 to 1000 employees':
                                                                    s = 5
                                                    elif Size == '201 to 500 employees':
                                                                    s = 3
                                                    elif Size == '5001 to 10000 employees':
                                                                    s = 4
                                                    elif Size == '10000+ employees':
                                                                    s = 1
                                                    elif Size == '51 to 200 employees':
                                                                    s = 6
                                                    elif Size == '1001 to 5000 employees':
                                                                    s = 2
                                                    else:
                                                                    s = 0
                                                                
                                                 
                                                    
                                                    Type=str(request.form['Type of Ownership'])
                                                     # nested if to convert string to numeric.
                                                    if Type ==  'Company - Private':
                                                                    t = 0
                                                    elif Type == 'Company - Public':
                                                                    t = 1
                                                    elif Type == 'Hospital':
                                                                    t = 2
                                                    elif Type == 'Nonprofit Organization':
                                                                    t = 3
                                                    elif Type == 'Subsidiary or Business Segment':
                                                                    t = 5
                                                    else:
                                                                    t = 4
                                                                    
                                                    Sector =str(request.form['Sector'])
                                                     # nested if to convert string to numeric.
                                                    if Sector ==  'Arts, Entertainment & Recreation':
                                                                    s1 =  2
                                                    elif Sector == 'Insurance':
                                                                    s1 =  11
                                                    elif Sector == 'Finance':
                                                                    s1 =  7
                                                    elif Sector == 'Health Care':
                                                                    s1 =  9
                                                    elif Sector == 'Business Services':
                                                                    s1 =  4
                                                    elif Sector == 'Information Technology':
                                                                    s1 =  10
                                                    elif Sector == 'Media':
                                                                    s1 =  13
                                                    elif Sector == 'Biotech & Pharmaceuticals':
                                                                    s1 =  3
                                                    elif Sector == 'Oil, Gas, Energy & Utilities':
                                                                    s1 =  15
                                                    elif Sector == 'Aerospace & Defense':
                                                                    s1 =  1
                                                    elif Sector == 'Non-Profit':
                                                                    s1 =  14
                                                    elif Sector == 'Manufacturing':
                                                                    s1 =  12
                                                    elif Sector == 'Government':
                                                                    s1 =  8
                                                    elif Sector == 'Construction, Repair & Maintenance':
                                                                    s1 =  5
                                                    elif Sector == 'Retail':
                                                                    s1 =  16
                                                    elif Sector == 'Transportation & Logistics':
                                                                    s1 =  18
                                                    elif Sector == 'Accounting & Legal':
                                                                    s1 =  0
                                                    elif Sector == 'Telecommunications':
                                                                    s1 =  17
                                                    else:
                                                                    s1 =  6
                                                                    
                                                    Revenue =str(request.form['Revenue'])
                                                     # nested if to convert string to numeric.
                                                    if Revenue ==  '$100 to $500 million (USD)':
                                                                    r = 3
                                                    elif Revenue == '$1 to $2 billion (USD)':
                                                                    r = 0
                                                    elif Revenue == '$5 to $10 billion (USD)':
                                                                    r = 6
                                                    elif Revenue == '$25 to $50 million (USD)':
                                                                    r = 5
                                                    elif Revenue == '$10+ billion (USD)':
                                                                    r = 2
                                                    elif Revenue == '$2 to $5 billion (USD)':
                                                                    r = 4
                                                    elif Revenue == '$500 million to $1 billion (USD)':
                                                                    r = 9
                                                    elif Revenue == '$50 to $100 million (USD)':
                                                                    r = 8
                                                    elif Revenue == '$10 to $25 million (USD)':
                                                                    r = 1
                                                    elif Revenue == '$5 to $10 million (USD)':
                                                                    r = 7                                    
                                                    else:
                                                                    r = 10
                                                    Rating = float(request.form['Rating (1.0 - 5.0)'])
                                                    prediction= Prediction(s,t,s1,r,Rating,Size,Type,Sector,Revenue)               
                                                    result = prediction.empty
                                                    if result == False:
                                                                        return render_template('job1.html',output= [prediction.to_html(index=False,justify='center')],header=True)
                                                    else:
                                                                        return render_template('job1.html',out='No jobs found for this criteria.')
        
       

if __name__=="__main__":
    app.run(debug=True)