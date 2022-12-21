import base64
import streamlit as st
import numpy as np
import os
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    .img {{
        opacity:1
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
def make_pred(image_path):
    class_codes={
                0:"Apple_Healthy", 1:"Apple_Scab", 2:"Apple_Black_rot", 3:"Apple_Cedar_rust", 
                4:"Corn_Healthy", 5:"Corn_Cercospora_leaf", 6:"Corn_Common_rust", 7:"Corn_Northern_Leaf_Blight",
                8:"Grape_Healthy", 9:"Grape_Black_Rut", 10:"Esca",11:"Grape_Blight",
                12:"Pepper_Healthy", 13:"Pepper_Bacterial_Spot",
                14:"Potato_Healthy", 15:"Potato_P_Early_Blight",16:"Potato_P_Late_Blight",
                17:"Tomato_Healthy", 18:"Tomato_Early_Blight", 19:"Tomato_Leaf_Mold", 20:"Tomato_Target_Spot"
            }
    image = np.asarray([img_to_array(image_path)/255,])
    obj_class = np.argmax(model.predict(image[0:1]))
    return class_codes[obj_class]


try:
    model = models.load_model("./models/LeafModel")
except:
     st.write(os.getcwd())
Diseases = {
    "Scab":["Leaving it out there in the Sun\n\n", "Paint it red"], "Cedar_rust":["Paint it Green"],
    "Cercospora_leaf":[], "Common_rust":[], "Northern_Leaf_Blight":[],
    "Black_Rut":[], "Esca":[], "Blight":[],
    "Bacterial_Spot":[],
    "P_Early_Blight":[],"P_Late_Blight":[],
    "Early_Blight":[], "Leaf_Mold":[], "Target_Spot":[]
}