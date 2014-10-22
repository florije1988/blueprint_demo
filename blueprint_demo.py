from flask import Flask
# from demos.views import demo


def create_app():
    app = Flask(__name__)
    from demos import demo
    app.register_blueprint(demo, url_prefix='/demo')
    from main import main
    app.register_blueprint(main, url_prefix='/main')

    return app


# if __name__ == '__main__':
#     app.run()
