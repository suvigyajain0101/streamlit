from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import streamlit as st

PATH = r'C:\Users\dell\Desktop\Plotly\Streamlit\model'

# Define Mappings
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


class Translator():

    def __init__(self):
        self.name = 'Translator'
        self.lang_name_to_code = lang_name_to_code
        self.lang_code_to_name = lang_code_to_name
        self.model, self.tokenizer = self.load_model()

    def get_lang_code_from_name(self, lc):
        return self.lang_name_to_code[lc]

    def get_lang_code_to_name(self):
        return self.lang_code_to_name

    def get_lang_name_to_code(self):
        return self.lang_name_to_code

    # Define Translation Function
    def translate(self, input_sentence, input_lang_code, output_lang_code):

        # Assign Input Language to the tokenizer
        self.tokenizer.src_lang = input_lang_code

        # Encode Input Sentence
        encoded_input = self.tokenizer(input_sentence, return_tensors="pt")

        # Generate Output Tokens
        generated_tokens = self.model.generate(**encoded_input,
                                               forced_bos_token_id=self.tokenizer.lang_code_to_id[output_lang_code])

        # Convert Tokens to Sequence
        output_sentence = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        return output_sentence

    def save_model(self):
        # You can then save them locally via:
        self.tokenizer.save_pretrained(PATH)
        self.model.save_pretrained(PATH)
        print('Saved')

    def load_model(self):
        try:
            local_tokenizer = MBart50TokenizerFast.from_pretrained(PATH)
            local_model = MBartForConditionalGeneration.from_pretrained(PATH)
            print('Loaded from disk')
            return local_model, local_tokenizer
        except OSError:
            hf_model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
            hf_tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
            print('Loaded from HuggingFace')
            return hf_model, hf_tokenizer
