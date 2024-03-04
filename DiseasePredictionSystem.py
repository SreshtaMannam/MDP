import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pytesseract

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    select = option_menu('Diseases Prediction',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Disease Prediction'],
                         icons=['activity', 'heart', 'person'],
                         default_index=0)


# Function to convert PDF to images
def convert_pdf_to_images(pdf_file):
    images = []
    # Logic to convert each page of the PDF to an image
    # You can use pdf2image library for this task
    # Example code:
    # ...
    return images


# Function to extract text from images using OCR
def extract_text_from_images(images):
    extracted_text = ""
    for image in images:
        # Use pytesseract to extract text from each image
        text = pytesseract.image_to_string(image)
        extracted_text += text + "\n"
    return extracted_text


# Prediction function for Diabetes
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,
                     extracted_text):
    diabetes_diagnosis = ''
    if extracted_text:
        # Parse the extracted text and populate input fields accordingly
        # You need to implement logic to extract relevant information based on the structure of the scanned documents
        # For example:
        # Age = extracted_age
        pass

    diabetes_prediction = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diabetes_prediction[0] == 0:
        diabetes_diagnosis = 'The person is Not Diabetic'
    else:
        diabetes_diagnosis = 'The person is Diabetic'

    return diabetes_diagnosis


# Prediction function for Heart Disease
def predict_heart_disease():
    # Implement prediction logic for Heart Disease
    pass


# Prediction function for Parkinson's Disease
def predict_parkinsons_disease():
    # Implement prediction logic for Parkinson's Disease
    pass


# Main application
if select == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction')

    # Columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')

    # File uploader for PDF
    pdf_file = st.file_uploader("Upload PDF file", type="pdf")

    # Perform OCR and extract text from PDF
    if pdf_file is not None:
        images = convert_pdf_to_images(pdf_file)
        extracted_text = extract_text_from_images(images)

    # Button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_diagnosis = predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                                              DiabetesPedigreeFunction, Age, extracted_text)
        st.success(diabetes_diagnosis)

elif select == 'Heart Disease Prediction':
    # Implement UI and prediction logic for Heart Disease Prediction
    pass

elif select == 'Parkinsons Disease Prediction':
    # Implement UI and prediction logic for Parkinson's Disease Prediction
    pass



    
    
    
    
