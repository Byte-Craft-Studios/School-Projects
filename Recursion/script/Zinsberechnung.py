def zukunftswert(startkapital, zinssatz, jahre, jahreseinzahlung=0):
    """
    Berechnet den zukünftigen Wert einer Investition mit optionalen jährlichen Einzahlungen.

    Args:
    startkapital (float): Der Anfangsbetrag der Investition.
    zinssatz (float): Der jährliche Zinssatz (als Dezimalzahl, z.B. 0.05 für 5%).
    jahre (int): Die Anzahl der Jahre.
    jahreseinzahlung (float, optional): Der jährliche Beitrag zur Investition. Default ist 0.

    Returns:
    float: Der zukünftige Wert der Investition.
    """
    zukunftswert = startkapital
    for jahr in range(1, jahre + 1):
        zukunftswert = (zukunftswert + jahreseinzahlung) * (1 + zinssatz)
    return zukunftswert

def hauptfunktion():
    weitere_investitionen = True

    while weitere_investitionen:
        # Eingabe der Parameter für die Investition
        print("\nWählen Sie die Berechnungsart:")
        print("1. Nur Startkapital")
        print("2. Startkapital und jährliche Einzahlungen")
        wahl = int(input("Geben Sie Ihre Wahl ein (1 oder 2): "))

        startkapital = float(input("Geben Sie den Anfangsbetrag der Investition ein: "))
        zinssatz = float(input("Geben Sie den jährlichen Zinssatz (in Dezimalform, z.B. 0.05 für 5%) ein: "))
        jahre = int(input("Geben Sie die Anzahl der Jahre ein: "))

        if wahl == 1:
            # Berechnung nur mit Startkapital
            jahreseinzahlung = 0
        elif wahl == 2:
            # Berechnung mit Startkapital und jährlichen Einzahlungen
            jahreseinzahlung = float(input("Geben Sie den jährlichen Beitrag zur Investition ein: "))
        else:
            print("Ungültige Wahl. Programm wird beendet.")
            return

        # Berechnung des zukünftigen Werts
        zukunftswert_betrag = zukunftswert(startkapital, zinssatz, jahre, jahreseinzahlung)

        # Ausgabe des Ergebnisses
        print(f"Der zukünftige Wert der Investition beträgt: {zukunftswert_betrag:.2f} EUR")

        # Abfrage, ob weitere Investitionen eingegeben werden sollen
        weiter = input("Möchten Sie eine weitere Investition berechnen? (ja/nein): ").lower()
        if weiter != "ja":
            weitere_investitionen = False

if __name__ == "__main__":
    hauptfunktion()