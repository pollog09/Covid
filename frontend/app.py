from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Aquí iría la lógica para comparar la imagen con el modelo de IA
        # y obtener la categoría
        category = "dummy_category"  # Reemplaza esto con la lógica real
        return render_template('result.html', category=category, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)