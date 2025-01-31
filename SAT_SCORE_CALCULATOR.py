import streamlit as st
import pandas as pd

# Load the grading data from the Excel file
def load_grading_data():
    try:
        file_path = 'Grading Sheet - SAT Exam.xlsx'  # Ensure this file is in the same directory
        sheet_data = pd.read_excel(file_path)

        # Clean and structure the data
        structured_data = sheet_data.iloc[1:, :].dropna()
        structured_data.columns = ["Raw_Score", "RW_Lower", "RW_Upper", "Math_Lower", "Math_Upper"]
        structured_data = structured_data.astype({
            "Raw_Score": int,
            "RW_Lower": int,
            "RW_Upper": int,
            "Math_Lower": int,
            "Math_Upper": int
        })
        return structured_data
    except FileNotFoundError:
        st.error("The Excel file is missing. Please upload the file to the deployment directory.")
        return pd.DataFrame(columns=["Raw_Score", "RW_Lower", "RW_Upper", "Math_Lower", "Math_Upper"])

# Streamlit app
st.title("SAT Score Calculator")

st.write("Enter the number of correct answers for each section below:")

# Input from the user
rw_correct = st.number_input("Number of correct answers in Reading and Writing:", min_value=0, max_value=69, step=1)
math_correct = st.number_input("Number of correct answers in Math:", min_value=0, max_value=57, step=1)

# Retrieve the scores based on input
rw_score = grading_data[grading_data['Raw_Score'] == rw_correct]
math_score = grading_data[grading_data['Raw_Score'] == math_correct]

# Display the scores if valid inputs are provided
if not rw_score.empty and not math_score.empty:
    rw_lower = rw_score['RW_Lower'].values[0]
    rw_upper = rw_score['RW_Upper'].values[0]
    math_lower = math_score['Math_Lower'].values[0]
    math_upper = math_score['Math_Upper'].values[0]

    total_lower = rw_lower + math_lower
    total_upper = rw_upper + math_upper

    st.subheader("Your SAT Section Scores:")
    st.write(f"Reading and Writing: {rw_lower} - {rw_upper}")
    st.write(f"Math: {math_lower} - {math_upper}")
    st.subheader("Your Total SAT Score Range:")
    st.write(f"Total Score: {total_lower} - {total_upper}")
else:
    st.write("Please enter valid numbers of correct answers.")
