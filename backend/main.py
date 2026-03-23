from fastapi import FastAPI

# 1. FastAPIの「本体」をインスタンス化
# これが、あなたのWebサーバーの「心臓」になります。
app = FastAPI()

# 2. 「@」はデコレータ。特定のURLに来た時の挙動を指定します。
# 「/」に「GET（取得）」しに来たら、下の関数を実行せよ、という命令です。
@app.get("/")
def read_root():
    # 3. 辞書型（{}）を返すと、FastAPIが勝手に「JSON」に変換してくれます。
    # これがフロントエンド（JS）との共通言語になります。
    return {"status": "success", "message": "My clean start!"}