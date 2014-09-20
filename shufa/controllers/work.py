# coding: utf-8
from flask import render_template, Blueprint
from ..models import Work

bp = Blueprint('work', __name__)


@bp.route('/<int:uid>')
def view(uid):
    """首页"""
    work = Work.query.get_or_404(uid)
    return render_template('work/view.html', work=work)
