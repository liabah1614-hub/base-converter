# Ce fichier contient toutes les fonctions de conversion entre bases.
# L'idée est de séparer la logique (les conversions) du programme principal.

def decimal_to_binary(n):
    # Convertit un entier décimal en binaire.
    # bin(n) renvoie une chaîne comme '0b1010', donc on enlève '0b' avec [2:].
    return bin(n)[2:]

def decimal_to_hex(n):
    # Convertit un entier décimal en hexadécimal.
    # hex(n) renvoie '0xA3', donc on enlève '0x' et on met en majuscules.
    return hex(n)[2:].upper()

def binary_to_decimal(b):
    # Convertit une chaîne binaire (ex: '1010') en entier décimal.
    # int(b, 2) interprète la chaîne comme un nombre en base 2.
    return int(b, 2)

def hex_to_decimal(h):
    # Convertit une chaîne hexadécimale (ex: 'A3') en entier décimal.
    # int(h, 16) interprète la chaîne comme un nombre en base 16.
    return int(h, 16)
