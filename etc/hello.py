CONFIG = {
        'mode': 'wsgi',
        'user': 'www-data',
        'group': 'www-data',
        'python': '/usr/bin/python',
        'args': (
            '--bind=0.0.0.0:8080',
            '--workers=2',
            '--timeout=60',
            'hello:wsgi_app',
        ),
}

def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('content-type', 'text/plain')]
    body = 'hello, gunicorn'
    start_response(status, headers)
    return [body]
