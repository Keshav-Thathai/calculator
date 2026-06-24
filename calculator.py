import streamlit as st

st.title("🧮 Pro Smart Calculator")
st.write("Welcome to your simple and fast installable calculator app.")
st.divider() 

print("Welcome to the calculator made by Keshav Thathai")
a=int(input("enter the first number"))
b=int(input("enter the first number"))
print("What kind of operation do you want \n press + for addition\n press - for subtraction\n press * for multiplication\n press / for division")
o=input("enter operation")
match o:
   case "+":
      print(f"The result is {a+b}")
   case "-":
      print(f"The result is {a+b}")
   case "*":
      print(f"The result is {a+b}")
   case "/":
      print(f"The result is {a+b}")
     

