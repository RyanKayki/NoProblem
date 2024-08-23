from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

# Substitua "SUA_API_KEY" pela sua chave de API do Gemini
gemini.configure(api_key="Your-key-api-gemini")
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/receita', methods=['POST'])
def make_receita():
    dados = request.json
    ingredientes = dados.get('ingredientes')
    
    prompt = f"""
    Crie uma lista com a solução do problma: {ingredientes} (problema e complementos).
    Apresente a lista no formato HTML com codificação UTF-8, sem o header,
    com o título em h1, subtítulos em h2, informações sobre o problema em parágrafo
    acompanhado de um ícone 💡, como resolver em parágrafo
    acompanhado de um ícone 💡, lista de soluções em lista não
    ordenada, link de vídeos 🎥, link de forum 💬 (coloque blank para abrir uma nova guia nos links) e dicas em lista ordenada, sugestão do que pode fazer em parágrafo.
    """

    try:
        resposta = model.generate_content(prompt)
        receita = resposta.text.strip().split('\n')
        return (receita), 200

    except Exception as e:
        return jsonify({"Erro": str(e)}), 300

if __name__ == '__main__':
    app.run(debug=True)
