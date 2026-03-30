from pydantic import BaseModel, Field

# 錬金術の依頼（リクエスト）
class AlchemyRequest(BaseModel):
    word1: str = Field(..., description="1つ目の単語", example="火")
    word2: str = Field(..., description="2つ目の単語", example="鳥")
    weight1: float = Field(1.0, description="1つ目の単語の重み", ge=0.0, le=2.0)
    weight2: float = Field(1.0, description="2つ目の単語の重み", ge=0.0, le=2.0)

# 錬金術の結果（レスポンス）
class AlchemyResponse(BaseModel):
    new_word: str = Field(..., description="生成された新概念")
    description: str = Field(..., description="概念の説明（現在は定型文）")
    rarity: int = Field(..., ge=1, le=100, description="レア度 (1-100)")
    similarity_score: float = Field(..., description="合成ベクトルとの近似度")