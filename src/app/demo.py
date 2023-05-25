import streamlit as st
# import soundfile as sf
from src.ner import build_entity
from src.speech2transcript import speech_to_transcript
from src.utils import save_transcript, download_transcript


# Speech to Transcript
st.header('Speach to Transcript')

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    audio_data = uploaded_file.getvalue()
    with open("src/data/file.m4a", "wb") as f:
        f.write(audio_data)
    st.success("Audio file saved successfully!")
transcript = speech_to_transcript("src/data/file.m4a")
# save_transcript("src/data/file.text", transcript)

download_transcript(transcript)



# Name Entity
st.image("https://www.rosette.com/wp-content/uploads/2022/03/header-img-event-extraction@2x.png")
st.header('Find Named Entitiy')

text = st.text_input('Enter Your Text')

gen_button = st.button('Generate')
if gen_button ==True:
    st.dataframe(build_entity(text))


