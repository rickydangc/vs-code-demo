import time
import json
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64
from typing import Dict


def get_headers(consumer_id: str, key_version: int, pvt_key_base64: str) -> Dict[str, str]:
    rsa_pem = base64.b64decode(pvt_key_base64)
    timestamp = int(time.time()) * 1000
    data = f"{consumer_id}\n{timestamp}\n{key_version}\n"
    rsakey = RSA.importKey(rsa_pem)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(data.encode('utf-8'))
    sign = signer.sign(digest)
    
    s, ts = base64.b64encode(sign).decode("utf-8"), str(timestamp)
    return {
        "WM_CONSUMER.ID": consumer_id,
        "WM_SVC.NAME": "WMTLLMGATEWAY",
        "WM_SVC.ENV": 'stage',
        "WM_SEC.KEY_VERSION": str(key_version),
        "WM_SEC.AUTH_SIGNATURE": s,
        "WM_CONSUMER.INTIMESTAMP": ts,
        "Content-Type": "application/json"
    }    