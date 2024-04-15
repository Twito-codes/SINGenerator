from functions import randoms as rand
from datetime import date
import random
import numpy as np
import json


def create_initials(sin_name: str, sin_surname: str):
    names = sin_name.split(' ')
    initials = ''
    for name in names:
        initials += name[0]
    initials += sin_surname[0]
    return initials


def prepare_identificator(
        country_code: str,
        initials: str,
        date_of_birth: date,
        metatype: str
):
    roll = np.random.randint(1, 101)
    status = 'C'    # Civilian
    if roll <= 7:
        status = 'D'    # Deceased
    if roll in range(8, 17):
        status = 'F'    # Felon
    return f"{country_code}{status}{initials}{date_of_birth.strftime('%m%d%y')}{metatype[:2].upper()}"


class SystemIdentificationNumber:
    def __init__(self):
        self.nation: str | None = None
        self.country_code: str | None = None
        self.prepare_sin_origin_data()
        self.metatype: str
        metatypes: dict
        self.metatype, metatypes = rand.determine_metatype(self.nation)
        self.metavariant: str = rand.determine_metavariant(metatypes)
        #  TODO: Create name generator
        self.name = 'John'
        self.surname = 'Doe'
        self.initials = create_initials(self.name, self.surname)
        self.date_of_birth = date(2053, 11, 11)
        self.discriminator = rand.generate_sin_number()
        self.identificator = prepare_identificator(
            self.country_code,
            self.initials,
            self.date_of_birth,
            self.metatype
        )
        self.cipher_mapping = self.generate_cipher()
        self.encoded_identificator = self.encrypt()

    def __str__(self):
        return f"System Identification Number: {self.encoded_identificator}"

    def prepare_sin_origin_data(self):
        country_name, country_of_origin = rand.determine_sin_origin()
        self.nation = country_name
        self.country_code = country_of_origin['country_code']

    def generate_cipher(self):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        random.seed(self.discriminator)
        shuffled_alphabet = alphabet.copy()
        random.shuffle(shuffled_alphabet)

        # Create a mapping between original and shuffled alphabet
        cipher_mapping = dict(zip(alphabet, shuffled_alphabet))
        return cipher_mapping

    def save_cipher_mapping(self):
        with open('cipher_mapping.json', 'w') as file:
            json.dump(self.cipher_mapping, file)

    def encrypt(self):
        cipher_mapping = self.cipher_mapping
        # Encrypt the message using the cipher mapping
        encrypted_message = ''.join(cipher_mapping.get(char, char) for char in self.identificator.upper())
        # TODO: Splice the string and add dashes
        encrypted_identifier = None
        return encrypted_message

    def decrypt(self):
        hashed_name = self.encoded_identificator
        hashed_name.replace('-', '')
        cipher_mapping = self.cipher_mapping
        # Create a reverse mapping for decryption
        reverse_mapping = {v: k for k, v in cipher_mapping.items()}
        # Decrypt the message using the reverse mapping
        decrypted_message = ''.join(reverse_mapping.get(char, char) for char in hashed_name.upper())

        return decrypted_message
