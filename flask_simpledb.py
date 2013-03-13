from flask import _app_ctx_stack as stack

class SimpleDb(object):
    def __init__(self, store = {}):
        self.store = store
        self.store["posts"] = []

    def addPost(self, title, content):
        posts = self.store['posts']
        posts.append({'id': len(posts), 'title': title, 'content': content})
        print posts
        self.store['posts'] = posts

    def getPosts(self):
        print self.store["posts"]
        return self.store["posts"]

    def getPost(self, theId):
        return self.store["posts"][theId]
