from flask import render_template
from jinja2 import TemplateNotFound

from quickboosters.frontend.home import home


@home.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@home.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        return render_template(template)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    except:
        return render_template('page-500.html'), 500
