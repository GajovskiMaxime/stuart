from stuart.database.surrogate_pk import SurrogatePK
from stuart.extensions import db
from stuart.models.abtract_model import AbstractModel


class SaltModule(SurrogatePK, AbstractModel):
    """A user of the app."""

    __tablename__ = 'salt_module'
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<SaltModule({name!r})>'.format(name=self.name)
