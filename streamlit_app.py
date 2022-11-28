import streamlit
import pandas

#import data
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#App title
streamlit.title('My Parents New Healthy Diner')

#Menu
streamlit.header('Breafast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#BYO Smoothie with info
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)


