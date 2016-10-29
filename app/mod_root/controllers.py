import datetime

from flask import Blueprint, render_template;

mod_root = Blueprint('root', __name__, url_prefix='/app')

@mod_root.route('/', methods=['GET'])
def root():
    my_datetime = datetime.datetime.now().isoformat()
    print("DATE:", my_datetime)
    return render_template('mod_root/index.html', now_str=my_datetime)
