from flask import Flask, request, render_template
import uuid
import json
import datetime
import time
import pika
app = Flask(__name__)


def send_to_MQ(message):
    '''
    Sends an acknowledgement message to the exchange that pygbq has finished
    running.
    '''
    body = json.dumps(message)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='RABBIT'))
    channel = connection.channel()
    channel.exchange_declare(
        exchange='EXAMPLE',
        exchange_type='fanout')
    channel.basic_publish(exchange='EXAMPLE',
                          routing_key='',
                          body=body)

    print " [x] Sent message"
    connection.close()


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
    send_to_MQ(d)
    return render_template('layout.html')


@app.route('/foo')
def foo():
    print 'foo'
    return "Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
