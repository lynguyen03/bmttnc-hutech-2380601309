import rsa
import os


class RSACipher:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')
        os.makedirs(self.keys_dir, exist_ok=True)

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(self.key_size)
        with open(os.path.join(self.keys_dir, 'publicKey.pem'), 'wb') as f:
            f.write(public_key.save_pkcs1())
        with open(os.path.join(self.keys_dir, 'privateKey.pem'), 'wb') as f:
            f.write(private_key.save_pkcs1())

    def load_keys(self):
        with open(os.path.join(self.keys_dir, 'publicKey.pem'), 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(os.path.join(self.keys_dir, 'privateKey.pem'), 'rb') as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        return private_key, public_key

    def encrypt(self, message, public_key):
        return rsa.encrypt(message.encode('utf-8'), public_key)

    def decrypt(self, ciphertext, private_key):
        return rsa.decrypt(ciphertext, private_key).decode('utf-8')

    def sign(self, message, private_key):
        return rsa.sign(message.encode('utf-8'), private_key, 'SHA-256')

    def verify(self, message, signature, public_key):
        try:
            rsa.verify(message.encode('utf-8'), signature, public_key)
            return True
        except rsa.VerificationError:
            return False