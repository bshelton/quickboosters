from flask import Flask, render_template, Blueprint, request
from flask_login import login_required, login_url, current_user

import json

from users.models import User

from quickboosters import app, db, socketio

adminbp = Blueprint('adminbp', __name__, template_folder='templates', static_folder='static',static_url_path='/admin/static')

@adminbp.route('/admindashboard')
def admindashboard():
    return render_template('/admin/index.html')

@adminbp.route('/admin/test')
def test():
    return render_template('/admin/test.html')

@adminbp.route('/admin/user-lookup')
def user_lookup():
    return render_template('/admin/user-lookup.html')

@adminbp.route('/admin/user-search', methods=['GET','POST'])
def user_search():
    search_text = request.args.get("searchText")
    matches = []
    users = User.query.filter(User.username.like("%" + search_text + "%")).all()
    
    for f in users:
        matches.append(f.username)

    new_matches = dict(enumerate(matches))

    json_matches = json.dumps(new_matches)

    return json_matches
    
@adminbp.route('/admin/create-user')
def create_user():
    return render_template('admin/create-user.html')

@adminbp.route('/admin/register')
def register_user():
    return render_template('admin/register.html')

@adminbp.route('/error_404')
def error_404():
    return render_template('admin/404.html')

@adminbp.route('/error_500')
def error_500():
    return render_template('admin/500.html')

@adminbp.route('/charts')
def charts():
    return render_template('admin/charts.html')

@adminbp.route('/ui-buttons')
def ui_buttons():
    return render_template('admin/ui-buttons.html')

@adminbp.route('/form-elements')
def form_elements():
    return render_template('admin/form-elements.html')

@adminbp.route('/form-wizard')
def form_wizard():
    return render_template('admin/form-wizard.html')

@adminbp.route('/form-image-crop')
def form_image_crop():
    return render_template('admin/form-image-crop.html')

@adminbp.route('/form-x-editable')
def form_x_editable():
    return render_template('admin/form-x-editable.html')

@adminbp.route('/gallery')
def gallery():
    return render_template('admin/gallery.html')

@adminbp.route('/layout-blank')
def layout_blank():
    return render_template('admin/layout-blank.html')

@adminbp.route('/layout-boxed')
def layout_boxed():
    return render_template('admin/layout-boxed.html')

@adminbp.route('/layout-fixed-header')
def layout_fixed_header():
    return render_template('admin/layout-fixed-header.html')

@adminbp.route('/lockscreen')
def lockscreen():
    return render_template('admin/lockscreen.html')


@adminbp.route('/admin/login')
def login():
    return render_template('admin/login.html')

@adminbp.route('/table-data')
def table_data():
    return render_template('admin/table-data.html')

@adminbp.route('/table-responsive')
def table_responsive():
    return render_template('admin/table-responsive.html')

@adminbp.route('/table-static')
def table_static():
    return render_template('admin/table-static.html')

@adminbp.route('/ui-alerts')
def ui_alerts():
    return render_template('admin/ui-alerts.html')

@adminbp.route('/ui-modals')
def ui_modals():
    return render_template('admin/ui-modals.html')

@adminbp.route('/ui-nestable')
def ui_nestable():
    return render_template('admin/ui-nestable.html')

@adminbp.route('/ui-tabs-accordions')
def ui_tabs_accordions():
    return render_template('admin/ui-tabs-accordions.html')

@adminbp.route('/pricing-tables')
def pricing_tables():
    return render_template('admin/pricing-tables.html')