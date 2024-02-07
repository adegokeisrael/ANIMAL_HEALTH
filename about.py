import streamlit as st
import streamlit.components.v1 as components

# Function to style text
def style_text(text, style="bold", size=0, color=None):
    if style == "bold":
        text = f"**{text}**"
    elif style == "italic":
        text = f"*{text}*"

    if size > 0:
        text = f"<span style='font-size:{size}px'>{text}</span>"

    if color:
        text = f"<span style='color:{color}'>{text}</span>"

    return text

# Function to display header
def display_header(text, level=2):
    header = style_text(text, style="bold", size=36)
    st.markdown(f"<h{level}>{header}</h{level}>", unsafe_allow_html=True)

# Function to display image with caption
def display_image_with_caption(image_path, caption, width):
    st.image(image_path, caption=caption, width=width)

# Function to display about section
def display_about_section():
    st.write(style_text("**Name:** Ayinde Jubril Adekunle"))
    st.write(style_text("**Level of Education:** Electrical and Electronic Engineering Department"))

def show_about_page():
    st.title("About Me")

    display_image_with_caption("Aiphoto_1692112831938.jpg", "My Passport Photo", 150)
    display_about_section()

# ... (remaining code)

    def show_about_app_page():
        st.title("About the App")

        st.write(
            """
            ### Application Architecture
            This app is built using the Streamlit framework, which allows for diverse creation of web-based data visualizations and interfaces. It utilizes Python to process and visualize data.

            ### Algorithms Used
            XGBoost (eXtreme Gradient Boosting) is a popular machine learning algorithm that belongs to the gradient boosting family. It's widely used for both classification and regression tasks. XGBoost is known for its high performance, scalability, and effectiveness in dealing with complex datasets. You can integrate XGBoost into your Streamlit app to enhance its analytical capabilities. Here's an overview of XGBoost and how you might use it in your app:

            **What is XGBoost?**
            XGBoost is an ensemble learning algorithm that combines the power of multiple weak models (typically decision trees) to create a strong predictive model. It employs a boosting technique, which iteratively builds new models that focus on the errors made by the previous models. The predictions of all these models are combined to produce the final prediction.

            The Livestock Disease Prediction App represents a pivotal convergence of advanced computational methodologies and streamlined user interface design. At its core, this application leverages the formidable capabilities of the XGBoost algorithm to prognosticate diseases within the bovine, ovine, caprine, and bubaline domains. These livestock categories are characterized by unique health intricacies, thereby necessitating a predictive framework that accommodates both the specificity and heterogeneity of the datasets.

            Functioning as a predictive juggernaut, the XGBoost model is engendered through an intricate web of training data and iterative enhancement mechanisms. Comprehending intricate correlations between three principal symptoms, age, and the species of livestock, the model rapidly synthesizes a predictive landscape founded upon its encyclopedic repository of diagnostic insights. This holistic predictive ethos, while mathematically intricate, culminates in an application that epitomizes user-centricity.

            On the outward-facing spectrum, the app's user interface exudes the elegance of Streamlit, a comprehensive package that transcends mere presentation. The interface, meticulously architected, metamorphoses data input into actionable insights. Intuitively designed elements guide users to input symptomatology and demographic specifics. This input seamlessly interfaces with the XGBoost model's underlying infrastructure, precipitating informed diagnostic conjectures within moments.

            In sum, the Livestock Disease Prediction App signifies the zenith of data-driven and user-centric design paradigms. Harmonizing the prowess of the XGBoost algorithm with the artistry of Streamlit, it forges an indelible bridge between advanced computational science and approachable application. In doing so, it empowers livestock custodians with an avant-garde toolset for preemptive health management, engendering a paradigm shift in disease mitigation strategies.

            The app employs various algorithms for data processing and visualization. These include algorithms for generating charts, aggregating data, and creating meaningful insights from the provided dataset.

            This app aims to provide an interactive platform for exploring disease data in livestock. It loads data from a CSV file, processes it to create informative visualizations, and allows users to gain insights into livestock disease patterns. Users can explore distributions, correlations, and trends in the data using different visualizations provided on the app's pages.
            """
        )

  

    # Call the about app page function
    show_about_app_page()
    

# Call the about page function
show_about_page()

import streamlit as st
import datetime

# ... (previous code)





