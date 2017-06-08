#!/usr/bin/env python
from cryptography import fernet

if __name__ == '__main__':
    bin_key = fernet.Fernet.generate_key()
    print(bin_key.decode('utf-8'))
