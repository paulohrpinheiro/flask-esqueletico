from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from app.mod_root.controllers import mod_root as root_module
app.register_blueprint(root_module)

application = app
