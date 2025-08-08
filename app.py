from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
import io
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
        # Abre imagem e redimensiona se maior que 800px largura
        img = Image.open(file.stream)
        max_width = 800
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.ANTIALIAS)

        # Salva imagem redimensionada em memória
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Remove fundo
        output_data = remove(img_byte_arr)

        # Salva imagens na pasta static
        input_path = os.path.join(STATIC_PATH, INPUT_IMG)
        output_path = os.path.join(STATIC_PATH, OUTPUT_IMG)

        # Salva a imagem original redimensionada
        with open(input_path, 'wb') as f:
            f.write(img_byte_arr)

        # Salva a imagem sem fundo
        with open(output_path, 'wb') as f:
            f.write(output_data)

        return render_template('index.html', processed_image=True)

    except Exception as e:
        error_message = f'Ocorreu um erro ao processar a imagem: {str(e)}'
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
