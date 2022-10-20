from flask import Flask, jsonify
from user_info import get_user_info
from auction import do_auction
import requests

DEFAULT_PORT = 5001

DSP_URLS = [
    'http://localhost:5002/ads',
    'http://localhost:5003/ads',
]


def create_ssp(port: int = DEFAULT_PORT):
    ssp = Flask('SSP Service')

    @ssp.route('/recs')
    def get_recs():
        recs = []
        user = get_user_info()
        for url in DSP_URLS:
            resp = requests.get(url + '?gender={}&geo={}'.format(user['gender'], user['geo']))
            recs += resp.json()
        return jsonify(do_auction(recs))

    ssp.run(port=port)


if __name__ == '__main__':
    create_ssp()
