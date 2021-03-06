from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
	app.run()

def register_blueprints(app):
	from flask1.views import posts
	from flask1.admin import admin
	app.register_blueprint(posts)
	app.register_blueprint(admin)

register_blueprints(app)