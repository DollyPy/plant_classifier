import streamlit as st
from model_data import add_bg_from_local

add_bg_from_local("bg-01.jpg")
st.header("ABOUT")
st.write("""
This Crop disease detection system is a user - friendly detection system based on ML. This detection system majorly detects the crop’s plant leaf with just one click and label the disease accurately. It is not only a system but it is been developed in the form of a web-based application so that every user can make use of it and detect their crops. It will be feasible for farmers to use where they just have to upload the leaf image of the affected plant and automatically the disease will be detected and it will let the farmer know to how to treat that particular disease. Majorly the aimed users are farmers or the dealers/suppliers who deal with agriculture sector on daily basis. The product will definitely help them to cure or analyze the disease and will provide best solutions.

""")
