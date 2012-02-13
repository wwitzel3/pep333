# My random WSGI playings around.
from wsgiref.simple_server import make_server

# This is called application because if you want to use this
# with mod_wsgi it is requied to be named application

def application(environ, start_response):
    response_body = ['{0}: {1}'.format(key, val)
                     for key, val in sorted(environ.items())]
    response_body = '\n'.join(response_body)
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

def main():
    httpd = make_server('localhost', 8051, application)
    httpd.handle_request()

if __name__ == '__main__':
    main()

