from flask                                  import Flask
from environs                               import Env
import os

env = Env()
env.read_env()

UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']

ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif', 'jpeg'}


def create_upload_folder() -> None:

    if not os.path.exists(UPLOAD_FOLDER):

        os.mkdir(UPLOAD_FOLDER)
    
create_upload_folder()



def create_app():

    app = Flask(__name__)

    app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000

    from app.views.routes import init_app

    init_app(app, UPLOAD_FOLDER, ALLOWED_EXTENSIONS)

    return app