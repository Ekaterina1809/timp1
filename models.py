import datetime, re
from app import db

def slugify(s)
    return re.sub('[^\w]+','-',s).lower()

class Entry(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    slug=db.Column(db.String(100),unique=True)  #заголовок
    body=db.Column(db.Text)                     #содержимое
    create_timestamp=db.Column(db.DataTime, datetime=datetime.datetime.now)
    modified_timestamp = db.Column(db.DataTime, datetime=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self,*args, **kwargs):             #автоматически переопределяет таблицы в соответствии с заголовками
        super(Entry,self).__init(*args,**kwargs)
        self.generate_slug

    def generate_slug(self):                        #
        self.slug=''
        if self.title:
            self.slug=slugify(self.title)

    def __str__(self):                              #полезно при отладке
        return 'Entry: %s>' %self.title
