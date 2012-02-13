import os

# My random WSGI playings around.
from wsgiref.simple_server import make_server

from mako.template import Template
from mako.lookup import TemplateLookup

from cgi import parse_qs
from cgi import escape

# This is called application because if you want to use this
# with mod_wsgi it is requied to be named application

def application(environ, start_response):
    here = os.getcwd()

    # setup our mako stuff and load index.html
    template_path = os.path.join(here,'templates')
    lookup = TemplateLookup(directories=[template_path])
    template = Template(filename=os.path.join(template_path,'index.html'))

    d = parse_qs(environ['QUERY_STRING'])
    args = dict(
        age=escape(d.get('age',[''])[0]),
        name=escape(d.get('name',[''])[0]),
        cb=[escape(c) for c in d.get('cb',[])]
    )

    response_body = [str(template.render(**args))]
    # response body is an interable, each item is returns from the
    # serve. be sure to always wrap single responses to avoid
    # iterating over every character in a single response string

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(sum(len(i) for i in response_body)))
    ]

    start_response(status, response_headers)
    return response_body

def main():
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()

if __name__ == '__main__':
    main()

