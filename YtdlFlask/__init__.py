from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6eafc9425925847cb4218e97d28a6cb'

from YtdlFlask import routes