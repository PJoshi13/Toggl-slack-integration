from flask import Flask, request

from urllib import urlencode
from requests.auth import HTTPBasicAuth
import getpass, requests, os, time, datetime, sys, select, termios, tty

app = Flask(__name__)
token = "1e8e441f4cf317c4efc264b84aee1375"
headers = {'content-type': 'application/json'}

@app.route('/toogl start', methods=['GET', 'POST'])
def get_tasks():
	url = 'https://www.toggl.com/api/v8/workspaces/476356/tasks'
	headers = {'content-type': 'application/json'}
	orig   = request.form['text']
	g = requests.GET(url, headers=headers, auth=HTTPBasicAuth(token, 'api_token'))
	import pdb; pdb.set_trace()
	return g.json()

@app.route('/toggl starts', methods=['GET', 'POST'])
def start_task():
    url = 'https://www.toggl.com/api/v8/time_entries/start'
    headers = {'content-type': 'application/json'}
    orig - request.form['text']
    start_time = datetime.datetime.utcnow()
    local_start_time = datetime.datetime.now()

    data = {
        "id":1573236,
        "pid":123,
        "wid":476356,
        "billable": false,
        "start": start_time,
        "duration": -calendar.timegm(time.gmtime()),
        "description":"Meeting with possible clients",
        "tags":["billed"]
        }

    r = requests.get(url, params=data)
    import pdb; pdb.set_trace()
    return p.json()

if __name__ == '__main__':
    app.run(host='104.131.72.152')