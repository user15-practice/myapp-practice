from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! デプロイ成功！'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5201)  # XX を自分のポート番号に変更
