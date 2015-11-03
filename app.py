import spotify

from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient
import urllib

client = TwilioRestClient()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def inbound_sms():
    response = twiml.Response()
    response.message('Thanks for texting! Searching for your song now.'
                     'Wait to receive a phone call :)')

    song_title = urllib.quote(request.form['Body'])
    from_number = request.form['From']
    to_number = request.form['To']

    client.calls.create(to=from_number, from_=to_number,
                        url='http://sagnew.ngrok.io/call?track={}'
                        .format(song_title))

    return str(response)


@app.route('/call', methods=['POST'])
def outbound_call():
    song_title = request.args.get('track')
    track_url = spotify.get_track_url(song_title)

    response = twiml.Response()
    response.play(track_url)
    return str(response)

app.run(host='0.0.0.0', debug=True)
