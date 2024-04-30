import pickle as pk
import streamlit as st
import pandas as pd
import joblib as jb

l = ['concave points_worst', 'perimeter_worst', 'concave points_mean',
       'radius_worst', 'perimeter_mean', 'area_worst', 'radius_mean',
       'area_mean', 'concavity_mean', 'concavity_worst']

hide_menu = """
<style>
#MainMenu {
       visibility:hidden;
       }
footer:after{
content:"Copyright @ 2021: Streamlit";
display: block;
position: relative;
color: tomato;
}
</style>
"""
st.markdown(hide_menu,unsafe_allow_html=True)

model = pk.load(open("SV_model.pkl","rb"))
def num_to_let (x):
    if x == 0:
        x = "Benign"
    else:
        x = "Malignant"
    return x
st.title("Cancer Prediction System")
concave_pw = st.slider("Concave points_worst",0.0,100.0)
perimeter_worst = st.slider("Perimeter_worst",0.0,500.0)
concave_pm = st.slider("Concave points_mean",0.0,100.0)
radius_w = st.slider("Radius_worst",0.0,50.0)
perimeter_mean = st.slider("Perimeter_mean",0.0,300.0)
area_worst = st.slider("Area_worst",0.0,5000.0)
radius_mean = st.slider("Radius_mean",0.0,100.0)
area_mean = st.slider("Area_mean",0.0,5000.0)
concavity_mean = st.slider("Concavity_mean",0.0,10.0)
concavity_worst = st.slider("Concavity_worst",0.0,10.0)
value = [concave_pw,perimeter_worst,concave_pm,radius_w,perimeter_mean,area_worst,radius_mean,area_mean,concavity_mean,concavity_worst]

if st.button("predict"):
       data = pd.DataFrame([value], columns=l)
       pre = model.predict(data)
       st.text_input("prediction result", num_to_let(pre))