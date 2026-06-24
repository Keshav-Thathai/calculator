import streamlit as st


st.title("

|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___  ___   |
| | 7 | 8 | 9 | | / | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | * | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | - | |
| |___|___|___| |___| |
| | . | 0 | = | | + | |
| |___|___|___| |___| |
|_____________________|
Pro Smart Calculator")
st.write("Welcome to your simple and fast installable calculator app.")
st.divider()


num1 = st.number_input("Enter First Number:", value=0.0)
num2 = st.number_input("Enter Second Number:", value=0.0)


operation = st.selectbox(
    "Choose Operation:", 
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)


if st.button("Calculate ✨", use_container_width=True):
    match operation:
        case "Addition (+)":
            st.success(f"### 🎯 Result: {num1 + num2}")
        case "Subtraction (-)":
            st.success(f"### 🎯 Result: {num1 - num2}")
        case "Multiplication (*)":
            st.success(f"### 🎯 Result: {num1 * num2}")
        case "Division (/)":
            if num2 != 0:
                st.success(f"### 🎯 Result: {num1 / num2}")
            else:
                st.error("Error! Cannot divide by zero.")


