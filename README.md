# Py Adyen Encrypt

Py Adyen Encrypt is a python library used to encrypt data to be used for Adyen's payment processing.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install directly from github.

```bash
pip install git+https://github.com/66niko99/py-adyen-encrypt.git
```

## Usage

```python
from py_adyen_encrypt import encryptor

# paste your adyen key here to run tests
ADYEN_KEY = "10001|ABC123..."

# changing adyen version, default is set to _0_1_18
enc = encryptor(ADYEN_KEY)
enc.adyen_version = '_0_1_6'
# or set adyen version when creating the object:
enc = encryptor(adyen_public_key=ADYEN_KEY, adyen_version='_0_1_6')

# changing adyen key after creating encryptor
enc = encryptor(ADYEN_KEY)
# do some stuff with that adyen key...
enc.adyen_public_key = "10001|ABC123..."
# do some stuff with new adyen key...

# generating card data
enc = encryptor(ADYEN_KEY)
card = enc.encrypt_card(card='4444222233337777', cvv='999', month='03', year='2025')
print(card)  # {"card": "adyen...", "cvv": "adyen...", "month": "adyen...", "year": "adyen..."}

# encrypting a single field
enc = encryptor(ADYEN_KEY)
cvv = enc.encrypt_field(name='cvc', value='889')
print(cvv)  # adyenjs_0_1_8$...

# creating a ready-to-encrypt dict with our fields
enc = encryptor(ADYEN_KEY)
cvv_json = enc.field_data(name='cvc', value='889')
print(cvv_json)  # {'cvc': '889', 'generationtime': '2021-05-25T18:26:48.000Z'}

# encrypting from a dict object
enc = encryptor(ADYEN_KEY)
cvv_json = enc.field_data(name='cvc', value='889')
cvv = enc.encrypt_from_dict(dict_=cvv_json)
print(cvv)  # adyenjs_0_1_8$...
```

## Issues
Let me know if you have any issues. Please include MRE if needed.

## License
[MIT](https://choosealicense.com/licenses/mit/)
