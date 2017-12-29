import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fp:
        data = json.load(fp)

    return data


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(pretty_print_json(load_data('alco_shops.json')))
