from flask import Flask

app = Flask(__name__, static_folder='./public', template_folder='./static')

import templates.home.views
import templates.extract.views
import templates.product.views