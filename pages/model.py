import streamlit as st
from PIL import Image
from model_data import Diseases, add_bg_from_local, make_pred

add_bg_from_local('bg-01.jpg')

st.header("Crop Disease Detection System")

crop_image = st.file_uploader("Upload Crop Image",["jpg","jpeg","png","svg"],False)

if crop_image:
    #image = crop_image.read()
    image = Image.open(crop_image)
    pred = make_pred(image)
    crop_type = pred.split("_")[0]
    Healthy =  pred.split("_")[1] == "Healthy"
    Health = "Healthy" if Healthy else "Unhealthy"
    if not Healthy:
        Disease = " ".join(pred.split("_")[1:])
        prevention = "".join(Diseases[Disease.replace(" ","_")])
        extra = f"<b>Disease Type: {Disease}</b>\n\n<b>Prevention: {prevention}</b>"
    else: 
        extra = ""
    cols = st.columns(2)
    cols[0].image(image.resize((200,200)))
    cols[1].header("Plant Information")
    cols[1].write(f"<b>Crop Type: {crop_type}</b>\n\n<b>Health Status: {Health}</b>\n\n{extra}", unsafe_allow_html=True)
    