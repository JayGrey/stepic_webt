def format_body(query):
    result = '';
    for token in query.split('&'):
        result += token
        result += '\r\n'
    return  result


def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('content-type', 'text/plain')]
    body = ''

    if 'QUERY_STRING' in environ:
        body = format_body(environ['QUERY_STRING'])

    start_response(status, headers)
    return [body]
