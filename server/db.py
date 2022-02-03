import uuid

from pony import orm


db = orm.Database()


class Owner(db.Entity):
    _table_ = 'owners'

    id = orm.PrimaryKey(int, auto=True)

    name = orm.Required(str)

    surname1 = orm.Required(str)

    surname2 = orm.Optional(str)

    vat = orm.Optional(str, unique=True, index='vat_index')

    address = orm.Required(str)
    

class Contract(db.Entity):
    _table_ = 'contracts'

    id = orm.PrimaryKey(int, auto=True)

    cups = orm.Required(str, unique=True)

    address = orm.Required(str)

    owner = orm.Required(Owner)
    
    portal = orm.Optional(str)


class Invoice(db.Entity):
    _table = 'invoices'

    id = orm.PrimaryKey(int, auto=True)

    contract = orm.Required(Contract)

    owner = orm.Required(Owner)


CONTRACTS = [
    {
        'id': uuid.uuid4().hex,
        'cups': 'ES0363315453020214VA',
        'address': 'Praza León, 334, 6º D (89276) Salgado del Vallès',
        'owner': 'Jack Kerouac',
        'active': True
    },
    {
        'id': uuid.uuid4().hex,
        'cups': 'ES0029968486145694XL',
        'address': 'Paseo Iker, 6, Ático 7º (41140) Los Quesada',
        'owner': 'J. K. Rowling',
        'active': True
    },
    {
        'id': uuid.uuid4().hex,
        'cups': 'ES0023784943500247ZH',
        'address': 'Ronda Javier, 08, 6º A (64874) Vall González',
        'owner': 'Dr. Seuss',
        'active': True
    }
]
