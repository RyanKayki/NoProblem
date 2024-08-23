from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

# Substitua "SUA_API_KEY" pela sua chave de API do Gemini
gemini.configure(api_key="your-key")
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/receita', methods=['POST'])
def make_receita():
    dados = request.json
    ingredientes = dados.get('ingredientes')
    
    prompt = f""" 
    mostre soluções para os problemas, seguindo esses criterios:
    - O texto deve ser apresentado em formato HTML com codificação UTF-8, sem o header. 
    - Use as font Clarendon LT, Lulo Clean, e Georgia.
    - O título deve ser um <h1>
    - subtítulos como <h2>
    - informações sobre o problema em um parágrafo (<p>) com um ícone 💡]
    - Como resolver em um parágrafo (<p>)
    - lista de soluções em uma lista não ordenada (<ul>).
    - coloque um <iframe>  de um video sobre uma solução.
    - Procure em fóruns relevantes e forneça links com a pesquisa, usando ícones 💬 (use target="_blank" para abrir em uma nova guia).
    - dicione dicas em uma lista ordenada (<ol>), e uma sugestão em um parágrafo (<p>).
    - Não inclua observações adicionais.
    o problema: {ingredientes}
"""



    try:
        resposta = model.generate_content(prompt,generation_config=gemini.types.GenerationConfig(temperature=1.5))
        receita = resposta.text.strip().split('\n')
        return (receita), 200

    except Exception as e:
        make_receita()

if __name__ == '__main__':
    app.run(debug=True)