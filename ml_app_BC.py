import streamlit as st

#Load ML Pkgs
import os
import joblib

# Load EDA Pkgs
import numpy as np

attrib_info = """
### Attribute Information:
	- Clump Thickness: 1 - 10 
	- Uniformity of Cell Size: 1 - 10 
	- Uniformity of Cell Shape: 1 - 10 
	- Marginal Adhesion: 1 - 10 
	- Single Epithelial Cell Size: 1 - 10 
	- Bare Nuclei: 1 - 10 
	- Bland Chromatin: 1 - 10 
	- Normal Nucleoli: 1 - 10 
	- Mitoses: 1 - 10 
	- Class: (0 for benign, 1 for malignant)

"""
#
target_label_map = {"Malignant":1,"Benign":0}

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value



## Load ML Models 
@st.cache(allow_output_mutation=True)
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def run_ml_app_BC():
	st.subheader("Machine Learning Liver Prediction")
#	st.write("It is working")
#	st.success("it is so cool")

	with st.expander("Attribute Info"):
		st.markdown(attrib_info)


	# Layout
	col1, col2 = st.columns(2)

	with col1:
		clump_thickness = st.number_input("Clump Thickness")
		#gender = st.selectbox("Gender",("Female","Male"))
		UC_size = st.number_input("Uniformity of Cell Size")
		UC_shape = st.number_input("Uniformity of Cell Shape") 
		MA = st.number_input("Marginal Adhesion")
		SEC_size = st.number_input("Single Epithelial Cell Size") 
		
	with col2:
		BN = st.number_input("Bare Nuclei") 
		BC = st.number_input("Bland Chromatin") 
		NN = st.number_input("Normal Nucleoli")
		Mitoses = st.number_input("Mitoses") 

	with st.expander("Your Selected Options"):
		result = {'Clump Thickness':clump_thickness,
		'Uniformity of Cell Size':UC_size ,
		'Uniformity of Cell Shape':UC_shape,
		'Marginal Adhesion':MA,
		'Single Epithelial Cell Size':SEC_size,
		'Bare Nuclei':BN,
		'Bland Chromatin':BC,
		'Normal Nucleoli':NN,
		'Mitoses':Mitoses}
		st.write(result)


		encoded_result = []
		for i in result.values():
			encoded_result.append(i)


	with st.expander("Prediction result"):
		single_sample = np.array(encoded_result).reshape(1,-1)
#		st.write(single_sample)

		model = load_model("BreastCancerWiscosin/RandomForest_model_BreastCancer.pkl")
		prediction = model.predict(single_sample)
		pred_prob = model.predict_proba(single_sample)
		#st.write(prediction)
		#st.write(pred_prob)

		if prediction == 1:
			st.warning("Malignant Breast Cancer".format(prediction[0]))
			pred_probanility_score = {"Benign Breast Cancer":pred_prob[0][0]*100,
			"Malignant Breast Cancer":pred_prob[0][1]*100}
			st.write(pred_probanility_score)

		else:
			st.success("Benign Breast Cancer".format(prediction[0]))
			pred_probanility_score = {"Benign Breast Cancer":pred_prob[0][0]*100,
			"Malignant Breast Cancer":pred_prob[0][1]*100}
			st.write(pred_probanility_score)













