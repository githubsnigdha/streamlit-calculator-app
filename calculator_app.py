import streamlit as st

st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Operation selection
operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate based on selection
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    
    st.success(f"Result: {result}")
