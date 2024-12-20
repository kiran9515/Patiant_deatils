# Import necessary packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Page configuration for better appearance
st.set_page_config(
    page_title="Patient Information Lookup", 
    page_icon="🩺", 
    layout="wide"
)

# App title and header
st.title("Patient Information Lookup 🩺")
st.markdown(
    """
    Welcome to the patient info dashboard. Use the search bar below to retrieve specific patient information from the database. 
    """
)

# Get the current Snowflake session
session = get_active_session()

# Input section with placeholder for better guidance
Patient_id_picker = st.text_input(
    "Enter the Patient ID:", 
    placeholder="E.g., P001",
    help="Type a valid patient ID to retrieve detailed information."
)

# Logic to handle user input and fetch data
if Patient_id_picker:
    sql = """
    SELECT * 
    FROM HEALTH_CARE.PATIENT.PATIENT_DETAILS
    WHERE PATIENTID = '{text_input}'
    """
    
    try:
        # Run the SQL query
        result = session.sql(sql.format(text_input=Patient_id_picker))
        result_df = result.to_pandas()

        # Display results in a clear way
        if not result_df.empty:
            st.success(f"Showing results for Patient ID: {Patient_id_picker}")
            st.dataframe(result_df, use_container_width=True)
        else:
            st.warning(f"No data found for Patient ID: {Patient_id_picker}")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer for branding or instructions
st.markdown("---")
st.markdown("**Note:** Please ensure the Patient ID is valid and that the database connection is active.")
