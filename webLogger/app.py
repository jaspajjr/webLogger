from flask import Flask, request, jsonify
import uuid
import datetime
import time
app = Flask(__name__)


@app.route('/')
def logger():
    start_time = time.time()
    day_of_week = datetime.datetime.today().weekday()
    referrer = request.referrer
    user_agent = request.headers.get('User-Agent')
    session_id = uuid.uuid4()
    session_information = [session_id, start_time, day_of_week, referrer,
                           user_agent]
    d = {'info': session_information}
    return jsonify(d)


if __name__ == '__main__':
    app.run()
