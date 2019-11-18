#(private key) -> (object of information)
import os, binascii, hashlib, base58, datetime

identities = {}
directory = []

# ID
class ID():
    def __init__(self, name, ID_number, birthday, SSN):
        hasher = hashlib.sha256()
        #Hash(name+birthday+SSN)
        hasher.update((name.lower() + birthday + str(SSN)).encode('UTF-8'))

        self.ID_number = hasher.hexdigest()
        self.name = name.lowercase()
        #String of 8 characters, "DDMMYYYY"
        self.birthday = birthday
        self.SSN = str(SSN)

        #Add id number to public directory
        directory.append(self.ID_number)

def create_id(name, ID_number, birthday, SSN):
    identity = ID(name, ID_number, birthday, SSN)
    check_duplicate = identity.ID_number
    if check_duplicate in directory:
        return "ID already used"

    #Private key creation
    fullkey = "80"+binascii.hexlify(os.urandom(32)).decode()
    sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
    sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
    WIF = base58.b58encode(binascii.unhexlify(fullkey+sha256b[:8]))
    ########

    private_key = WIF

    Identities[private_key] = identity
    return private_key

def view_id(private_key):
    if identities.get(private_key, False):
        return identities[private_key]
    return "Not a valid private key"

def convert_birth_age(id):
    birthdate = id.birthday
    person_year = int(birthdate[5:])
    person_month = int(birthdate[2:4])

    age = now.year - person_year - 1 + (now.month > person_month)

    return age

######z-proof section
def verify_age():

######
# Stuff to do:
# -research zero knowledge implementation
# -blockchain for transactions and creation of id
# -front end ideas
