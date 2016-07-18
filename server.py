#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

from checkEmail import checkEmailExists

PORT = 2304

class JSONRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):

        #send response code:
        self.send_response(200)
        #send headers:
        self.send_header("Content-type", "application/json")
        # send a blank line to end headers:
        self.wfile.write("\r\n")

        try:
            # output = open("." + "/" + self.path[1:] + ".json", 'r').read()
            output = checkEmailExists( self.path[1:] )
        except Exception:
            output = json.dumps({'success': '', 'error':'Something is wrong', 'data':''})
        self.wfile.write(output)

server = HTTPServer(("0.0.0.0", PORT), JSONRequestHandler)
server.serve_forever()
