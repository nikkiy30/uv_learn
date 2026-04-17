import numpy as np
from gensim.models import KeyedVectors

class AlchemyService:
    def __init__(self, model_path: str = None):
        self.model = KeyedVectors.load_word2vec_format(model_path, binary=True)
        pass

    def perform_logic(self, word1: str, word2: str, w1: float, w2: float):
        if word1 not in self.model or word2 not in self.model:
            return None, 0.0
        
        """
        ベクトルの線形結合による新概念の抽出
        式: V_result = (w1 * V_word1) + (w2 * V_word2)
        """
        v1 = self.model[word1]
        v2 = self.model[word2]
        target_vec = (w1 * v1) + (w2 * v2)
        result = self.model.most_similar(positive=[target_vec], topn=1)[0]
        return result[0], result[1]

    def calculate_rarity(self, similarity: float) -> int:
        # 近似度が低い（＝意外な組み合わせ）ほどレア度が高いという独自ロジック
        return int((1 - similarity) * 100)