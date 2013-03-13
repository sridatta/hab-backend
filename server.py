# #Post pages
from flask import *
from flask_simpledb import SimpleDb

app = Flask(__name__)
db = SimpleDb()


if __name__ == "__main__":
    app.debug = True
    app.run()
