import streamlit as st
import pickle5 as pickle
import numpy as np


def load_model(name):
    with open(name, 'rb') as file:
        data = pickle.load(file)
    return data


def show_predict_page():
    st.title("Livestock Disease Prediction")

    st.write("""### Give some information so we can predict Livestock Disease """)

    Symptoms1 = (
        'loss of appetite', 'depression','shortness of breath',
       'painless lumps', 'chest discomfort', 'swelling in limb',
       'blisters on gums', 'swelling in extremities', 'crackling sound',
       'swelling in muscle', 'sores on gums', 'sweats',
       'difficulty walking', 'swelling in abdomen', 'fatigue', 'lameness',
       'blisters on tongue', 'blisters on hooves', 'blisters on mouth',
       'swelling in neck', 'chills', 'sores on hooves', 'sores on mouth',
       'sores on tongue'
    )

    Symptoms2 = (
        'painless lumps', 'swelling in limb', 'sweats', 'loss of appetite',
       'swelling in extremities', 'depression', 'sores on hooves',
       'crackling sound', 'swelling in muscle', 'difficulty walking',
       'lameness', 'fatigue', 'blisters on hooves', 'chills',
       'blisters on gums', 'blisters on mouth', 'swelling in abdomen',
       'chest discomfort', 'swelling in neck', 'shortness of breath',
       'sores on tongue', 'blisters on tongue', 'sores on gums',
       'sores on mouth'
    )

    Symptoms3 = (
        'blisters on tongue','loss of appetite', 'crackling sound', 'chills', 'painless lumps',
       'depression', 'shortness of breath', 'lameness',
       'difficulty walking', 'fatigue', 'swelling in extremities',
       'swelling in muscle', 'swelling in abdomen', 'chest discomfort',
       'blisters on hooves', 'blisters on mouth', 'sores on mouth',
       'swelling in limb', 'sweats', 'sores on hooves',
       'swelling in neck', 'sores on tongue', 'sores on gums',
       'blisters on gums'
    )

    livestock=(
        'goat','buffalo','sheep','cow'
    )

    animal_temperatures = {
        "goat": "Normal body temperature of a healthy goat: 101.5°F to 104°F (38.6°C to 40°C)",
        "cow": "Normal body temperature of a healthy cow: 100.4°F to 102.5°F (38°C to 39.2°C)",
        "sheep": "Normal body temperature of a healthy sheep: 101.5°F to 104°F (38.6°C to 40°C)",
        "buffalo": "Normal body temperature of a healthy buffalo: 100.4°F to 103.1°F (38°C to 39.5°C)"
    }

    livestock = st.selectbox("Select Livestock", list(animal_temperatures.keys()))
    First_Symptoms = st.selectbox("Symptoms 1", Symptoms1)
    Second_Symptoms = st.selectbox("Symptoms 2", Symptoms2)
    Third_Symptoms = st.selectbox("Symptoms 3", Symptoms3)
    #Temperature = st.slider("LiveStock body Temperature", 0, 120, 3)

    #Temperature = st.slider("Indicate Animal body Temperature", min_value=0, max_value=150)
    
    st.title("Animal Body Temperature Hint Box")

    
    Temperature = st.slider("Select a Animal Body Temperture", min_value=0, max_value=120)

    hint_text = animal_temperatures.get(livestock, "Select an animal to see its normal body temperature.")
    st.info(hint_text)

    


    age = st.slider("Age of livestock", 0, 15, 3) 
    
    prognosis_list_cow=['pneumonia', 'blackleg', 'lumpy virus', 'anthrax',
       'foot and mouth']
    prognosis_list_buffalo=['lumpy virus', 'foot and mouth', 'anthrax', 'blackleg',
       'pneumonia']
    prognosis_list_sheep= ['lumpy virus', 'pneumonia', 'blackleg', 'foot and mouth',
       'anthrax']
    prognosis_list_goat= ['foot and mouth', 'anthrax', 'lumpy virus', 'pneumonia',
       'blackleg']
    
    

    ok = st.button("Predict Disease in Livestock")

    data = load_model(f'xgmodel{livestock}.pkl')

    le_symptom1 = data["le_symptom1"]
    le_symptom2 =data["le_symptom2"]
    le_symptom3 = data["le_symptom2"]
    regressor = data["xgmodel"]
    label_encoder =data["label_encoder"]
    if ok:
        x=np.array([[age,Temperature,First_Symptoms,Second_Symptoms ,Third_Symptoms]])
        x[:, 2] = le_symptom1.transform(x[:,2])
        x[:, 3] = le_symptom2.transform(x[:,3])
        x[:, 4] = le_symptom3.transform(x[:,4])
        x = x.astype(float)

        prognosis = regressor.predict(x)
        #prognosis= label_encoder.transform(prognosis)
        if livestock=='cow':
            for i in prognosis_list_cow:
                check_prognosis=label_encoder.transform([i])
                if check_prognosis==prognosis:
                    prognosis=i
        elif livestock=='goat':
            for i in prognosis_list_goat:
                check_prognosis=label_encoder.transform([i])
                if check_prognosis==prognosis:
                    prognosis=i
        elif livestock=='buffalo':
            for i in prognosis_list_buffalo:
                check_prognosis=label_encoder.transform([i])
                if check_prognosis==prognosis:
                    prognosis=i
        else:
            for i in prognosis_list_sheep:
                check_prognosis=label_encoder.transform([i])
                if check_prognosis==prognosis:
                    prognosis=i


        st.subheader(f"The predicted prognosis for this {livestock } is {prognosis}")
