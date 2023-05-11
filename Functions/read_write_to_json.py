import json

def write_data(filename, data):
        with open(filename, 'w', encoding = 'utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False)

def read_data(filename):
        with open(filename, 'r') as fp:
                data = json.load(fp)
        return data