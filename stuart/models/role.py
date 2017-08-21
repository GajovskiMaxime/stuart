from stuart.database.others import reference_col
from stuart.database.surrogate_pk import SurrogatePK
from stuart.extensions import db
from stuart.models.abtract_model import AbstractModel


class Role(SurrogatePK, AbstractModel):
    """A role for a user."""

    __tablename__ = 'roles'
    name = db.Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col('users', nullable=True)
    user = db.relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)
