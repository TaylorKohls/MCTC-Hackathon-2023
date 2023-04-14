"""Configuration for Flask API"""
import os
import connexion
from flask_caching import Cache

my_app = connexion.App(__name__, specification_dir='./swagger')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/database.db')

my_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
my_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
my_app.app.config['CACHE_TYPE'] = 'SimpleCache'
my_app.app.config['CACHE_DEFAULT_TIMEOUT'] = 300

my_app.add_api('swagger.yml')
cache = Cache(my_app.app)