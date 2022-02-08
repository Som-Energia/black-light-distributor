from flask import Flask
from flask_cors import CORS

from .db import Database


def build_app(database_name='database.sqlite', args=None):
    try:
        manager = Database()
        manager.define_models()
        manager.db.bind(provider='sqlite', filename=database_name, create_db=True)
        manager.db.generate_mapping(create_tables=True)

    except Exception as e:
        raise e
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.db_manager = manager

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    from .app import ping_pong, contracts, single_contract
    app.add_url_rule(
        rule='/ping',
        view_func=ping_pong
    )
    app.add_url_rule(
        rule='/owners/<owner_id>/contracts',
        view_func=contracts,
        methods=['GET']
    )
    app.add_url_rule(
        rule='/contracts/<contract_id>',
        view_func=single_contract,
        methods=['PUT', 'DELETE']
    )

    return app
