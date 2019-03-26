import pytest

from secode.cli import encode_secrets
from secode.core import base64_decode, base64_encode


@pytest.mark.parametrize('file_path, file_path_expected', [
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
])
def test_encode_decode(file_path, file_path_expected):
    # encode
    encoded = encode_secrets(file_path)
    with open(file_path_expected) as f:
        expected = f.read()
    
    assert encoded == expected
    
    # decode
    decoded = encode_secrets(file_path_expected, decode=True)
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
