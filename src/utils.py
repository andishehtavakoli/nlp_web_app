import streamlit as st
import base64

def save_transcript(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)



def download_transcript(file_data):

    # Create a download link
    b64_file = base64.b64encode(file_data.encode()).decode()
    download_link = f'<a href="data:application/octet-stream;base64,{b64_file}" download="file.txt">Download File</a>'

    # Display the download button
    st.markdown(download_link, unsafe_allow_html=True)

