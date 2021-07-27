from flask import Flask
from flask_restplus import Api, Resource
from src.server.intance import server

app, api = server.app, server.api

books_db = [
    {'id':0, 'title':'War of the wolrd'},
    {'id':1, 'title':'O Fim da Eternidade'}
]

@api.route('/books')
class BookList(Resource):
    def get(self,):
        return books_db
    def post(self,):
        response = api.payload
        books_db.append(response)
        return response, 200
