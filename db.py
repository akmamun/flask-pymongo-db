from flask_pymongo import PyMongo
import server as s

s.app.config['MONGO_DBNAME'] = 'db_name'
s.app.config['MONGO_URI'] = 'mongodb://<db_user>:<db_password>@ds261429.mlab.com:61429/table_name_of_db'
mongo = PyMongo(s.app)
