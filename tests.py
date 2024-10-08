""" this module is for all the tests in order to make sure the ciphers are working"""


import pytest
from one_time_pad import decrypt_one_time_pad, encrypt_one_time_pad
from caesar import caesar_encryption, caesar_decryption
from vigenere import *

#Tests for One-Time Pad encryption and decryption.

@pytest.mark.parametrize(
    "plain_text, key, expected_encrypted",
    [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZXYWVUTSRQPONMLKJIHGFEDCBA", "ZY ZZZZZZZZZZZZZZZZZZZZZZZ"),
        ("hello", "world", "CSBWR"),
    ]
)
def test_encrypt_otp(plain_text, key, expected_encrypted):
    """Test encryption using the One-Time Pad cipher.

    Args:
        plain_text (str): The plaintext to be encrypted.
        key (str): The key used for encryption.
        expected_encrypted (str): The expected encrypted result.
    """
    encrypted = encrypt_one_time_pad(plain_text, key)
    assert encrypted == expected_encrypted


@pytest.mark.parametrize(
    "encrypted_text, key, expected_decrypted",
    [
        ("ZY ZZZZZZZZZZZZZZZZZZZZZZZ", "ZXYWVUTSRQPONMLKJIHGFEDCBA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        ("csbwr", "world", "HELLO"),
    ]
)
def test_decrypt_otp(encrypted_text, key, expected_decrypted):
    """Test decryption using the One-Time Pad cipher.

    Args:
        encrypted_text (str): The text to be decrypted.
        key (str): The key used for decryption.
        expected_decrypted (str): The expected decrypted result.
    """
    decrypted = decrypt_one_time_pad(encrypted_text, key)
    assert decrypted == expected_decrypted


@pytest.mark.parametrize(
    "plain_text, key",
    [
        ("HELLO", "WORLDX"),  # Length of key is longer than plain_text
        ("ABCDEFGHI", "XYZ"),  # Length of key is shorter than plain_text
    ]
)
def test_encrypt_otp_length_mismatch(plain_text, key):
    """Test encryption length mismatch raises ValueError.

    Args:
        plain_text (str): The plaintext to be encrypted.
        key (str): The key used for encryption.
    """
    with pytest.raises(ValueError, match="secret and key are not the same length"):
        encrypt_one_time_pad(plain_text, key)


@pytest.mark.parametrize(
    "encrypted_text, key",
    [
        ("HELLO", "WORLDX"),  # Length of key is longer than encrypted_text
        ("ABCDEFGHI", "XYZ"),  # Length of key is shorter than encrypted_text
    ]
)
def test_decrypt_otp_length_mismatch(encrypted_text, key):
    """Test decryption length mismatch raises ValueError.

    Args:
        encrypted_text (str): The text to be decrypted.
        key (str): The key used for decryption.
    """
    with pytest.raises(ValueError, match="secret and key are not the same length"):
        decrypt_one_time_pad(encrypted_text, key)

# END OF OTP TESTS

# Tests for Caesar cipher 

    @pytest.mark.parametrize(
    "plain_text, key, expected_encrypted",
    [
        ("I love cryptography", "i", "QHTWCMHKZFXAWOZIXPF"),
        ("hello", "w", "C GGJ"),
    ]
)
    def test_encrypt_caesar(plain_text, key, expected_encrypted):
        """Test encryption using the Caesar cipher.

        Args:
            plain_text (str): The plaintext to be encrypted.
            key (str): The key used for encryption.
            expected_encrypted (str): The expected encrypted result.
        """
        encrypted = caesar_encryption(plain_text, key)
        assert encrypted == expected_encrypted


    @pytest.mark.parametrize(
    "encrypted_text, key, expected_decrypted",
    [
        ("QHTWCMHKZFXAWOZIXPF", "i","I love cryptography"),
        ("hello", "w", "C GGJ"),
    ]
)
    def test_encrypt_caesar(plain_text, key, expected_encrypted):
        """Test decryption using the Caesar cipher.

        Args:
            plain_text (str): The plaintext to be encrypted.
            key (str): The key used for encryption.
            expected_encrypted (str): The expected encrypted result.
        """
        encrypted = caesar_decryption(plain_text, key)
        assert encrypted == expected_encrypted

# TESTS FOR VIGENERE CIPHER
def test_create_key():
    original_message = "THIS IS A SECRET MESSAGE"
    keyword = "HIDE THIS"
    key = create_key(original_message, keyword)
    assert key == "HIDE THISHIDE THISHIDE T"

def test_vigenere_encryption():
    original_message = "THIS IS A SECRET MESSAGE"
    keyword = "HIDE THIS"
    encrpyted_message = encrypt_vigenere(original_message, keyword)
    assert encrpyted_message == " PLWZAZHSG HGQX HDL VEFX"

def test_vigenere_decryption():
    original_message = "JLCW TRSHHJVGLITKLXZ SXI"
    keyword = "REVEAL THIS"
    decrpyted_message = decrypt_vigenere(original_message, keyword)
    assert decrpyted_message == "THIS IS A SECRET MESSAGE"
# END OF TESTS FOR VIGENERE CIPHER