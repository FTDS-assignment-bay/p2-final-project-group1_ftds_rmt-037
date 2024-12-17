from helper import text_preprocessing, scrape_reviews_and_ratings
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import ast
# Pre-processing & Feature Engineering
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.impute import SimpleImputer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

st.header("💬 Tokopedia Shoe Sentiment Analysis")

st.markdown("""
    <style>
      .stTextInput > label > div > p {
        font-size: 23px;
        padding: 0;
        margin: 0;
        font-weight: 600;
      }
    </style>
""", unsafe_allow_html=True)

user_input = st.text_input("Enter Tokopedia shoe product link for sentiment analysis")

# Define Stopwords
stpwds_id = list(set(stopwords.words('indonesian')))
# Define Stemming
stemmer = StemmerFactory().create_stemmer()

# Open slangwords_indonesian.txt
with open('slangwords_indonesian.txt') as f:
    data = f.read()
slangwords_indonesian =  ast.literal_eval(data)

model = tf.keras.models.load_model('nlp_model')



sentiment_colors = {
    "Positive": "#28a745",
    "Negative": "#dc3545"   
}

if st.button('Submit', type="secondary"):
  sentiments = ["Positive", "Negative"]
  with st.spinner("Please wait while we're loading the data..."):
    the_data = scrape_reviews_and_ratings(user_input)
    # Applying Text Preprocessing to the Dataset
    the_data['Review_processed'] = the_data['Review'].apply(lambda x: text_preprocessing(x, slangwords_indonesian))
    y_pred_inf = model(the_data['Review_processed'])
    y_pred_inf = np.argmax(y_pred_inf.numpy(), axis=1)  # Menentukan label 0 atau 1

    # Combine into dataframe
    inffinal = pd.DataFrame()
    inffinal['Review_processed'] = the_data['Review_processed']
    inffinal['Sentiment'] = pd.DataFrame(y_pred_inf)
    inffinal['Sentiment_meaning'] = inffinal['Sentiment'].apply(lambda x: 'Positive' if x != 0 else 'Negative')
    # Hitung jumlah positif dan negatif
    data_count = inffinal['Sentiment'].shape[0]
    positive_count = inffinal[inffinal['Sentiment'] == 1].shape[0]
    negative_count = inffinal[inffinal['Sentiment'] == 0].shape[0]
    st.balloons()
    st.markdown(f"""<p style="color: gray;">Total Review: {data_count}</p>""", unsafe_allow_html=True)
    st.markdown(f"""<p style="color: green;">Positives: {positive_count}</p>""", unsafe_allow_html=True)
    st.markdown(f"""<p style="color: red;">Negatives: {negative_count}</p>""", unsafe_allow_html=True)
#         for index, data in enumerate(the_data):
#           sentiment_color = sentiment_colors.get(sentiment_data.iloc[index, 0], "#6c757d")
#           comment_html = f"""
#               <div style="background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin: 20px auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
#                 <p style="font-size: 18px; line-height: 1.6; color: #333; font-family: 'Arial', sans-serif;">
#                   {data["comment"]}
#                 </p>
#                 <p style="font-size: 16px; color: gray; margin-top: 15px; font-family: 'Arial', sans-serif; font-weight: bold;">
#                   Sentiment Analysis: <span style="color: {sentiment_color}; font-size: 18px; font-weight: bold; padding: 5px 10px; background-color: {sentiment_color + "33"}; border-radius: 5px;">
#                     {sentiment_data.iloc[index, 0]}
#                   </span>
#                 </p>
#               </div>
#             """

#           st.markdown(comment_html, unsafe_allow_html=True)
#     else:
#       st.write("Invalid youtube link.")
#   except Exception as e:
#     print(e)
#     st.write("Invalid youtube link.")
    