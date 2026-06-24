import streamlit as st


st.title("Pro Smart Calculator  created by Keshav Thathai")
st.write("Welcome to your simple and fast installable calculator app.")
st.divider()


num1 = st.number_input("Enter First Number:", value=0)
num2 = st.number_input("Enter Second Number:", value=0)


operation = st.selectbox(
    "Choose Operation:", 
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)


if st.button("Calculate ✨", use_container_width=True):
    match operation:
        case "Addition (+)":
            st.success(f"### 🎯 Result: {num1 + num2}")
            st.success("Thank you for using the calculator")
        case "Subtraction (-)":
            st.success(f"### 🎯 Result: {num1 - num2}")
            st.success("Thank you for using the calculator")
        case "Multiplication (*)":
            st.success(f"### 🎯 Result: {num1 * num2}")
            st.success("Thank you for using the calculator")
        case "Division (/)":
            if num2 != 0:
                st.success(f"### 🎯 Result: {num1 / num2}")
            else:
                st.error("Error! Cannot divide by zero.")


