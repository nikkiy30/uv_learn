import numpy as np
from gensim.models import KeyedVectors

# モデルの読み込み（ハッカソン用軽量モデルを想定）
# model = KeyedVectors.load_word2vec_format('model.bin', binary=True)

def craft_alchemy(word_a, word_b, weight_a=1.0, weight_b=1.0):
    # 1. 各単語のベクトルを取得
    vec_a = model[word_a]
    vec_b = model[word_b]
    
    # 2. 重み付き加算（これが独自アルゴリズムの核）
    combined_vec = (vec_a * weight_a) + (vec_b * weight_b)
    
    # 3. 合成ベクトルに最も近い単語を検索
    # topn=3にして、似た概念をいくつか抽出する
    results = model.most_similar(positive=[combined_vec], topn=3)
    return results

# 実行例： 「炎」に「知性（重め）」を混ぜる
# 炎の熱量よりも、知的な鋭さを優先した錬金
output = craft_alchemy("炎", "知性", weight_a=0.5, weight_b=1.5)

for word, score in output:
    print(f"錬金成果物: {word} (適合度: {score:.4f})")