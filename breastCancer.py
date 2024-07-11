import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
#import joblib
import pypickle

#Load the model
loaded_model = pypickle.load('BreastC.pkl')

#preprocessing
#create a function for the prediction taking in the data(the columns to be entered by the user)

def prediction(data):
     

#create a dataframe for the data 
     df = pd.DataFrame(data)
 #convert the row to numerical form
    
     label = LabelEncoder()
 #Create a list for the categorical columns    
     rowitems = [2,7,8,11,12]

     for i in rowitems:
         df.iloc[i] = label.fit_transform(df.iloc[i])

  #craete a variable that will convert the data to a numpy array and reshape it to a one dimensional
     num_data = df.drop([0, 9, 10, 13, 14]).values.reshape(1,-1)  
 #prediction the model
     pred = loaded_model.predict(num_data)     

     if  pred[0] == 0:
          return "The patient will not survive"
     else:
          return "The patient will survive"    
     
def main ():
     st.title("Breast Cancer Survivor Prediction Model")
     Patient_ID = st.text_input("What is your ID no: ")
     Age = st.number_input("How old are you ?: ")
     Gender = st.radio("Select Gender: ", ('Male', 'Female'))
     Protein1 = st.number_input("Please enter the level of Protein 1: ")
     Protein2 = st.number_input("Please enter the level of Protein 2: ")
     Protein3 = st.number_input("Please enter the level of Protein 3: ")
     Protein4 = st.number_input("Please enter the level of Protein 4: ")
     Tumour_Stage = st.radio("Enter your Tumor stage", ('II','III',"I"))
     Histology = st.radio("Enter the lab Histology",("Infiltrating Ductal Carcinoma","Mucinous Carcinoma","Infiltrating Lobular Carcinoma"))
     ER_status = st.radio("What is your ER status",("Positive","Negative"))
     PR_status = st.radio("What is your PR status",("Positive","Negative"))
     HER2_status = st.radio("What is your HER2 status status",("Positive","Negative"))	
     Surgery_type = st.radio("What is the surgery type",("Modified Radical Mastectomy","Lumpectomy","Simple Mastectomy","Others"))
     Date_of_Surgery = st.date_input("What date is the surgery : ")
     Date_of_Last_Visit = st.date_input("What date was your last visit : ")  

     Patient_status = ""

     if st.button("Result"):
        Patient_status = prediction([Patient_ID, Age, Gender, Protein1, Protein2, Protein3, Protein4,
        Tumour_Stage, Histology, ER_status, PR_status, HER2_status, Surgery_type, Date_of_Surgery, Date_of_Last_Visit])

        st.success(Patient_status)

if  __name__ == "__main__":
            main()

        

     

     


            

