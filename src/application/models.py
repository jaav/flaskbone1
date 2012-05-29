"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db


class Searches(db.Model):
    """Searches Model"""
    search_word = db.StringProperty(required=True)
    search_result_ids = db.ListProperty(db.Key)

class SearchResults(db.Model):
    """Search Results"""
    url = db.StringProperty(required=True)
    result = db.TextProperty(required=False)

