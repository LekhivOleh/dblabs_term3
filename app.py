from flask_migrate import Migrate
from src import db, create_app

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)