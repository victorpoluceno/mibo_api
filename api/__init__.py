from flask import Flask

app = Flask(__name__)
app.config.from_object('api.settings.default')
app.config.from_envvar('API_SETTINGS', silent=True)

import api.views
