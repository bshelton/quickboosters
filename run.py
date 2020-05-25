import os
from flask_mail import Mail
from quickboosters.config import DevConfig
from quickboosters.environments import Environment as env
from quickboosters import (
    create_app,
    db
)


conf = os.getenv('FLASK_ENV')

if conf == 'development':
    print(DevConfig().verbose())
    app = create_app(env.DEVELOPMENT)
    app.app_context().push()
    db.create_all(app=app)
    print(app.url_map)
else:
    app = create_app('prod')


if __name__ == "__main__":
    app.run()
