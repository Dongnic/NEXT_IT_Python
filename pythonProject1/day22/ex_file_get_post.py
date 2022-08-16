from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return "welcome to flask"

@app.route('/handler_post', methods=['POST'])
def handler_post():
    params = json.loads(request.get_data(), encoding='utf-8')
    if len(params) == 0:
        return 'No parameter'
    params_str = ''
    for key in params.keys():
        params_str += 'key:{}, values:{}<br>'.format(key, params[key])
    return params_str

@app.route('/send_post', methods=['GET'])
def sen_post():
    params = {
        "param1":"test1"
        ,"param2":123
        ,"param3":"한글"
    }
    res = requests.post("http://127.0.0.1:5050/handler_post", data=json.dumps(params))
    return res.text

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return '파일 저장됨'
    else:
        return render_template('file_upload.html')


if __name__=='__main__':
    app.run(port=5050)