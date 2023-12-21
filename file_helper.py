from json import load, dump, JSONDecodeError


def get_data(file_path):
    try:
        with open(file_path) as f:
            data = load(f)
        return data
    except (FileNotFoundError, JSONDecodeError):
        with open(file_path, 'w') as f:
            dump([], f)
        return []


def write_data(file_path, data):
    with open(file_path, 'w') as f:
        dump(data, f, indent=4)
