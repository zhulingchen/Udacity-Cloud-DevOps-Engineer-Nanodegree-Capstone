def app(environ, start_response):
	data = b"Hello, World!\nThis is a Gunicorn server!"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])