import streamlit as st
import json
import requests

st.title('Daily News Application 🗞️')

api_key="7cf59655df194aa7b5f8e048eb2a0bf1"

base_url = 'https://newsapi.org/v2/everything'

topic = st.text_input('Enter any news topic:')
page = st.number_input('how many articles do you need?', min_value=1)

p = {
    'q': topic,
    'apiKey': api_key,
    'pageSize': page
}



#
if st.button('Display News'):
    response = requests.get(base_url, params=p)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']

        st.subheader('Headlines:')

        for article in articles:
            title = article['title']
            url = article['url']
            desc = article['description']
            image = article['urlToImage']

            html_code = f"""  
            <div style="background-color:#f1cfa0  ; padding:15px; margin-bottom:20px; border-radius:10px; color:black;">  
                <h2>{title}</h2>  
                <p>Link to the article: <a href="{url}">{url}</a></p>  
                <p>{desc}</p>  
                <img src="{image}" style="width:100%; border-radius:5px;">  
            </div>  
            """
            st.markdown(html_code, unsafe_allow_html=True)
