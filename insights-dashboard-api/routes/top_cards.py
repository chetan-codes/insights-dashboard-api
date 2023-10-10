from flask import Blueprint, jsonify


top_cards = [

    {
       "bgcolor": 'success',
        "icon": 'bi bi-coin',
        "subtitle": 'AR Balance',
        "title": '$17,389,313'
    },
    {
        "bgcolor": 'danger',
        "icon": 'bi bi-wallet',
        "subtitle": 'Average DSO last 12 months',
        "title": '34'
    },
    {
        "bgcolor": 'warning',
        "icon": 'bi bi-person',
        "subtitle": 'Customers with Invoices last 12 months',
        "title": '1071'
    },
    {
        "bgcolor": 'primary',
        "icon": 'bi bi-bank',
        "subtitle": 'Collections last month',
        "title": '$5,452,941'
    }
]

top_cards_routes = Blueprint('top_cards', __name__)

# Define route for top_cards API
@top_cards_routes.route('/api/top_cards', methods=['GET'])
def get_top_cards():
    # Return top_cards as JSON
    return jsonify(top_cards)