import pytest

from OTP import *


@pytest.mark.parametrize("plain_text, key, expected_encrypted", [
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZXYWVUTSRQPONMLKJIHGFEDCBA", "ZY ZZZZZZZZZZZZZZZZZZZZZZZ"),
    ("hello", "world", "CSBWR")
])
def test_encrypt(plain_text, key, expected_encrypted):
    encrypted = EncryptOneTimePad(plain_text, key)
    assert encrypted == expected_encrypted

@pytest.mark.parametrize("encrypted_text, key, expected_decrypted", [
    ("ZY ZZZZZZZZZZZZZZZZZZZZZZZ", "ZXYWVUTSRQPONMLKJIHGFEDCBA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ("csbwr", "world", "HELLO")
])
def test_decrypt(encrypted_text, key, expected_decrypted):
    decrypted = DecryptOneTimePad(encrypted_text, key)
    assert decrypted == expected_decrypted