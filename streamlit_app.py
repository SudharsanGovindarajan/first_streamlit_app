import streamlit
import pandas
streamlit.title('🍕Our diet menu')
streamlit.header('🍽Dinner')
streamlit.text('Monday:🌭 Puttu')
streamlit.text('Tuesday: 🌽Solakarudhu Salad')
streamlit.text('Wednesday: 🍵Karuppu Arisi Kanji')
streamlit.text('Thursday: 🥗Aval Sundal')
streamlit.text('Friday: 👀TBD')
streamlit.text('Saturday: 🍍Fruit Salad after evening snacks')
streamlit.text('Sunday: 😎Anything based on mood')

streamlit.header('🍌 Build your own fruit smoothie 🍉')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# normalizing the json response from fruityvice
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Displaying the normalized json data as a pandas dataframe
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
