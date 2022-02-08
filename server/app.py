from flask import jsonify, request, current_app as app
from pony import orm


# sanity check route
def ping_pong():
    return jsonify('pong!')


@orm.db_session
def contracts(owner_id):
    response_object = {}
    if request.method == 'GET':
        owner_contracts = orm.select(
            contract for contract in app.db_manager.db.Contract
            if contract.owner.id == owner_id
        )
        response_object = [contract.to_dict() for contract in owner_contracts]

    return jsonify(response_object)


def single_contract(contract_id):
    response_object = {}
    return jsonify(response_object)
