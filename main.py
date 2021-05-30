import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import MinMaxScaler


model = pickle.load(open("heartfailuremodel.pkl","rb"))

scaler = pickle.load(open("scaler.pkl","rb"))

page_bg_img = '''
<style>
body {
background-image: url("https://th.bing.com/th/id/OIP.incp3UJuGQPhBfgn3iISAwHaEK?pid=ImgDet&rs=1");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
'''



def input_page():
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown('<p class="big-font"><b>Heart Failure Prediction</b></p>', unsafe_allow_html=True)
   
    

    gender = st.selectbox('Gender', ["Male","Female"])
    
    age = st.number_input('Age')

    highbp = st.selectbox('Do you have High Blood Pressure?', ["Yes","No"])    

    creatinine_phosphokinase = st.number_input('Creatinine Phosphokinase')

    ejection_fraction = st.number_input('Ejection Fraction')

    platelets = st.number_input('Platelets')

    serum_creatinine = st.number_input('Serum Creatinine')
    
    serum_sodium = st.number_input('Serum Sodium')

    time = st.selectbox('Time(Enter true if >75 days else enter false)',["True","False"])
    

    btn = st.button("Predict")
    
    if btn:
       
        if gender=="Male":
            sex=1
        elif gender=="Female":
            sex=0

        if highbp=="Yes":
            highbp=1
        elif highbp=="No":
            highbp=0

        if time=="True":
            time=True
        elif time == "False":
            time=False

            
        test=np.array([[age,creatinine_phosphokinase,ejection_fraction,platelets,
                        serum_creatinine,serum_sodium,time]])
        test = scaler.fit_transform(test)
        result = model.predict(test)[0]
        if result==0:
            st.markdown('<p class="success_class"><b>The patient survives.</b></p>', unsafe_allow_html=True)

        if result==1:
            st.markdown('<p class="error_class"><b>The patient dies.</b></p>', unsafe_allow_html=True)

        

    
    
input_page() 
