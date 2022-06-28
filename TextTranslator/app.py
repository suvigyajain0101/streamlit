import streamlit as st

lang_name_to_code = {'Arabic': 'ar_AR',
                     'Czech': 'cs_CZ',
                     'German': 'de_DE',
                     'English': 'en_XX',
                     'Spanish': 'es_XX',
                     'Estonian': 'et_EE',
                     'Finnish': 'fi_FI',
                     'French': 'fr_XX',
                     'Gujarati': 'gu_IN',
                     'Hindi': 'hi_IN',
                     'Italian': 'it_IT',
                     'Japanese': 'ja_XX',
                     'Kazakh': 'kk_KZ',
                     'Korean': 'ko_KR',
                     'Lithuanian': 'lt_LT',
                     'Latvian': 'lv_LV',
                     'Burmese': 'my_MM',
                     'Nepali': 'ne_NP',
                     'Dutch': 'nl_XX',
                     'Romanian': 'ro_RO',
                     'Russian': 'ru_RU',
                     'Sinhalese': 'si_LK',
                     'Turkish': 'tr_TR',
                     'Vietnamese': 'vi_VN',
                     'Chinese': 'zh_CN'}

lang_code_to_name = {}
for k, v in lang_name_to_code.items():
    lang_code_to_name[v] = k

with st.form(key='LangCodes'):
    c1, c2 = st.columns(2)
    with c1:
        input_lang_code = st.selectbox('Please Select Input Language', sorted(lang_name_to_code.keys()))

    with c2:
        output_lang_code = st.selectbox('Please Select Output Language', sorted(lang_name_to_code.keys()))

    submitButton = st.form_submit_button(label='Submit')

input_text = st.text_input("Input Text", key = "input_text")

st.subheader(f'Your Input : {input_text}, will be translated from {input_lang_code} to {output_lang_code}')
