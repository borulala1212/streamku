import streamlit as st

#Load data Eda Pkgs
import pandas as pd
import numpy as np

#load data viz pkg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

#Load data 
@st.cache

def load_data(HeartDisease):
	df = pd.read_csv(HeartDisease)
	return df

def run_eda_app_HD():
	st.subheader("Exploratory Data Analysis")
	#df = pd.read_csv("ILPD/Indian_Liver_Patient_Dataset_(ILPD).csv")

	df = load_data("HeartDisease/heart_disease_data.csv")

#	df_encoded = load_data("HeartDisease/heart_disease_data.csv")
	freq_df = load_data("HeartDisease/freq_HD.csv")

	submenu = st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		st.dataframe(df)

#	#	with st.expander("Data Types"): ##???
#	#		st.dataframe(df.dtypes)

		with st.expander("Descriptive Summary"):
			st.dataframe(df.describe())

		with st.expander("Class Distribution"):
			st.dataframe(df['target'].value_counts())

		with st.expander("Gender Distribution"):
			st.dataframe(df['sex'].value_counts())


	elif submenu == "Plots":
		st.subheader("Plots")

		#layouts
		col1,col2 = st.columns([2,1])

		with col1:
			#Gender Distribution
			with st.expander("Dist Plot of Gender"):
				fig = plt.figure()
				sns.countplot(df['sex'])
				st.pyplot(fig)
				st.write("0 for Female; 1 for Male")

				gen_df = df['sex'].value_counts().to_frame()
		#		st.dataframe(gen_df)
		#		gen_df = gen_df.reset_index()
		#		gen_df.columns = ["Gender type","Counts"]
		#		#st.dataframe(gen_df)

		#		pl = px.pie(gen_df,)  #????
		#		st.plotly_chart(pl)

			#For Class Distribution
			with st.expander("Dist Plot of Target"):
				fig = plt.figure()
				sns.countplot(df['target'])
				st.pyplot(fig)


		with col2: 
			with st.expander("Gender Distribution"):
				st.dataframe(gen_df)

			with st.expander("Target Distribution"):
				st.dataframe(df['target'].value_counts())

#		#Freq Dist 
		with st.expander("Frequency Distribution of Age"):
			st.dataframe(freq_df)
			
			#p2 = px.bar(freq_df,x='Age',y='count')
			#st.plotly_chart(p2)

		# Outlier Detection 
		with st.expander("Outlier Detection Plot of Age"):
			fig = plt.figure()
			sns.boxplot(df['age'])
			st.pyplot(fig)
#
#			p3 = px.box(df,x='Age',color='Gender')
#			st.plotly_chart(p3)
#
#		# Correlation 
		with st.expander("Correlation Plot"):
			corr_matrix = df.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

#			p4 = px.imshow(corr_matrix)
#			st.plotly_chart(p4)






























