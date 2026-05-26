import streamlit as st

st.title("Jackfruit Leaf Disease Classifier 🌿")

st.write("এইটা একটা demo Streamlit app। এখানে তুমি dataset বা model connect করতে পারবে।")

# Simple input
name = st.text_input("তোমার নাম লিখো:")
if name:
    st.success(f"স্বাগতম, {name}!")

# Simple button
if st.button("Click me"):
    st.info("তুমি button চাপছো ✅")
