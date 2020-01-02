def wsgi_application(environ, start_response):

    query = environ['QUERY_STRING']
    params = query.split('&')
    body = bytes('\n'.join(params), encoding='utf-8')

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    
    start_response(status, headers)
    return [body]