from .core import create_app
from dotenv import load_dotenv

# Necessary for development runs of gunicorn.
load_dotenv(".flaskenv")

app = create_app()

# app.run(port=5001)
# "flask run --port 5000 --debug" FLASK_ENV=development, FLASK_APP=app.core.
