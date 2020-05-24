import os
from flask_mail import Mail
from quickboosters.config import DevConfig
from quickboosters import (
    create_app,
    db
)

from quickboosters.api.roles.dev.sample_data import create_role
from quickboosters.api.users.dev.sample_data import create_user
from quickboosters.api.orders.dev.sample_data import create_order

conf = os.getenv('FLASK_ENV')

if conf == 'development':
    print(DevConfig().verbose())
    app = create_app('development')
    app.app_context().push()
    db.create_all(app=app)
    print(app.url_map)
    create_role()
    create_user()
    create_order()

else:
    app = create_app('prod')


if __name__ == "__main__":
    app.run()
