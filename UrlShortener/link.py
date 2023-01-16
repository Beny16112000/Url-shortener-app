from ..models import UrlShortenerModel
from .. import db


# Url Shortener Class


class Link:

    def __init__(self, user, url, shorter, click):
        self.user = user
        self.url = url
        self.shorter = shorter
        self.click = click


    def create(self):
        check = self.check()
        if check is True:
            url = UrlShortenerModel(user=self.user,url=self.url,shorter=self.shorter,click=self.click)
            db.session.add(url)
            db.session.commit()
            return True
        else:
            return check


    def check(self):
        url = UrlShortenerModel.query.filter_by(shorter=self.shorter).first()
        if url:
            return 'Shorter Url Already exist'
        else:
            return True



class LinkData:

    def getall(self, user):
        urls = UrlShortenerModel.query.filter_by(user=user)
        return urls


    def redirector(self, url, isUser):
        urlTo = UrlShortenerModel.query.filter_by(shorter='http://127.0.0.1:5000/shorti/'+url).first()
        if isUser is False:
            return urlTo 
        else:
            addClick = urlTo.click + 1
            urlTo.click = addClick
            db.session.commit()
            return urlTo


