import os
from pyairtable import Api

class BookReview:
    def __init__(self):
        self.api = Api(os.environ['AIRTABLE_KEY'])
        self.table = self.api.table('appkUrlrjwHudezoV', 'tblqq5L1PAYh6rGc0')

    def get_book_ratings(self, sort="ASC", max_records=10):
        if not sort:
            return self.table.all(max_records=max_records)
        elif sort == "ASC":
            rating = ["Rating"]
        elif sort == "DESC":
            rating = ["-Rating"]
        
        table = self.table.all(sort=rating, max_records=max_records)
        return table

    def add_book_rating(self, book_title, book_rating, notes=None):
        fields = {'Book': book_title, 'Rating': book_rating, 'Notes': notes}
        self.table.create(fields=fields)


if __name__ == '__main__':
    br = BookReview()
    # br.add_book_rating('Infinite Jest', 7.0)
    get_book_ratings = br.get_book_ratings(sort="DESC", max_records=1)
    print(get_book_ratings)