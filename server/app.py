from flask import Flask, jsonify, request
from flask_cors import CORS
from pony import orm
from db import db


def build_app(args=None):
    try:
        db.bind({
            'provider': 'postgres',
            'host': 'localhost',
            'port': 5432,
            'database': '',
            'user': '',
            'password': ''
        })
        db.generate_mapping(create_tables=True)

    except Exception as e:
        raise e
    app = Flask(__name__)
    app.config.from_object(__name__)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    return app

app = build_app()

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/owner/<owner_id>/contracts', methods=['GET', 'POST'])
@orm.db_session
def contracts():
    response_object = {}
    return jsonify(response_object)


@app.route('/contracts/<contract_id>', methods=['PUT', 'DELETE'])
def single_contract(contract_id):
    response_object = {}
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()