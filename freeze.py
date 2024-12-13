from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

# @freezer.register_generator
# def product_details():  # endpoint defaults to the function name
#    # `values` dicts
#    yield {'product_id': '1'}
#    yield {'product_id': '2'}


if __name__ == '__main__':
    freezer.freeze()
