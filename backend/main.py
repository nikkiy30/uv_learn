from fastapi import FastAPI
from .schemas import AlchemyRequest, AlchemyResponse
from .services.alchemy import AlchemyService

app = FastAPI()
alchemy_service = AlchemyService() # インスタンス化

@app.get("/")
def read_root():
    return {"status": "ok", "message": "The Alchemical Circle is ready."}

# 3. 錬金術実行の窓口（POSTメソッド）
@app.post("/alchemy", response_model=AlchemyResponse)
def perform_alchemy(request: AlchemyRequest):
    # ロジックの呼び出し
    new_word, score = alchemy_service.perform_logic(
        request.word1, request.word2, request.weight1, request.weight2
    )
    
    rarity = alchemy_service.calculate_rarity(score)
    
    return {
        "new_word": new_word,
        "description": "ベクトルの交わりによって、新たな概念が具現化しました。",
        "rarity": rarity,
        "similarity_score": score
    }