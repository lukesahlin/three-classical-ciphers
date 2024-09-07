import pytest

from OTP import decrypt_one_time_pad, encrypt_one_time_pad


#TESTS FOR OTP
@pytest.mark.parametrize(
    "plain_text, key, expected_encrypted",
    [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZXYWVUTSRQPONMLKJIHGFEDCBA", "ZY ZZZZZZZZZZZZZZZZZZZZZZZ"),
        ("hello", "world", "CSBWR")
    ]
)
def test_encrypt_otp(plain_text, key, expected_encrypted):
   #testing encryption for one-time-pad
    encrypted = encrypt_one_time_pad(plain_text, key)
    assert encrypted == expected_encrypted

@pytest.mark.parametrize(
    "encrypted_text, key, expected_decrypted",
    [
        ("ZY ZZZZZZZZZZZZZZZZZZZZZZZ", "ZXYWVUTSRQPONMLKJIHGFEDCBA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        ("csbwr", "world", "HELLO")
    ]
)
def test_decrypt_otp(encrypted_text, key, expected_decrypted):
    #testing decryption for One Time Pad
    decrypted = decrypt_one_time_pad(encrypted_text, key)
    assert decrypted == expected_decrypted
@pytest.mark.parametrize(
    "plain_text, key",
    [
        ("HELLO", "WORLDX"),  # Length of key is longer than plain_text
        ("ABCDEFGHI", "XYZ")  # Length of key is shorter than plain_text
    ]
)
def test_encrypt_otp_length_mismatch(plain_text, key):
    #testing to make sure that it raises an error when the secret and key are not the same size for encryption
    with pytest.raises(ValueError, match="secret and key are not the same length"):
        encrypt_one_time_pad(plain_text, key)

@pytest.mark.parametrize(
    "encrypted_text, key",
    [
        ("HELLO", "WORLDX"),  # Length of key is longer than encrypted_text
        ("ABCDEFGHI", "XYZ")  # Length of key is shorter than encrypted_text
    ]
)
def test_decrypt_otp_length_mismatch(encrypted_text, key):
    #testing to make sure that it raises an error when the secret and key are not the same size for decryption
    with pytest.raises(ValueError, match="secret and key are not the same length"):
        decrypt_one_time_pad(encrypted_text, key)
#END OF OTP TESTS