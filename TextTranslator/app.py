import streamlit as st
import translator

translator = translator.Translator()

# Save model to disk
translator.save_model()

# Initialize Language Code to Name and vice versa mapping dict
lang_name_to_code = translator.get_lang_name_to_code()
lang_code_to_name = translator.get_lang_code_to_name()

with st.form(key='LangCodes'):
    c1, c2, c3 = st.columns(3)
    with c1:
        input_lang_name = st.selectbox('Please Select Input Language', sorted(lang_name_to_code.keys()))
        # Convert Input Language Name to Language Code
        input_lang_code = translator.get_lang_code_from_name(input_lang_name)

    with c3:
        output_lang_name = st.selectbox('Please Select Output Language', sorted(lang_name_to_code.keys()))
        # Convert Output Language Name to Language Code
        output_lang_code = translator.get_lang_code_from_name(output_lang_name)

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col4:
        submitButton = st.form_submit_button(label='Submit')

input_text = st.text_input("Input Text", value="", key = "input_text")

st.subheader(f'Your Input : {input_text}, will be translated from {input_lang_name} to {output_lang_name}')
output_text = ' '.join(translator.translate(input_text, input_lang_code, output_lang_code))


# Write Translated Text
st.subheader(f"Translated : {output_text}")
