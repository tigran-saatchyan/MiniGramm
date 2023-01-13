import json
import logging
from json import JSONDecodeError

logging.basicConfig(filename='log.log', level=logging.INFO)


class PostHandler:
    """
    Post Handling class
    """

    def __init__(self, path):
        """
        Path initiation
        :param path: - json file path
        """
        self.path = path

    def load_post(self):
        """
        Load posts method
        :return:
        """
        posts = []
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            logging.info('Ошибка загрузки файла')
        return posts

    def search_post(self, substr):
        """
        Search post method
        :param substr:
        :return:
        """
        posts = []
        for post in self.load_post():
            if substr.lower() in post['content'].lower():
                posts.append(post)
        return posts

    def add_post(self, post):
        """
        Add post method
        :param post: - post to be added in posts.json
        :return:
        """
        posts = self.load_post()
        posts.append(post)
        self.save_post(posts)

    def save_post(self, posts):
        """
        Saving posts to json by rewriting old one
        :param posts: - posts to save in posts.json
        :return:
        """
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file)
        except JSONDecodeError:
            logging.info('Ошибка сохранения файла')

        return posts
