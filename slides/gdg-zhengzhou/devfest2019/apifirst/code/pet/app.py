import connexion
from flask_cors import CORS


def get_pets_by_id(pet_id: int) -> list:
    return [{
                'name': 'lucky',
                'petType': 'dog',
                'bark': 'woof!'
            }, 
            {
                'name': 'kitty',
                'petType': 'cat',
                'meow': 'meow!'
            },
            {
                'name': 'jack',
                'petType': 'lizard',
                'loveRocks': True
            }][pet_id%3]


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='./')
    app.add_api('spec.yaml', arguments={'title': 'Simple Pet'})
    CORS(app.app)
    app.run()