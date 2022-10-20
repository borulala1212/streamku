# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc

# Import mini apps
from eda_app_diabetesNum import run_eda_app_diabetesNum
from ml_app_diabetesNum import run_ml_app_diabetesNum

from eda_app_liver import run_eda_app_liver
from ml_app_liver import run_ml_app_liver

from eda_app_BC import run_eda_app_BC
from ml_app_BC import run_ml_app_BC

from eda_app_HD import run_eda_app_HD
from ml_app_HD import run_ml_app_HD

html_temp = """
        <div style="background-color:#3872fb;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Early Stage Disease Risk Data App </h1>
        <h4 style="color:white;text-align:center;">Cronic Disease</h4>
        </div>
        """
desc_temp = """
            ### Early Stage Disease Predictor App
            This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
            #### Datasource
                - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
            #### App Content
                - EDA Section: Exploratory Data Analysis of Data
                - ML Section: ML Predictor App

            """

def main():
    #st.title("Main App")
    stc.html(html_temp)

    menu = ["Home","Disease","About"]
    choice = st.sidebar.selectbox('Menu',menu)


    if choice == "Home":
        st.subheader("Home")
        ##st.write(desc_temp)
        #st.markdown(desc_temp,unsafe_allow_html=True)


    elif choice == "Disease":
        menu1 = ["Diabetes Disease","Liver Disease","Breast Cancer Disease","Heart Disease","Disease 5"]
        choice1 = st.sidebar.selectbox('Pilihan',menu1)

        ## DIABETES DISEASE

        desc_temp_diabetes = """
            ### Early Stage Diabetes Disease Predictor App
            Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.
            #### Datasource
                - https://www.kaggle.com/datasets/mathchi/diabetes-data-set
            #### App Content
                - EDA Section: Exploratory Data Analysis of Data
                - ML Section: ML Predictor App

            """

        desc_temp_liver = """
            ### Early Stage Liver Disease Predictor App
            This data set contains 416 liver patient records and 167 non liver patient records.The data set was collected from north east of Andhra Pradesh, India. Selector is a class label used to divide into groups(liver patient or not). This data set contains 441 male patient records and 142 female patient records. 
            #### Datasource
                - https://archive.ics.uci.edu/ml/datasets/ILPD+(Indian+Liver+Patient+Dataset)
            #### App Content
                - EDA Section: Exploratory Data Analysis of Data
                - ML Section: ML Predictor App

            """

        desc_temp_BC = """
            ### Early Stage Breast Cancer Disease Predictor App
            Original Wisconsin Breast Cancer Database
            #### Datasource
                https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29
            #### App Content
                - EDA Section: Exploratory Data Analysis of Data
                - ML Section: ML Predictor App

            """

        desc_temp_HD = """
            ### Early Stage Heart Disease Predictor App
                Heart Disease Dataset
            #### Datasource
                https://github.com/ammarmahmood1999/HeartHealthPrediction/blob/master/heart.csv
            #### App Content
                - EDA Section: Exploratory Data Analysis of Data
                - ML Section: ML Predictor App

            """

        if choice1 == "Diabetes Disease":
            
            DD = ["Home","EDA","ML","About"]
            choice11 = st.sidebar.selectbox('Diabetes Disease',DD)

            if choice11 == "Home":
                st.subheader("Home")
                st.markdown(desc_temp_diabetes,unsafe_allow_html=True)

            elif choice11 == "EDA":
                run_eda_app_diabetesNum()
            elif choice11 == "ML":
                run_ml_app_diabetesNum()
            else:
                st.subheader("About")



        ## LIVER DISEASE
        elif choice1 == "Liver Disease":
            DD = ["Home","EDA","ML","About"]
            choice11 = st.sidebar.selectbox('Liver Disease',DD)

            if choice11 == "Home":
                st.subheader("Home")
                st.markdown(desc_temp_liver,unsafe_allow_html=True)

            elif choice11 == "EDA":
                run_eda_app_liver()
            elif choice11 == "ML":
                run_ml_app_liver()
            else:
                st.subheader("About")

        elif choice1 == "Breast Cancer Disease":

            DD = ["Home","EDA","ML","About"]
            choice11 = st.sidebar.selectbox('Breast Cancer Disease',DD)

            if choice11 == "Home":
                st.subheader("Home")
                st.markdown(desc_temp_BC,unsafe_allow_html=True)

            elif choice11 == "EDA":
                run_eda_app_BC()
            elif choice11 == "ML":
                run_ml_app_BC()
            else:
                st.subheader("About")


        elif choice1 == "Heart Disease":

            DD = ["Home","EDA","ML","About"]
            choice11 = st.sidebar.selectbox('Heart Disease',DD)

            if choice11 == "Home":
                st.subheader("Home")
                st.markdown(desc_temp_HD,unsafe_allow_html=True)

            elif choice11 == "EDA":
                run_eda_app_HD()
            elif choice11 == "ML":
                run_ml_app_HD()
            else:
                st.subheader("About")


        elif choice1 == "Disease 5":
            pass

if __name__ == '__main__':
    main()

