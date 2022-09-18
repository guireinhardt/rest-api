from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [{
        'hotel_id': 'alpha',
        'nome':'Alpha Hotel',
        'estrelas':4.3,
        'diaria':420.65,
        'cidade':'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome':'Bravo Hotel',
        'estrelas':3.2,
        'diaria':369.45,
        'cidade':'São Paulo'
    },
    {
        'hotel_id': 'charlie',
        'nome':'Charlie Hotel',
        'estrelas':4.9,
        'diaria':1025.59,
        'cidade':'Sergipe'}]




class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome')
    arguments.add_argument('estrelas')
    arguments.add_argument('diaria')
    arguments.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self,hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'mensagem': 'Hotel não encontrado'},404
    def post(self,hotel_id):
        
        dados = Hotel.arguments.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel,200
    def put(self,hotel_id):
        dados = Hotel.arguments.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #ok
        hoteis.append(novo_hotel)
        return novo_hotel, 201 # criado
    def delete(self,hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'mensagem':'Hotel deletado'}