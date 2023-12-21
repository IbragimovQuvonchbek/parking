from file_helper import get_data, write_data


def plate_exists(car_plate):
    for client in get_data('clients.json'):
        if client['plate'] == car_plate:
            return True
    return False


class Client:
    id = -1

    def __init__(self, car_plate):
        self.car_plate = car_plate

    def add_to_data(self):
        if not plate_exists(self.car_plate):
            data = get_data(file_path='clients.json')
            self.id = data[-1]['id'] + 1 if data else 1
            new = {
                'id': self.id,
                'plate': self.car_plate,
                'places': []
            }
            data.append(new)
            write_data(file_path='clients.json', data=data)
        return self.id
