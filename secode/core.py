import base64

from ruamel.yaml import RoundTripDumper, YAML, dump


def encode_secrets(file_path, decode=False):
    encoder = base64_decode if decode else base64_encode
    original_payload = read_yaml(file_path)
    encoded_payload = encode(original_payload, encoder)
    content = dump(encoded_payload, Dumper=RoundTripDumper)
    return content


def read_yaml(file_path):
    with open(file_path, 'r') as stream:
        yaml = YAML()
        return yaml.load(stream.read())


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
