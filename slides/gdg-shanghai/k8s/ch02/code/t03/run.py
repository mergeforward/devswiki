import connexion
from flask_cors import CORS
from prometheus_client import make_wsgi_app
# from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask

if __name__ == '__main__':


    # app = Flask(__name__)
    capp = connexion.FlaskApp(__name__, specification_dir='specs/')
    capp.add_api('blog.yaml', arguments={'title': 'Hello World Example'})
    # capp.app.wsgi_app = DispatcherMiddleware(capp.app.wsgi_app, {
    #     '/metrics': make_wsgi_app(),
    #     # '/api': con_app.app
    # })

    # app.wsgi_app = connexion.App(app.wsgi_app)


    # con_app = connexion.FlaskApp(__name__, port=9090, specification_dir='specs/')
    # con_app = connexion.FlaskApp(__name__, specification_dir='specs/')
    # con_app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example'})
    # app.wsgi_app = con_app    
    # # app.add_api('project.yaml', arguments={'title': 'project'})

    # app.app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    #     '/metrics': make_wsgi_app()
    # })
    # CORS(app)
    CORS(capp.app)
    capp.run(host='0.0.0.0', debug=True, port=9090)
