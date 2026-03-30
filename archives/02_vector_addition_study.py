import numpy as np

def complex_alchemy(model, base_word, minus_word, axis_word=None):
    # 1. ベクトルの取得
    v_base = model[base_word]
    v_minus = model[minus_word]
    
    # 2. 演算：ベースから特定の要素を引き、属性軸を加える
    # 例：『王』から『男』を引き、『女』の成分を強調する
    res_vec = v_base - v_minus
    
    if axis_word:
        v_axis = model[axis_word]
        res_vec = res_vec + (v_axis * 0.5) # 特定の属性を少し足す
    
    # 3. 類似単語の検索
    results = model.most_similar(positive=[res_vec], topn=1)
    return results[0] # (word, similarity)