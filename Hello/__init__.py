import json
import logging
from . import dataStore
from flask import current_app, Flask, redirect, request,render_template, session, url_for
from google.cloud import error_reporting
import google.cloud.logging
import httplib2
from oauth2client.contrib.flask_util import UserOAuth2


oauth2 = UserOAuth2()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)


    dataStore.init_app(app)

    #oauth2 helper is initialized
    oauth2.init_app(
        app,
        scopes=['email', 'profile'],
        authorize_callback=_request_user_info)

    #Flask doesn't have logout by default, so added a logout handler
    @app.route('/logout')
    def logout():
        del session['profile']
        session.modified = True
        oauth2.storage.delete()
        return redirect(request.referrer or '/')

    # Register app with CRUD blueprint.
    from .crud import crud
    app.register_blueprint(crud, url_prefix='/Hello')

    # Entry point to the app.
    @app.route("/")
    def index():
        return redirect(url_for('crud.add'))


    # Reports an error if there is any
    @app.errorhandler(500)
    def error(e):
        error_client = error_reporting.Client(app.config['PROJECT_ID'])
        error_client.report_exception(
            http_context=error_reporting.build_flask_context(request))
        return """error occured""", 500

    return app


def _request_user_info(credentials):
    
    http = httplib2.Http()
    credentials.authorize(http)
    resp, content = http.request(
        'https://www.googleapis.com/oauth2/v2/userinfo')


    session['profile'] = json.loads(content.decode('utf-8'))
