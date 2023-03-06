def say_hello(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = 'Hello from Gunicorn'.encode('utf-8')
    return [text]
