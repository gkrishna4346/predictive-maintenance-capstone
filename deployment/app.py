# Importing required libraries

import streamlit as st
import pandas as pd
import joblib

from huggingface_hub import hf_hub_download

# Page configuration

st.set_page_config(
    page_title="Predictive Maintenance System",
    layout="wide"
)

# Main title

st.markdown(
    "<h1 style='text-align:center;'>Predictive Maintenance System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;color:gray;'>Predict Engine Health</h4>",
    unsafe_allow_html=True
)

st.write("")

# Loading model from Hugging Face Model Hub

@st.cache_resource
def load_model():

    model_path = hf_hub_download(
        repo_id="gkrishna4346/predictive-maintenance-adaboost",
        filename="adaboost_model.pkl"
    )

    return joblib.load(model_path)

model = load_model()

# Three-column layout

left_space, input_section, output_section = st.columns([0.2, 2, 1.3])

# -------------------------
# INPUT SECTION
# -------------------------

with input_section:

    with st.container(border=True):

        st.subheader("Inputs")

        col1, col2 = st.columns(2)

        with col1:

            engine_rpm = st.number_input(
                "Engine rpm",
                value=1800.0
            )

            fuel_pressure = st.number_input(
                "Fuel pressure",
                value=20.0
            )

            lub_oil_temp = st.number_input(
                "lub oil temp",
                value=80.0
            )

        with col2:

            lub_oil_pressure = st.number_input(
                "Lub oil pressure",
                value=4.5
            )

            coolant_pressure = st.number_input(
                "Coolant pressure",
                value=3.0
            )

            coolant_temp = st.number_input(
                "Coolant temp",
                value=85.0
            )

        predict_button = st.button(
            "Predict",
            use_container_width=True
        )

# -------------------------
# OUTPUT SECTION
# -------------------------

with output_section:

    with st.container(border=True):

        st.subheader("Prediction Result")

        if predict_button:

            input_df = pd.DataFrame({
                "Engine rpm": [engine_rpm],
                "Lub oil pressure": [lub_oil_pressure],
                "Fuel pressure": [fuel_pressure],
                "Coolant pressure": [coolant_pressure],
                "lub oil temp": [lub_oil_temp],
                "Coolant temp": [coolant_temp]
            })

            prediction = model.predict(input_df)

            st.write("")

            if prediction[0] == 1:

                st.error("Engine Condition: Failure")
                st.warning("Action: Maintenance Required")

            else:

                st.success("Engine Condition: Normal")
                st.info("Action: No Maintenance Required")

        else:

            st.info("Click Predict to generate the result.")
