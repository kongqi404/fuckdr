from Cryptodome.Cipher import AES
import base64
from Cryptodome.Util.Padding import pad


def test_aes():
    key = "6cfd5dd4dea0e831"
    ip = "127.0.0.1"
    data = AES.new(key.encode("utf-8"), AES.MODE_ECB).encrypt(
        pad(ip.encode("utf-8"), 16)
    )
    data = base64.b64encode(data).decode("utf-8")
    assert data == "qI5Nmwm3SRDAqd9uyQgmWg=="
