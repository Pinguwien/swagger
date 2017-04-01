import logging

import connexion
from connexion.resolver import RestyResolver

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('efa-api.yaml', arguments={'title': 'eFa'},
                resolver=RestyResolver('api'))
    app.run(port=8000)
