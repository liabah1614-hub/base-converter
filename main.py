# On importe toutes les fonctions du fichier converter.py
from converter import *

def detect_base(value):
    """
    Détecte automatiquement la base du nombre entré par l'utilisateur.
    - Si ça commence par '0x' → hexadécimal
    - Si ça contient uniquement 0 et 1 → binaire
    - Si ce sont uniquement des chiffres → décimal
    """
    
    # Cas hexadécimal (notation classique 0xA3)
    if value.startswith("0x") or value.startswith("0X"):
        return "hex"
    
    # Cas binaire : tous les caractères doivent être 0 ou 1
    elif all(c in "01" for c in value):
        return "bin"
    
    # Cas décimal : uniquement des chiffres
    elif value.isdigit():
        return "dec"
    
    # Aucun format reconnu
    else:
        return None


def main():
    # On demande un nombre à l'utilisateur
    value = input("Entrez un nombre (binaire, décimal ou hexadécimal) : ")

    # On détecte la base du nombre
    base = detect_base(value)

    # Si la base n'est pas reconnue, on arrête le programme
    if base is None:
        print("Format non reconnu.")
        return

    # Si le nombre est en décimal
    if base == "dec":
        n = int(value)  # On convertit la chaîne en entier
        print("Binaire :", decimal_to_binary(n))
        print("Hexadécimal :", decimal_to_hex(n))

    # Si le nombre est en binaire
    elif base == "bin":
        n = binary_to_decimal(value)  # binaire → décimal
        print("Décimal :", n)
        print("Hexadécimal :", decimal_to_hex(n))

    # Si le nombre est en hexadécimal
    elif base == "hex":
        # On enlève le '0x' si l'utilisateur l'a mis
        cleaned = value[2:] if value.startswith(("0x", "0X")) else value
        n = hex_to_decimal(cleaned)  # hex → décimal
        print("Décimal :", n)
        print("Binaire :", decimal_to_binary(n))


# Point d'entrée du programme
if __name__ == "__main__":
    main()
