# My random WSGI playings around.
# This is called application because if you want to use this
# with mod_wsgi it is requied to be named application

def application(environ, start_response):
    response_body = 'Request method %s' % environ['REQUEST_METHOD']
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

