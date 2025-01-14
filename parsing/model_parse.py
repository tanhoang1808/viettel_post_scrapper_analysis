import spacy
import pandas as pd
COMPLEX_WORDS = ['ai','robot','cloud','provider','cdn','cloud','session','cookies','server','vpn','machine','learning','storage','native','data','proxy','networking']

CATEGORY = {
    'AI' : ['ai','robot','machine','learning','deep','deep learning','neutral','bot'],
    'Network' : ['network','mạng','networking','website','hosting','vpc','lan','wan','man','san'],
    'Computer' : ['computer','vpn','proxy','server','máy chủ ảo','máy chủ'],
    'Data' : ['data','data center','sql','nosql','dữ liệu','kubernetes','storage'],
    'Cloud' : ['cloud','đám mây','cloud storage','aws','azure','azure factory']
        }

def GunningFogCalculate(document):
    sentences = list(document.sents)  # Chia câu
    words = [token.text for token in document if token.is_alpha]  # Chỉ lấy từ
    complex_words = [word for word in words if len(word) > 6]  # Từ dài hơn 6 ký tự
    avg_sentence_length = len(words) / len(sentences)
    percent_complex_words = len(complex_words) / len(words) * 100
    fog_index = 0.4 * (avg_sentence_length + percent_complex_words)
    return {
        sentences,
        words,
        complex_words,
        avg_sentence_length,
        percent_complex_words
    }


def CategoryByDict(pd:pd.Series) -> pd.Series:
    pass

