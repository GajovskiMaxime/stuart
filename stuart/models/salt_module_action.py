from stuart.database.others import reference_col
from stuart.database.surrogate_pk import SurrogatePK
from stuart.extensions import db
from stuart.models.abtract_model import AbstractModel


class SaltModuleAction(SurrogatePK, AbstractModel):
    """A user of the app."""

    __tablename__ = 'salt_module_action'
    name = db.Column(db.String(80), unique=True, nullable=False)
    salt_module_id = reference_col('salt_module', nullable=False)
    salt_module = db.relationship('SaltModule', backref='salt_module_actions')

    def __init__(self, salt_module_id, name, **kwargs):
        """Create instance."""
        db.Model.__init__(
            self, name=name, salt_module_id=salt_module_id, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<SaltModule({name!r})>'.format(name=self.name)
