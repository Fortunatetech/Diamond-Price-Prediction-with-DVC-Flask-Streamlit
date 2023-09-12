from flask import Flask,request,render_template
import numpy as np
import pandas as pd

#from sklearn.preprocessing import StandardScaler
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

 
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
           carat = request.form.get("carat"),
           cut = request.form.get('cut'),
           color = request.form.get('color'),
           clarity = request.form.get('clarity'),
           depth = request.form.get('depth'),
           table = request.form.get('table'),
            x = request.form.get('x'),
            y = request.form.get('y'),
            z = request.form.get('z')
            
            )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        # Round up the result to 2 decimal places and include the US dollar symbol
        return render_template('home.html', results=f'Prediction based on your inputs is ${results[0]:.2f}')


if __name__=="__main__":
    app.run(debug= True)        
    

