import streamlit as st
import pickle
import numpy as np


def load_model(name):
    with open(name, 'rb') as file:
        data = pickle.load(file)
    return data


def show_predict_page():
    st.title("Livestock Disease Diagnosis")

    st.write("""### Give some information so we can predict Livestock Disease""")

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

    
    Temperature = st.slider("Select a Animal Body Temperture (°F)", min_value=100, max_value=105)

    hint_text = animal_temperatures.get(livestock, "Select an animal to see its normal body temperature.")
    st.info(hint_text)

    prescription={"Goat_anthrax":"Isolate and mark the affected goat.Disinfect the area thoroughly and avoid handling the goat or its body.Contact a veterinarian and report the suspected case to local authorities, as anthrax is a zoonotic disease that can affect humans too.",
"Goat_blackleg":"Isolate the affected goat to prevent further spread. This disease kills within 12- 48 hours of infection Contact your veterinarian immediately.",
"Goat_pneumonia":"Isolate the affected goat and monitor its breathing. Provide a clean and dry environment with proper ventilation to keep the sheep warm and dry.Feed the goat with balanced diet that provides enough calories to maintain body temperature.",
"Goat_lumpy virus":"Isolate the infected goat to prevent the spread of the virus. Clean the area around the wound with mild soap and water. Maintain good hygiene and disinfect the environment to reduce the risk of transmission.",
"Goat_foot and mouth":"Isolate the infected goat to prevent disease spread. Clean the area around the blister with mild soap and water. Check the blister regularly for signs of infection such as redness or discharge.",


"Buffalo_anthrax":"Isolate and mark the affected buffalo. Disinfect the area thoroughly and avoid handling the buffalo or its body. Contact a veterinarian and report the suspected case to local authorities, as anthrax is a zoonotic disease that can affect humans too.",
"Buffalo_blackleg":"Isolate the affected buffalo to prevent further spread. Contact a veterinarian immediately for support as diseases kill within 48 hours.",
"Buffalo_pneumonia":"Isolate the affected buffalo and monitor its breathing. Provide a clean and dry environment with proper ventilation to keep the sheep warm and dry. Provide supportive care like fluid therapy and antibiotics.",
"Buffalo_lumpy virus":"Isolate the buffalo to prevent the spread of the virus. Clean the area around the wound with mild soap and water. Maintain good hygiene and disinfect the environment to reduce the risk of transmission.",
"Buffalo_foot and mouth":"Isolate the infected buffalo to prevent disease spread. Clean the area around the blister with mild soap and water. Treat the blister by regularly dressing.",

"Cow_anthrax":"Isolate and mark the affected cow. Disinfect the area thoroughly and avoid handling the cow or its body. Contact a veterinarian and report the suspected case to local authorities, as anthrax is zoonotic disease that can affect humans too.",
"Cow_blackleg":"Isolate the affected cow to prevent spreading the disease. Contact a veterinarian immediately for support as diseases kill within 48 hours.",
"Cow_pneumonia":"Isolate the affected cow to prevent disease spread to other animals. Provide a well-ventilated, dry, and comfortable environment. Keep the animal warm and ensure access to clean water and food.",
"Cow_lumpy virus":"Isolate the affected cow to prevent disease spread. Clean the area around the wound with mild soap and water. Practice strict biosecurity measures, including disinfection of equipment and personnel.",
"Cow_foot and mouth":"Isolate the affected cow to avoid disease spread. Clean the area around the blister with mild soap and water. Check the blister regularly for signs of infection such as redness or discharge. ",

"Sheep_anthrax":"Isolate and mark the affected cow. Disinfect the area thoroughly and avoid handling the cow or its body. Contact a veterinarian and report the suspected case to local authorities, as anthrax is zoonotic disease that can affect humans too.",
"Sheep_blackleg":"Isolate the affected sheep to prevent further spread. This disease kills within 12- 48 hours of infection Contact your veterinarian immediately.",
"Sheep_pneumonia":"Isolate the affected sheep and monitor its breathing. Provide a clean and dry environment with proper ventilation to keep the sheep warm and dry. Provide supportive care like fluid therapy and antibiotics.",
"Sheep_lumpy virus":"Isolate the infected sheep to prevent the spread of the virus. Clean the area around the wound with mild soap and water. Maintain good hygiene and disinfect the environment to reduce the risk of transmission.",
"Sheep_foot and mouth":"Isolate the infected sheep to prevent disease spread. Clean the area around the blister with mild soap and water.  Apply wound healing cream on blister surface. "

}


    age = st.slider("Age of livestock (Years)", 0, 15, 3) 
    
    prognosis_list_cow=['pneumonia', 'blackleg', 'lumpy virus', 'anthrax',
       'foot and mouth']
    prognosis_list_buffalo=['lumpy virus', 'foot and mouth', 'anthrax', 'blackleg',
       'pneumonia']
    prognosis_list_sheep= ['lumpy virus', 'pneumonia', 'blackleg', 'foot and mouth',
       'anthrax']
    prognosis_list_goat= ['foot and mouth', 'anthrax', 'lumpy virus', 'pneumonia',
       'blackleg']
    
    data = load_model(f'xgmodel{livestock}.pkl')

    le_symptom1 = data["le_symptom1"]
    le_symptom2 =data["le_symptom2"]
    le_symptom3 = data["le_symptom3"]
    regressor = data["xgmodel"]
    label_encoder =data["label_encoder"]

    ok = st.button("Predict Disease in Livestock")
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
        key=f"{livestock}_{prognosis}"
        
        st.subheader(f"RECOMMENDATION: {prescription[key] } ")
