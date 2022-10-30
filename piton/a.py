from http.server import HTTPServer, BaseHTTPRequestHandler
from pylsl import StreamInlet, resolve_stream, StreamOutlet, StreamInfo
import random
import math

#streams = resolve_stream('type', 'EEG')
#inlet = StreamInlet(streams[0])

info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        BaseHTTPRequestHandler.end_headers(self)
    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)
    def do_GET(self):
        #chunk, timestamps = inlet.pull_chunk()
        broj = math.floor(random.random()*4)
        #if timestamps:
        self.write_response(str(broj).encode('utf-8'))
        #outlet.push_sample(broj)
        #print("Vrati id akcije iz poslednjeg elementa chunka")

httpd = HTTPServer(('192.168.0.18', 8008), SimpleHTTPRequestHandler)
httpd.serve_forever()
