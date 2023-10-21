import connexion
import book_review

from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yaml")

# def get_records(count=None, sort=None):
#     books = book_review.get_all_records(count=count, sort=sort)
#     return {"books": books}


# def post_add_record():
#     data = connexion.request.json
#     if 'Book' not in data or 'Rating' not in data:
#         return {"message": "Bad request, missing 'Book' or 'Rating' in the request body"}, 400
#     success = book_review.add_record(data)
#     if success:
#         return {"message": "Record added successfully"}, 200
#     else:
#         return {"message": "Failed to add record"}, 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)

