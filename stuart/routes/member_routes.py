# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

from stuart.models.user import User

member_blueprint = Blueprint(
    'user',
    __name__,
    url_prefix='/users',
    static_folder='../static')


@member_blueprint.route('/')
@login_required
def members():
    """List members."""
    users = User.get_all()
    return render_template('users/members.html', users=users)
