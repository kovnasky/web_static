def app (environ, start_responce):
        status = '200 OK'
        responce_headers = [('content-type', 'text/plain')]
        start_responce(status, responce_headers)
        resp = environ['QUERY_STRING'].split("&")
        resp = [item+ "\r\n" for item in resp]
        return resp
