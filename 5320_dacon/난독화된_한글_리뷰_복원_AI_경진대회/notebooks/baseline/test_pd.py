from typing import Sequence

import pandas as pd
train = pd.read_csv('dataset/train.csv', encoding='utf-8-sig')
test = pd.read_csv('dataset/test.csv', encoding= 'utf-8-sig')

match_dict = {}

def replace_words(input_text: str, match_dict: dict) -> str:
    words = input_text.split()
    replaced_words = [match_dict.get(word, word)for word in words]
    return ' '.join(replaced_words)

# input과 output을 어절 수준으로 분해하여 매칭
for input_text, output_text in zip(train['input'], train['output']):
    input_word = input_text.split()
    output_word = output_text.split()
    # 단어 사전에 단어 추가
    for iw, ow in zip(input_word, output_word):
        match_dict[iw] = ow

converted_reviews = test['input'].apply(lambda x: replace_words(x, match_dict)).tolist()

# 제출
submission = pd.read_csv('dataset/sample_submission.csv', encoding= 'utf-8-sig')
submission['output'] = converted_reviews
submission.to_csv('result/submission.csv', index=False, encoding='utf-8-sig')