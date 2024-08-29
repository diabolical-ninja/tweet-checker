"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

from tweet_analysis import analyse_tweet

st.title("Tweet Checker 🐦")
st.markdown(
    """
    Curious whether a tweet is influencing your or telling you straight up fibs? 🤔
    
    TweetChecker is here to save the save giving you a bias and factual accuracy assessment of your tweets 👌🏾
    """
)

with st.form(key="my_form"):
    text_input = st.text_area(label="Tweet goes here...")
    uploaded_files = st.file_uploader(
        "OPTIONAL: Upload tweet images",
        accept_multiple_files=True,
        type=["jpg", "jpeg", "png"],
    )
    submit_button = st.form_submit_button(label="Submit")

image_attachments = uploaded_files if uploaded_files else []


if submit_button:
    with st.spinner("Analysing tweet..."):
        tweet_analysis = analyse_tweet(text_input, image_attachments)

    st.header("Tweet Analysis")
    st.subheader(f"Bias Rating: {tweet_analysis.bias.rating}/10")
    st.write(tweet_analysis.bias.spectrum.title())

    st.subheader(f"Factual Accuracy: {tweet_analysis.accuracy.rating}/5")
    st.write(tweet_analysis.accuracy.description)

    st.subheader("Summary:")
    st.write(f"{tweet_analysis.summary}")
