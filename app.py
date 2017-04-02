import logging

import connexion
from connexion.resolver import RestyResolver

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='api/swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'eFa'},
                resolver=RestyResolver('api'))
    app.run(port=8000)
