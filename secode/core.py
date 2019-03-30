import base64
import sys

from ruamel.yaml import RoundTripDumper, YAML, dump_all


def encode_secrets(file_path, decode=False):
    encoder = base64_decode if decode else base64_encode
    original_payload = read_yaml(file_path)
    encoded_payload = []
    for document in original_payload:
        encoded_payload.append(encode(document, encoder))
    return dump_all(encoded_payload, Dumper=RoundTripDumper)


def read_yaml(file_path):
    with open(file_path, 'r') as stream:
        yaml = YAML()
        docs = yaml.load_all(stream.read())
        for doc in docs:
            yield doc


def encode(payload, encoder):
    if 'items' in payload:
        for i, item in enumerate(payload['items']):
            payload['items'][i] = encode(item, encoder)
    elif payload.get('kind') == 'Secret':
        for key in payload['data']:
            payload['data'][key] = encoder(payload['data'][key])
    else:
        raise ValueError('Invalid K8S Secret file format')
    return payload


# Utils

def base64_encode(value):
    payload = bytes(str(value).encode())
    return base64.b64encode(payload).decode('utf-8')


def base64_decode(payload):
    value = base64.b64decode(payload).decode('utf-8')
    return downcast(value)


def downcast(value):
    if value.isnumeric():
        return int(value)
    try:
        return float(value)
    except:
        pass
    return value
