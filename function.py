from Client import Client, get_data, write_data


def enter():
    car_plate = input("enter car plate: ")
    client = Client(car_plate)
    current_user = client.add_to_data()
    if current_user == -1:
        for client in get_data('clients.json'):
            if client['plate'] == car_plate:
                current_user = client['id']
                break
    print("succeed")
    return current_user


def show_available_places():
    data = get_data('parking.json')
    floor1 = []
    floor2 = []
    floor3 = []
    floor4 = []
    count = 0
    for places in data:
        places = places['places']
        for i in range(len(places)):
            if count == 0:
                if not places[i]:
                    floor1.append(i + 1)
            if count == 1:
                if not places[i]:
                    floor2.append(i + 1)
            if count == 2:
                if not places[i]:
                    floor3.append(i + 1)
            if count == 3:
                if not places[i]:
                    floor4.append(i + 1)
        count += 1

    print(f"1 floor places {len(floor1)} {floor1}")
    print(f"2 floor places {len(floor2)} {floor2}")
    print(f"3 floor places {len(floor3)} {floor3}")
    print(f"4 floor places {len(floor4)} {floor4}")
    print(f"Total places: {len(floor1) + len(floor4) + len(floor3) + len(floor2)}")


def register_place(user_id):
    try:
        parking_floor = int(input("floor id: "))
        parking_id = int(input('place id: '))
        data = get_data('parking.json')
        if data[parking_floor - 1]['places'][parking_id - 1]:
            print("this place has already taken")
        else:
            data[parking_floor - 1]['places'][parking_id - 1] = True
            client_data = get_data('clients.json')
            new = {
                "id": parking_id,
                "floor": parking_floor
            }
            for client in client_data:
                if client['id'] == user_id:
                    client['places'].append(new)
            write_data('clients.json', client_data)
            print("Registered")

        write_data('parking.json', data)
    except IndexError:
        print("invalid id")


def unregister_place(user_id):
    try:
        is_found = False
        parking_floor = int(input("floor id: "))
        parking_id = int(input('place id: '))
        data = get_data('parking.json')
        clients_data = get_data('clients.json')
        client_places = None
        for client in clients_data:
            if client['id'] == user_id:
                client_places = client['places']
                break
        if data[parking_floor - 1]['places'][parking_id - 1]:
            new = {
                "id": parking_id,
                "floor": parking_floor
            }
            for places in client_places:
                if places == new:
                    data[parking_floor - 1]['places'][parking_id - 1] = False
                    client_places.remove(new)
                    print("Unregistered")
                    is_found = True
                    break
        if not is_found:
            print("this place is not belong to you")
        write_data('clients.json', clients_data)
        write_data('parking.json', data)
    except IndexError:
        print("invalid id")


def show_registered_places(user_id):
    clients_data = get_data('clients.json')
    client_places = None
    for client in clients_data:
        if client['id'] == user_id:
            client_places = client['places']
            break
    if client_places:
        print("==========================================")
        for place in client_places:
            print(f"Place: {place['id']}")
            print(f"Floor: {place['floor']}")
            print("==========================================")
    else:
        print("You have not registered for places yet")
