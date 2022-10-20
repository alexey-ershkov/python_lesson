from flask import Flask
from utils import get_single_rec_html, wrap_with_global_styles
import requests

DEFAULT_PORT = 5000
SSP_URL = 'http://localhost:5001'
GET_RECS_URL = SSP_URL + '/recs'


def create_client(port: int = DEFAULT_PORT):
    client = Flask('Client')

    @client.route('/')
    def get_page_with_ads():
        resp = requests.get(GET_RECS_URL)
        recs = resp.json()
        if len(recs) == 0:
            return wrap_with_global_styles('No recs')

        html_ads = ''
        for rec in recs:
            html_ads += get_single_rec_html(rec)
        return wrap_with_global_styles(html_ads)

    client.run(port=port)


if __name__ == '__main__':
    create_client()
