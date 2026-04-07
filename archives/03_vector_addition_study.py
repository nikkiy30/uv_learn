import numpy as np

def calculate_rarity_score(similarity, vector_norm):
    """
    similarity: 合成ベクトルとの近似度 (0.0 ~ 1.0)
    vector_norm: 結果単語のベクトルの大きさ（概念の強さ）
    """
    # 類似度が「高すぎず低すぎない」ゾーンをレアとする独自ロジック
    # 似すぎている = 順当すぎる / 遠すぎる = 無関係すぎる
    rarity_base = 1.0 - abs(similarity - 0.7) 
    
    # ベクトルのノルム（長さ）が極端に大きい単語は、強い個性を持つ
    norm_bonus = np.log1p(vector_norm)
    
    final_score = rarity_base * norm_bonus
    return np.clip(final_score * 100, 1, 100)

# 出力イメージ
# 太陽 + 叡智 = 黄金 (similarity: 0.72) -> Rarity: 85 (SSR)
# 火 + 水 = ぬるま湯 (similarity: 0.95) -> Rarity: 12 (Common)