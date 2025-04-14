import streamlit as st
import requests
from requests.exceptions import RequestException

# Constants
# API_URL = "http://127.0.0.1:8000/predict"  # Using port 8000
API_URL = "http://api:5000/predict"  # Uses Docker service name

CLASS_NAMES = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]

# App configuration - removed page icon since we're simplifying
st.set_page_config(page_title="Iris Classifier", layout="centered")

# Main content - moved all content to main area
st.title("🌸 Iris Flower Classifier")
st.markdown("Enter the features of the iris flower to predict its class.")

# Create columns for input fields
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

with col2:
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

# Added brief instructions where sidebar was
st.markdown("""
*This app predicts iris flower species using machine learning.*  
*Enter the four flower measurements and click Predict.*
""")

# Prediction section
if st.button("Predict", type="primary"):
    payload = {
        "feature_array": [sepal_length, sepal_width, petal_length, petal_width]
    }
    
    try:
        with st.spinner("Predicting..."):
            response = requests.post(API_URL, json=payload, timeout=5)
            response.raise_for_status()
            
            result = response.json()
            prediction = result['prediction'][0]  # Note: Fixed typo from original
            
            st.success(f"🌼 **Predicted Class:** {CLASS_NAMES[prediction]}")
            
            if 'probabilities' in result:
                st.subheader("Class Probabilities")
                for i, prob in enumerate(result['probabilities'][0]):
                    st.progress(prob)
                    st.text(f"{CLASS_NAMES[i]}: {prob:.2%}")
                
    except RequestException as e:
        st.error(f"""
        ❌ Connection failed to {API_URL}
        
        Error details: {str(e)}
        
        Troubleshooting steps:
        1. Ensure FastAPI is running (check terminal)
        2. Try this command to test:
        curl -X POST {API_URL} -H "Content-Type: application/json" -d '{str(payload)}'
        """)
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")