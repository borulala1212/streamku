import streamlit as st

#Load ML Pkgs
import os
import joblib

# Load EDA Pkgs
import numpy as np

attrib_info = """
#### Attribute Information:
	- Pregnancies	: Number of times pregnant 
	- Glucose		: Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
	- BloodPressure	: Diastolic blood pressure (mm Hg) 
	- SkinThickness	: Triceps skin fold thickness (mm) 
	- Insulin		: 2-Hour serum insulin (mu U/ml) 
	- BMI			: Body mass index (weight in kg/(height in m)^2) 
	- DiabetesPedigreeFunction	: Diabetes pedigree function 
	- Age 			: Age (years) 
	- Outcome		: Class variable (0 or 1)

"""
# Load ML Models 
@st.cache(allow_output_mutation=True)
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def run_ml_app_diabetesNum():
	st.subheader("Machine Learning Prediction")
	#st.write("It is working")
	#st.success("it is so")

	with st.expander("Attribute Info"):
		st.markdown(attrib_info)


	# Layout
	col1, col2 = st.columns(2)

	with col1:
		Pregnancies = st.number_input("Pregnancies") 
		Glucose = st.number_input("Glucose") 
		BloodPressure = st.number_input("BloodPressure") 
		SkinThickness = st.number_input("SkinThickness") 

	with col2:
		Insulin = st.number_input("Insulin")
		BMI = st.number_input("BMI") 
		DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction") 
		Age = st.number_input("Age",10,100)  

	with st.expander("Your Selected Options"):
		result = {'Pregnancies':Pregnancies,
		'Glucose':Glucose,
		'BloodPressure':BloodPressure,
		'SkinThickness':SkinThickness,
		'Insulin':Insulin,
		'BMI':BMI,
		'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
		'Age':Age}

		st.write(result)

		encoded_result = []

		for i in result.values():
			#if type(i) == float:
			encoded_result.append(i)

		#st.write(encoded_result)

	with st.expander("Prediction result"):
		single_sample = np.array(encoded_result).reshape(1,-1)
		#st.write(single_sample)

		model = load_model("DiabetesNumeric/RandomForest_model_diabetes.pkl")
		prediction = model.predict(single_sample)
		pred_prob = model.predict_proba(single_sample)
		#st.write(prediction)
		#st.write(pred_prob)

		if prediction == 1:
			st.warning("Diabetes Disease {}".format(prediction[0]))
			pred_probanility_score = {"No Diabetes Disease":pred_prob[0][0]*100,
			"Diabetes Disease":pred_prob[0][1]*100}
			st.write(pred_probanility_score)

		else:
			st.success("No Diabetes Disease {}".format(prediction[0]))
			pred_probanility_score = {"No Diabetes Disease":pred_prob[0][0]*100,
			"Diabetes Disease":pred_prob[0][1]*100}
			st.write(pred_probanility_score)













