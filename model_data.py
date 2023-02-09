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
    print("Successful")
except:
    print("Unsuccessful")
    st.write(os.getcwd())
Diseases = {
    "Scab":["  i) Chemical control can reduce an infection but it's challenging to apply at just the right times.\n\n", " ii) Apple scab resistant cultivars are the best way to prevent an infestation.\n\n","iii) Raking and removing leaves around trees in fall will reduce a source of infection.\n\n"], 
    "Black_rot":["i) Remove diseased fruit as soon as you notice the problem.\n\n", "ii) This reduces the fungi that cause summer rots and spots."],
    "Cedar_rust":["i) It is caused by a fungus that makes its primary home in eastern red cedar trees and other junipers.\n\n", "ii) If possible, remove any junipers growing within 200 feet of an apple tree.\n\n", "iii) Many cedar apple rust resistant apple cultivars are available.\n\n"],
    "Cercospora_leaf":["i) Plant corn hybrids with resistance to the disease\n\n", "ii) Crop rotation and plowing debris into soil may reduce levels of inoculum in the soil but may not provide control in areas where the disease is prevalent\n\n", "iii) Foliar fungicides may be economically viable for some high yeilding susceptible hybrids."], 
    "Common_rust":["i) The most effective method of controlling the disease is to plant resistant hybrids\n\n", "ii) Application of appropriate fungicides may provide some degree on control and reduce disease severity\n\n", "iii) Fungicides are most effective when the amount of secondary inoculum is still low, generally when plants only have a few rust pustules per leaf."], 
    "Northern_Leaf_Blight":["i) Follow proper tillage to reduce fungus inoculum from crop debris.\n\n", "ii) Follow crop rotation with non host crop.\n\n", "iii) Grow available resistant varieties.\n\n", "iv) In severe case of disease incidence apply suitable fungicide."],
    "Black_Rut":[""], 
    "Esca":[], 
    "Blight":[],
    "Bacterial_Spot":[],
    "P_Early_Blight":[],
    "P_Late_Blight":[],
    "Early_Blight":[], 
    "Leaf_Mold":[], 
    "Target_Spot":[]
}