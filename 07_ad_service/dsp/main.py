from flask import Flask, jsonify, request
from utils import filter_by_geo_and_gender
from default_recs import default_recs
import sys


def create_dsp(port: int, recs):
    dsp = Flask('DSP Service')

    @dsp.route('/ads', methods=['GET'])
    def get_ads():
        user_recs = filter_by_geo_and_gender(recs, request.values['gender'], request.values['geo'])
        return jsonify(user_recs)

    @dsp.route('/ads', methods=['POST'])
    def add_ad():
        recs.append(request.get_json())
        return jsonify({'status': 'ok'})

    dsp.run(port=port)


if __name__ == '__main__':
    portNum = int(sys.argv[1])
    create_dsp(portNum, default_recs[portNum])
