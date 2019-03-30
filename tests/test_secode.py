import pytest

from secode.cli import encode_file
from secode.core import base64_decode, base64_encode, encode_stream

_TEST_FILES = [
    (
        'yamls/test_single.yaml',
        'yamls/test_single_base64.yaml'
    ),
    (
        'yamls/test_multiple.yaml',
        'yamls/test_multiple_base64.yaml'
    ),
    (
        'yamls/test_documents.yaml',
        'yamls/test_documents_base64.yaml'
    ),
]


@pytest.mark.parametrize('file_path, encoded_file_path', _TEST_FILES)
def test_encode_decode_file(file_path, encoded_file_path):
    # encode
    encoded = encode_file(file_path)
    with open(encoded_file_path) as f:
        expected = f.read()

    assert encoded == expected

    # decode
    decoded = encode_file(encoded_file_path, decode=True)
    with open(file_path) as f:
        expected = f.read()

    assert decoded == expected


@pytest.mark.parametrize('file_path, encoded_file_path', _TEST_FILES)
def test_encode_decode_stream(file_path, encoded_file_path):
    # encode
    with open(file_path) as stream:
        encoded = encode_stream(stream)
    with open(encoded_file_path) as f:
        expected = f.read()

    assert encoded == expected

    # decode
    with open(encoded_file_path) as stream:
        decoded = encode_stream(stream, decode=True)
    with open(file_path) as f:
        expected = f.read()

    assert decoded == expected


def test_base64_encode():
    value = '012-abc-,.*-?$#'
    expected = 'MDEyLWFiYy0sLiotPyQj'
    encoded = base64_encode(value)
    assert encoded == expected


def test_base64_decode():
    value = 'MDEyLWFiYy0sLiotPyQj'
    expected = '012-abc-,.*-?$#'
    decoded = base64_decode(value)
    assert decoded == expected
