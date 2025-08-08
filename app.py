from flask import Flask, render_template, request, url_for
from rembg import remove
import os

app = Flask(__name__)

STATIC_PATH = os.path.join(app.root_path, 'static')
INPUT_IMG = 'input.png'
OUTPUT_IMG = 'output.png'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        error_message = 'Nenhuma imagem foi enviada. Por favor, selecione um arquivo.'
        return render_template('index.html', error=error_message)

    file = request.files['image']

    if file.filename == '':
        error_message = 'Nenhum arquivo foi selecionado. Por favor, escolha uma imagem.'
        return render_template('index.html', error=error_message)

    if not (file.filename.lower().endswith(('.png', '.jpg', '.jpeg'))):
        error_message = 'Formato inválido. Por favor, envie arquivos PNG ou JPG.'
        return render_template('index.html', error=error_message)

    try:
        # Salvar a imagem original em static/input.png
        input_path = os.path.join(STATIC_PATH, INPUT_IMG)
        file.save(input_path)

        # Abrir o arquivo original para remover fundo
        with open(input_path, 'rb') as f:
            input_data = f.read()

        output_data = remove(input_data)

        # Salvar a imagem processada em static/output.png
        output_path = os.path.join(STATIC_PATH, OUTPUT_IMG)
        with open(output_path, 'wb') as f:
            f.write(output_data)

        return render_template('index.html', processed_image=True)

    except Exception as e:
        error_message = 'Ocorreu um erro ao processar a imagem. Tente novamente com outra imagem.'
        return render_template('index.html', error=error_message)
    

if __name__ == '__main__':
    app.run(debug=True)

