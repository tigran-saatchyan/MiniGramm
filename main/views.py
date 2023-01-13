import logging

from flask import Blueprint, render_template, request

from config import POST_PATH
from main.utils import PostHandler

main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    template_folder='templates'
)

logging.basicConfig(filename='log.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    """
    Index page
    :return:
    """
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    """
    Search handling view
    :return:
    """
    post_handler = PostHandler(POST_PATH)
    substr = request.args.get('s')
    logging.info(f'Поиск: {substr}')
    posts = post_handler.search_post(substr)

    return render_template('post_list.html', posts=posts, substr=substr)
