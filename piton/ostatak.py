
import eventlet
import socketio
import threading




sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

mojsid = False

@sio.event
def connect(sid, environ):
    mojsid = sid
    print('EVO GA CONNECT ')
    print('connect ', sid)


@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('EVO GA DISCONNECT ')
    print('disconnect ', sid)

def asinh():
    threading.Timer(0.1, asinh).start()
    print("EMUPD")
    if mojsid:
        sio.emit('update', {'broj': broj}, room=mojsid)
    


if __name__ == '__main__':
    asinh()
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

