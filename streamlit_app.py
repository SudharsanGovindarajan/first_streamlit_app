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
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
