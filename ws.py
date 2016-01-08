#!/usr/bin/env python
import web


urls = (
    '/say_hello', 'say_hello'
)

app = web.application(urls, globals())

class say_hello:        
    def GET(self):
        return "hello from container"

if __name__ == "__main__":
    app.run()