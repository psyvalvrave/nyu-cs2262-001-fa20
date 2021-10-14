from flask import Flask, request, redirect
import json
app = Flask(__name__)


@app.route('/')
def index():
    return 'Fibonacci Server'

@app.route('/register/<body>', methods=['GET']) #retrieve info from query string
def register(body):        
    content = request.get_json()
    load = json.loads(content)
    hostname = load["hostname"]
    ip = load["ip"]
    as_ip = load["as_ip"]
    as_port = load["as_port"]
    register_url = 'http://'+str(as_ip)+':'+'53533/'+'registration?TYPE=A&NAME='+str(hostname)+'&Value='+str(ip)+'&TTL=10'
    return redirect(register_url) #communicate with other server
    
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    while True:                  #error handler to see input is int or not
        try:
            key = int(request.args.get('number'))
            return key,200
            break
        except ValueError:
            return 400
app.run(host='0.0.0.0',
        port=9090,
        debug=True)
