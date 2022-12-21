import streamlit as st
from model_data import add_bg_from_local

add_bg_from_local("bg-2.jpg")
st.title("FINAL YEAR PROJECT")
st.subheader("Crop Disease Detection System")
st.write(
    """
    <b>Ofodi Christabel (19/SCI01/070)</b>
    
    <b>Fasoiro Victor (19/SCI01/046)</b>

    <b>Department: Computer Science</b>

    <b>Supervisor: Mr. O.A Sanya</b>

    """, unsafe_allow_html=True
)
