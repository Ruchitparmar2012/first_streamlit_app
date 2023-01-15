import streamlit as st
import pandas as pd

st.header("My Mom's New healthy Diner")
st.title('BreakFast Favorites')
st.text('🥣 BreakFast Menu')
st.text('🥗 Omega 3 & Blueberry Oatmeal')
st.text('🐔 Kale,Spinach & Rocket Smoothie')
st.text('🥑🍞 Hard-Boiled Free-Range Egg')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
st.multiselect('Pick Some Fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
st.dataframe(my_fruit_list)
