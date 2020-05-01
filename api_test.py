import requests

url = 'http://0.0.0.0:5000/classify'


client_data = {
    'income': 43756.0566049069,
    'age': 63.9717958411202,
    'loan': 1622.72259832146,
}

if __name__ == '__main__':
    r = requests.post(url=url, json=client_data)
    print(r.text)
