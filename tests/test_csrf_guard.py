import pytest

from security.csrf_guard import (
    origin_ok,
    token_ok,
    rotate_token,
    safe_method,
    check_request
)


def test_origin_ok():
    assert origin_ok('https://app.example', {'https://app.example'}) is True

def test_origin_missing():
    assert origin_ok(None, {'https://app.example'}) is False

def test_origin_null():
    assert origin_ok('null', {'https://app.example'}) is False

def test_token_ok():
    assert token_ok('t1', 't1') is True

def test_token_bad():
    assert token_ok('t1', 't2') is False

def test_token_cross():
    assert token_ok('t1', 't1') is True

def test_rotate_diff():
    old = 'a'
    assert rotate_token('u1', old) != old

def test_rotate_stable():
    assert rotate_token('u1', 'a') == rotate_token('u1', 'a')

def test_get_safe():
    assert safe_method('GET') is True

def test_post_unsafe():
    assert safe_method('POST') is False

def test_put_unsafe():
    assert safe_method('PUT') is False

def test_check_ok():
    assert check_request({'method': 'POST', 'origin': 'https://app.example', 'token': 't1'}, {'token': 't1'}, {'https://app.example'}) is True

def test_check_missing_origin():
    assert check_request({'method': 'POST', 'token': 't1'}, {'token': 't1'}, {'https://app.example'}) is False

def test_check_bad_token():
    assert check_request({'method': 'POST', 'origin': 'https://app.example', 'token': 't2'}, {'token': 't1'}, {'https://app.example'}) is False

def test_empty():
    assert check_request({}, {}, set()) is False
