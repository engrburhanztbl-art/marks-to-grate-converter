import streamlit as st

st.title("Marks to Grade Converter 🎓")
st.write("Enter the marks and get the corresponding grade.")

# Input marks
marks = st.number_input("Enter your marks (0 - 100):", min_value=0, max_value=100, step=1)

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

if st.button("Get Grade"):
    grade = get_grade(marks)
    st.success(f"Your grade is: **{grade}**")
