import pytest
from one_time_pad import decrypt_one_time_pad, encrypt_one_time_pad

"""Tests for One-Time Pad encryption and decryption."""

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
