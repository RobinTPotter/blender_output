from .functions import *
from .config import *
from .render_thread import RenderThread

from . import app

from flask import render_template, redirect, url_for, request



@app.route('/')
def index(name=None):
    #app.logger.info(request.headers)
    #app.logger.info(request.args)
    #if "robin" in request.args: app.logger.info("hello {}".format(request.args["robin"]))
    return render_template('hello.html', name=name)

@app.route('/image/<int:num>')
def image(num=None):
    img = Image.open('{temp}/{num:04d}.png'.format(temp=RENDER_PATH,num=num))
    return serve_pil_image(img)

@app.route('/render/<int:num>')
def render(num):
    params = {"size_multiplier": 1.0, "border_boolean": "", "place": "bl"}
    for k in params:
        if k in request.args: params[k] = request.args[k]

    myclass = RenderThread(BLENDFILE,RENDER_PATH,num,bool(params["border_boolean"]),params["place"],float(params["size_multiplier"]))
    myclass.start()
    app.logger.info(myclass)
    return render_template('progress.html', out=myclass.stdout, err=myclass.stderr)

