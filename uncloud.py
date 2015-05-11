from bottle import Bottle
from controlpanel.routes import battery, cpu, clockspeed
app = Bottle()

app.route('/battery', ['GET'], battery)
app.route('/cpu', ['GET'], cpu)
app.route('/clockspeed', ['POST'], clockspeed)
app.run(reloader=False, debug=True, host='localhost', port=8080)
