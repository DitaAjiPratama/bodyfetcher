import cherrypy
import cherrypy_cors
import json

def body_json():
    if cherrypy.request.method == 'OPTIONS':
        cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])
    if cherrypy.request.method == 'POST':
        cherrypy.serving.response.headers['Content-Type'] = 'application/json'
    return json.loads(cherrypy.request.body.read().decode())
