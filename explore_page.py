import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


	#Age	Temperature	Symptom 1	Symptom 2	Symptom 3	Disease


@st.cache
def load_data():
    df = pd.read_csv("animal_disease_dataset.csv")
    df = df[["Animal","Age", "Temperature", "Symptom 1", "Symptom 2", "Symptom 3"]]
    df = df.dropna()
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Disease in Livestock")

    st.write(
        """
    ### 
    """
    )

    data = df["Animal"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different Livestock categories""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Age of each Livestock
    """
    )

    data = df.groupby(["Animal"])["Age"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### 
    """
    )
    
    # ... (previous code)

    def show_additional_plots():
        st.title("Additional Plots")

        st.write(
            """
        ### Distribution of Temperatures
        """
        )
        fig, ax = plt.subplots()
        ax.hist(df["Temperature"], bins=20, edgecolor="k")
        st.pyplot(fig)

        symptom_columns = ["Symptom 1", "Symptom 2", "Symptom 3"]
        symptoms_df = df[symptom_columns]
        symptoms_counts = symptoms_df.stack().value_counts().sort_values(ascending=False)
        st.bar_chart(symptoms_counts)

        st.write(
        """
        ### Age vs Temperature
        """
        )
        fig, ax = plt.subplots()
        ax.scatter(df["Age"], df["Temperature"])
        ax.set_xlabel("Age")
        ax.set_ylabel("Temperature")
        st.pyplot(fig)

        # ... (other sections)

    # ... (remaining code)
    show_additional_plots()



    
