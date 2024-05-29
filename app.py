#imports
import openai
import streamlit as st

openai.api_key = 'api-key'

#function for image generation
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        quality="hd"
    )
    image_url = response['data'][0]['url']
    return image_url

# Streamlit app
st.title("GET YOUR IMAGE DONE HERE <3")

prompt = st.text_input("Describe the image")
if st.button("Generate Image"):
    if prompt:
        with st.spinner('Generating image...'):
            try:
                image_url = generate_image(prompt)
                st.image(image_url, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")
