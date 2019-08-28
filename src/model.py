import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

def predict_model(experience):
	model = pickle.load(open('models/lr.model', 'rb'))
	result = model.predict([[float(experience)]])
	
	return result