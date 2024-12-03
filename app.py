import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the save models

diabetes_model = pickle.load(open("diabetes_model.sav","rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav","rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav","rb"))

# Sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabeters Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                           default_index=0)
    
# Diabetes Prediction Page
if (selected == 'Diabeters Prediction'):
    
    # Page Title
    st.title('Diabetes Prediction Using Ml')
    
    # Getting The Input Data
    # Columns for input fields 
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnencies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('BloodPressure Level')
        
    with col1:
        SkinThickness = st.text_input('SkinThickness Value')
           
    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
         BMI = st.text_input('BMI Level')
         
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Level Value')

    with col2:
        Age = st.text_input('Age')

    
    # Code For Prediction
    diab_diagnosis = ''
    
    # Creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
     
    st.success(diab_diagnosis)            
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using Ml')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type (CP)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (trestbps)')
    with col2:
        chol = st.text_input('Cholesterol Level (chol)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (fbs)')
    with col1:
        restecg = st.text_input('Resting ECG Results (restecg)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    with col3:
        exang = st.text_input('Exercise Induced Angina (exang)')
    with col1:
        oldpeak = st.text_input('ST Depression (oldpeak)')
    with col2:
        slope = st.text_input('Slope of the Peak (slope)')
    with col3:
        ca = st.text_input('Number of Major Vessels (ca)')
    with col1:
        thal = st.text_input('Thalassemia (thal)')
    
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), 
                                                             float(chol), float(fbs), float(restecg), float(thalach), 
                                                             float(exang), float(oldpeak), float(slope), float(ca), float(thal)]])
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The Person has Heart Disease'
            else:
                heart_diagnosis = 'The Person does not have Heart Disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values.'
     
    st.success(heart_diagnosis)
     
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction Using ML')
    
    # Input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz) - Average Vocal Fundamental Frequency')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz) - Maximum Vocal Fundamental Frequency')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz) - Minimum Vocal Fundamental Frequency')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR - Noise-to-Harmonics Ratio')
    with col1:
        HNR = st.text_input('HNR - Harmonics-to-Noise Ratio')
    with col2:
        RPDE = st.text_input('RPDE - Recurrence Period Density Entropy')
    with col3:
        DFA = st.text_input('DFA - Detrended Fluctuation Analysis')
    with col1:
        spread1 = st.text_input('Spread 1')
    with col2:
        spread2 = st.text_input('Spread 2')
    with col3:
        D2 = st.text_input('D2 - Correlation Dimension')
    with col1:
        PPE = st.text_input('PPE - Pitch Period Entropy')
    
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    if st.button('Parkinsons Test Result'):
        try:
            parkinsons_prediction = parkinsons_model.predict([[float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), 
                                                               float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP), 
                                                               float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer), 
                                                               float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), 
                                                               float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), 
                                                               float(RPDE), float(DFA), float(spread1), float(spread2), 
                                                               float(D2), float(PPE)]])
            
            if (parkinsons_prediction[0] == 1):
                parkinsons_diagnosis = 'The Person has Parkinson\'s Disease'
            else:
                parkinsons_diagnosis = 'The Person does not have Parkinson\'s Disease'
        except ValueError:
            parkinsons_diagnosis = 'Please enter valid numeric values.'
     
    st.success(parkinsons_diagnosis)

    