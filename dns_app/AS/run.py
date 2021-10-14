from flask import Flask, request,redirect
import pickle
app = Flask(__name__)


@app.route('/')
def index():
    return 'Authoritative Server'

@app.route('/registration', method = ['GET'])
def registration():
    _type = request.args.get('TYPE')
    _name = request.args.get('NAME')
    _value = request.args.get('VALUE')
    _ttl = request.args.get('TTL')
    temp_key = 'TYPE='+str(_type)+'\n'+'NAME='+str(_name)
    temp_value = 'TYPE='+str(_type)+'\n'+'NAME='+str(_name)+'\n'+'VALUE='+str(_value)+'\n'+'TTL='+str(_ttl)
    record_dict = open("record.pkl","wb")            #use pickle to save locally
    temp_dict = pickle.load(record_dict)
    temp_dict[temp_key] = temp_value
    pickle.dump(temp_dict, record_dict)
    record_dict.close()
    return  201                                      #for the respond of FS server

@app.route('/query',method = ['GET'])
def query():
    _type = request.args.get('TYPE')
    _name = request.args.get('NAME')
    _fs_port = request.args.get('fs_port')
    _number = request.args.get('number')
    temp_key = 'TYPE='+str(_type)+'\n'+'NAME='+str(_name)
    with open("record.pkl","rb") as record_dict:            #use pickle to save locally
        temp_dict = pickle.load(record_dict)
        if temp_key in temp_dict:
            querystring = temp_dict[temp_key]
            querystring = querystring.replace('\n','&')
            url = 'http://localhost:8080'+'fibonacci/?'+str(querystring)+'&number='+str(_number)+"&fs_port="+str(_fs_port)
            return redirect(url)
    return 400
app.run(host='0.0.0.0',
        port=53533,
        debug=True)
