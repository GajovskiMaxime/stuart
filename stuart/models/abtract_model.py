from stuart.database.crud_mixin import CRUDMixin
from stuart.extensions import db


class AbstractModel(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True
