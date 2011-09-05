from flask import Flask, render_template

import requests

from api import app, decorators

@app.route('/api/list_categories/')
@decorators.cached(timeout=15*60)
@decorators.jsonp_proxy('http://www.miroguide.com/api/list_categories')
def list_categories():
    pass


@app.route('/api/get_channels/')
@decorators.cached(timeout=15*60)
@decorators.jsonp_proxy('http://www.miroguide.com/api/get_channels')
def get_channels():
    pass


@app.route('/api/get_channel/')
@decorators.cached(timeout=15*60)
@decorators.jsonp_proxy('http://www.miroguide.com/api/get_channel')
def get_channel():
    pass

