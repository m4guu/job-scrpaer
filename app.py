import configparser
import os

from website import create_app

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


if __name__ == '__main__':
    app = create_app()  
    app.config['SECRET_KEY'] = 'secret key'
    app.config['MONGO_URI'] = config['DEV']['DB_URI']
    app.config['DEBUG'] = True


    app.run()