from flask import Flask, request, jsonify
import uuid
import datetime
import time
import pika
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
    send_to_MQ(d)
    return jsonify(d)


if __name__ == '__main__':
    app.run()


def send_to_MQ(message):
    '''
    Sends an acknowledgement message to the exchange that pygbq has finished
    running.
    '''
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='RABBIT'))
    channel = connection.channel()
    channel.exchange_declare(
        exchange='0.0.0.0:15672',
        exchange_type='fanout')
    channel.basic_publish(exchange='PYGBQ_EXCHANGE',
                          routing_key='',
                          body=message)

    print " [x] Sent message"
    connection.close()
