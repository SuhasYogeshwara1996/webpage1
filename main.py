from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Suhas', page_icon=':iphone:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css('C:/Users/Suhas/Desktop/Machine Learning/style/style.css.txt')


lottie_coding = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_v4isjbj5.json')

Recommendedsystem=Image.open('C:/Users/Suhas/Desktop/Machine Learning/images/Recommendedsystem.jpg')

FACEREC = Image.open('C:/Users/Suhas/Desktop/Machine Learning/images/FACEREC.webp')

OCR = Image.open('C:/Users/Suhas/Desktop/Machine Learning/images/OCR.webp')

AIGame = Image.open('C:/Users/Suhas/Desktop/Machine Learning/images/AIGame.jpeg')

with st.container():
    st.subheader('Hi, I am Suhas Yogeshwara:wave:')
    st.title('Machine Learning/Data Science enthusiast from Germany')
    st.write('Actively looking for a challenging career in machine learning, data science, or software development methodologies that involve research, development, and design of autonomous artificial intelligence systems. having a self-developed sense of discipline, a steady learning process, and a history of success in the classroom. ')
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Work Experience:computer:')
        st.subheader('Data Science Intern')
        st.write('Analyzing exploratory data to assist business improvements.'
                 'Building Models from a Simple Dataset to Improve Understanding.'
                 'Display your understanding of and experience in application user interface development.')

    with right_column:
        st_lottie(lottie_coding,height=300,key='coding')

with st.container():
    st.write('---')
    st.header('Projects')
    st.write('##')

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(AIGame)

    with text_column:
        st.subheader('AI Game using Reinforcement Learning')
        st.write('Setting up Game Environment and Creation of Agent.'
                 'Traditional Methods of Building a Game AI, Smart enough to defeat novice player.'
                 'Coming up with cutting edge Reinforcement Learning Algorithm.')

    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(OCR)

    with text_column:
        st.subheader('Drug Label Extraction using PaddleOCR & Python')
        st.write('Extraction of Prescription Medication Labels.'
                 'Importing Dependencies like Matplotlib, Numpy and opencv.'
                 'Visualization of Image Texts.')


    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Recommendedsystem)

    with text_column:
        st.subheader('machine learning music recommended system')
        st.write('Baseline, Import and Data Cleansing.'
                 'Basic Music Recommendation Model Based on Users Preferences.'
                 'Decision Tree Model from SciKit Learn Library.')


    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(FACEREC)

    with text_column:
        st.subheader('Face Recognition Application')
        st.write('real-time dataset'
                 'Built in model for Use'
                 'Improving the quality')

with st.container():
    st.write('---')
    st.header('Get in Touch with me')
    st.write('##')
    contact_form= '''<form action="https://formsubmit.co/suhas.gys1996@gmail.com" method="POST">
    <input type="hidden" name='_captcha' value='false'>
     <input type="text" name="name" placeholder ='Your name' required>
     <input type="email" name="email" placeholder ='Your email' required>
     <input type="Message" placeholder='your message here' required></textarea>
     <button type="submit">Send</button>
</form>'''

left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()










