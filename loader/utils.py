from config import UPLOAD_FOLDER


def save_picture(picture):
    """
    Saving picture
    :param picture: - picture object
    :return:
    """
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ('jpg', 'png', 'bmp'):
        return

    picture.save(f'./{UPLOAD_FOLDER}/{filename}')
    return f'{UPLOAD_FOLDER}/{filename}'
