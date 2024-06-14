import base64
import io
from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    ## convert pdf into image
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        
        first_page = images[0]
        
        #convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr,format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
    
st.set_page_config(page_title='ATS Resume Expert')
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your Resume(PDF)...",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")
    
submit1 = st.button("Tell me about the resume")

#submit2 = st.button("How can I improvise my skill")

submit3 = st.button("Percentage Match")

input_prompt1 = '''
You are an experienced HR with Tech Experience in the field of any one job role from Data Science or Data Analyst or Business Analyst or Product Manager or Project Manager or Product Owner. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with this role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
'''

#input_prompt2 = 

input_prompt3 = '''
You are a skilled ATS(Applicant Tracking System) scanner with a deep understanding of any one job role Data Science or Data Analyst or Business Analyst or Product Manager or Project Manager or Product Owner and deep ATS functionality.
Your Task is to evaluate the resume against the provided job description. Give me the percentage match if the resume matches the job description.
First output should come as percentage and then keywords missing and last final thoughts
'''

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write('Please upload the resume')
        
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write('Please upload the resume')
        