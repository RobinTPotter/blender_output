from flask import Flask, request
from flask import render_template
from flask_bootstrap import Bootstrap

from PIL import Image
import io


app = Flask(__name__)
bootstrap = Bootstrap(app)

from .functions import *


@app.route('/')
@app.route('/<string:name>')
def index(name=None):
    print(request.headers)
    return render_template('hello.html', name=name)

@app.route('/image/<int:num>')
def image(num=None):
    img = Image.open('temp/{:04d}.png'.format(num))
    return serve_pil_image(img)

if __name__ == "__main__":
    app.run(debug=True)
