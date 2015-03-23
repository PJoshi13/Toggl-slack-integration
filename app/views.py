from flask import Flask, request

from urllib import urlencode
from requests.auth import HTTPBasicAuth
from PyToggl import PyToggl
import getpass, requests, os, time, datetime, sys, select, termios, tty
pytoggl = PyToggl('1e8e441f4cf317c4efc264b84aee1375')

app = Flask(__name__)
token = "1e8e441f4cf317c4efc264b84aee1375"
headers = {'content-type': 'application/json'}

@app.route('/toggl start', methods=['GET', 'POST'])
def get_tasks():
	url = 'https://www.toggl.com/api/v8/workspaces/476356/tasks'
	headers = {'content-type': 'application/json'}
	orig   = request.form['text']
	g = requests.GET(url, headers=headers, auth=HTTPBasicAuth(token, 'api_token'))
	import pdb; pdb.set_trace()
	return g.json()
def send_data(key, params=None, data=None):
    '''
    Use the api to send data.
    params: A dictionary that will be urlencoded
    Returns a dictionary.
    '''
    headers = {"Content-Type": "application/json"}
    key = token

    # JSON Encode the data dict
    data=simplejson.dumps(data)
    with session(headers=headers) as r:
        response = r.post(api(key), data=data)
        content = response.content
        if response.ok:
            json = simplejson.loads(content)
            return json["data"]
        else:
            exit("Please verify your login credentials...")

@app.route('/toggl start', methods=['GET', 'POST'])
def start_task():
    url = 'https://www.toggl.com/api/v8/time_entries/start'
    headers = {'content-type': 'application/json'}

    start_time = datetime.datetime.utcnow()
    local_start_time = datetime.datetime.now()

    data = {
        "start": start_time.isoformat(),
        "stop": "null",
        "description": orig}

    # If task Id was specified, add it to the data dict
    if taskID:
        data["task"] = {"id":taskID}

    # Add to time_entry key
    data = {"time_entry" : data }


    send_data("time_entries", data=data)

    p = requests.POST(url, headers=headers, auth=HTTPBasicAuth(token, 'api_token'))
    import pdb; pdb.set_trace()
    return p.json()
def new_time_entry(description, taskID=False):
                    
    # Get the current time and store it. Then pause until the user
    # says they are finished timing the task. Get the time they stopped
    # the timer, subtract it from the start_time, and store the difference
    # in seconds as the duration.
    #start_time = datetime.datetime.now()
    start_time = datetime.datetime.utcnow()
    local_start_time = datetime.datetime.now()

    # Let user know the timer has started, and wait for them to press
    # Enter to stop it.
    timer_start_print(description, local_start_time)

    try:
        raw_input()
    except (KeyboardInterrupt, SystemExit):
        # Break out of main While loop, go back to menu.
        print "\nTimer cancelled. Returning to main menu...\n"
        return

    print "Sending data..."

    end_time = datetime.datetime.utcnow()
    time_difference = (end_time - start_time).seconds


    # Data passed to the request

    print "Success."

if __name__ == '__main__':
    app.run(host='104.131.72.152')