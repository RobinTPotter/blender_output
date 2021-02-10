from .functions import *
from .config import *
from .render_thread import RenderThread

from . import app

from flask import render_template, redirect, url_for, request



@app.route('/')
def index(name=None):
    print(request.headers)
    return render_template('hello.html', name=name)

@app.route('/image/<int:num>')
def image(num=None):
    img = Image.open('{temp}/{num:04d}.png'.format(temp=RENDER_PATH,num=num))
    return serve_pil_image(img)

@app.route('/render/<int:num>')
def render(num):
    myclass = RenderThread(BLENDFILE,RENDER_PATH,num)
    myclass.start()
    app.logger.info(myclass)
    return render_template('progress.html', out=myclass.stdout, err=myclass.stderr)

