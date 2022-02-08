import uuid

from pony import orm


class Database:

    def __init__(self):
        self.db = orm.Database()

    def define_models(self):

        class Owner(self.db.Entity):
            _table_ = 'owners'

            id = orm.PrimaryKey(int, auto=True)

            name = orm.Required(str)

            surname1 = orm.Required(str)

            surname2 = orm.Optional(str)

            vat = orm.Optional(str, unique=True, index='vat_index')

            address = orm.Required(str)

            contracts = orm.Set('Contract')

            invoices = orm.Set('Invoice')

        class Contract(self.db.Entity):
            _table_ = 'contracts'

            id = orm.PrimaryKey(int, auto=True)

            cups = orm.Required(str, unique=True)

            address = orm.Required(str)

            owner = orm.Required(Owner, cascade_delete=False)

            invoices = orm.Set('Invoice')

        class Invoice(self.db.Entity):
            _table = 'invoices'

            id = orm.PrimaryKey(int, auto=True)

            contract = orm.Required(Contract, cascade_delete=False)

            owner = orm.Required(Owner, cascade_delete=False)

            total = orm.Required(int)

            desc = orm.Required(str)

            other_info = orm.Optional(str)
