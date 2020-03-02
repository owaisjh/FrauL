import pandas as pd
from sklearn.externals import joblib
import warnings

warnings.filterwarnings("ignore")

def checker(body):
    
    # Load the model from the file 
    model = joblib.load('sshackmodel.pkl') 
    myvect = joblib.load('vect.pickle')
    # Use the loaded model to make predictions

    df = pd.DataFrame([body], columns=['text'])
    x_testing = df.text
    x_testing = myvect.transform(x_testing)

    prediction = model.predict(x_testing)
    
    if prediction == 1:
        return True
    else:
        return False

testing_text = 'Last chance to get $5 off your next purchase $10 or more. Just activate this offer and choose Paypal at checkout.'
print(checker(testing_text))