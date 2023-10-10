from flask import Blueprint, jsonify

# List of Dictionaries with data
top_customers = [

    {
      "name": 'Gerlach, McClure and Haley' ,
      "arBalance": '$610,427',
      "percentOfTotalAr": '4%',
      "creditLimit": '$300,000'
    },
    {
      "name": 'Bogan-Feeney' ,
      "arBalance": '$531,877',
      "percentOfTotalAr": '3%',
      "creditLimit": '$450,000'
    },
    {
      "name": 'Von and Sons' ,
      "arBalance": '$893,209',
      "percentOfTotalAr": '5%',
      "creditLimit": '$900,000'
    },
    {
      "name": '	McKenzie Group' ,
      "arBalance": '$477,523',
      "percentOfTotalAr": '3%',
      "creditLimit": '$650,000'
    },
    {
      "name": 'Schuppe Ltd' ,
      "arBalance": '$302,121',
      "percentOfTotalAr": '2%',
      "creditLimit": '$475,000'
    },
    {
      "name": 'Lehner Inc' ,
      "arBalance": '$255,418',
      "percentOfTotalAr": '1%',
      "creditLimit": '$450,000'
    }

]

# Create blueprint for top customers route. 
top_customers_routes = Blueprint('top_customers', __name__)

# Define route for top_customers API
@top_customers_routes.route('/api/top_customers', methods=['GET'])
def get_top_customers():
    # Return top_customers as JSON
    return jsonify(top_customers)