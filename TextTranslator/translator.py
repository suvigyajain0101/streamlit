from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

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
        self.model = model
        self.tokenizer = tokenizer
        self.lang_name_to_code = lang_name_to_code
        self.lang_code_to_name = lang_code_to_name

    def get_lang_code_from_name(self, lc):
        return self.lang_name_to_code[lc]

    # Define Translation Function
    def translate(self, input_sentence, input_lang_code, output_lang_code):
        lm, lt = self.load_model()

        # Assign Input Language to the tokenizer
        lt.src_lang = input_lang_code

        # Encode Input Sentence
        encoded_input = lt(input_sentence, return_tensors="pt")

        # Generate Output Tokens
        generated_tokens = lm.generate(**encoded_input,
                                       forced_bos_token_id=lt.lang_code_to_id[output_lang_code])

        # Convert Tokens to Sequence
        output_sentence = lt.batch_decode(generated_tokens, skip_special_tokens=True)

        return output_sentence

    def save_model(self):
        # You can then save them locally via:
        self.tokenizer.save_pretrained(PATH)
        self.model.save_pretrained(PATH)
        print('Saved')

    def load_model(self):
        local_tokenizer = MBart50TokenizerFast.from_pretrained(PATH)
        local_model = MBartForConditionalGeneration.from_pretrained(PATH)
        print('Loaded')
        return local_model, local_tokenizer
