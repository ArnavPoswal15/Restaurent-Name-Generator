import streamlit as st
import langchain_helper
st.title("Restaurent Name Generator")
cuisine = st.sidebar.selectbox("Pick and Cuisine",("American","Argentinian","Brazilian","British","Burmese","Cajun",
 "Caribbean","Chinese","Danish","Egyptian","Ethiopian","Filipino",
 "French","Fusion","German","Ghanaian","Greek","Haitian","Hungarian",
 "Indian","Indonesian","Irish","Israeli","Italian","Jamaican","Japanese",
 "Korean","Lebanese","Malaysian","Mexican","Moroccan","Nigerian",
 "Pakistani","Paleo","Peruvian","Persian","Polish","Portuguese",
 "Russian","South African","Spanish","Sri Lankan","Street Food",
 "Swedish","Syrian","Tex-Mex","Thai","Tunisian","Turkish","Vegan",
 "Vietnamese"))

if cuisine:
    response= langchain_helper.generate_retuarent_name_and_menu(cuisine)
    st.header(response['restaurent_name'])
    menu_items = response['menu_items'].split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)