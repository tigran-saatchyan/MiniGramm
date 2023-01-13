import logging

from flask import Blueprint, render_template, request

from config import POST_PATH
from loader.utils import *
from main.utils import PostHandler

loader_blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    template_folder='templates'
)

logging.basicConfig(filename='log.log', level=logging.INFO)


@loader_blueprint.route('/post')
def create_post_page():
    """
    View to post form
    :return:
    """
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def create_post():
    """
    View to post form getting submitted form data
    :return:
    """
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not (picture or content):
        return 'Все поля должны быть заполнены'

    path = save_picture(picture)
    if not path:
        logging.info(
            f'{picture.filename} - не подходящий файл'
        )
        return f'Файл {picture.filename} не является изображением ' \
               f'либо имеет не поддерживаемый формат'

    post_handler = PostHandler(POST_PATH)

    last_post = {'pic': path, 'content': content}
    post_handler.add_post(last_post)

    return render_template(
        'post_uploaded.html',
        picture=path,
        content=content
    )
