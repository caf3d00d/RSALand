import sys
import binascii
from math import sqrt


# Create two large prime numbers namely p and q.
# The product of these numbers will be called n, where n= p*q
#
# Generate a random number which is relatively prime
# with (p-1) and (q-1). Let the number be called as e.
#
# Calculate the modular inverse of e.
# The calculated inverse will be called as d.

def encryption():
    # The message we want to encrypt
    M = "My credit card number is 1337"

    # The public key and exponent
    n = 30994968412821274638126108542140224647370292100079091608343041083209715023181825537637957453183815788151099869840363450721
    e = 65537

    # Encoding the message to hex
    m_hex = M.encode("utf-8").hex()

    # The encryption formula of RSA: c = m ^ e mod n
    c = pow(int(m_hex, 16), e, n)

    print("The encrypted message: ", c)


def decryption():
    n = 30994968412821274638126108542140224647370292100079091608343041083209715023181825537637957453183815788151099869840363450721
    d = 10949944362147351445695313961215384000802056441294706923101734114824865877971959648683318864984560110549528540371119079473
    c = 3740808283126743789473658216888004237756151970385422112230702175214670415045578511813428786937523016996521109011952458274
    t = pow(c, d, n)
    t_hex = hex(t)
    # t_byte = bytes.fromhex('4d79206372656469742063617264206e756d6265722069732031333337').decode('utf-8')
    t_byte = bytes.fromhex(t_hex[2:]).decode('utf-8')
    print(t_byte)


if len(sys.argv) == 2:
    if str(sys.argv[1]) == "enc":
        encryption()
    elif str(sys.argv[1]) == "dec":
        decryption()
    else:
        sys.exit("Usage: ./rsa_encryption <enc/dec>")
else:
    sys.exit("Usage: ./rsa_encryption <enc/dec>")
