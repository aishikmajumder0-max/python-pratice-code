import webbrowser
from datetime import datetime

def afficher_aide():
    print("\nCommandes disponibles :")
    print("  heure          - Afficher l'heure actuelle")
    print("  date           - Afficher la date du jour")
    print("  ouvrir youtube - Ouvrir YouTube")
    print("  ouvrir google  - Ouvrir Google")
    print("  ouvrir github  - Ouvrir GitHub")
    print("  aide           - Afficher les commandes")
    print("  quitter        - Fermer l'assistant")


def afficher_heure():
    print(f"\nHeure actuelle : {datetime.now():%H:%M:%S}")


def afficher_date():
    print(f"\nDate du jour : {datetime.now():%d/%m/%Y}")


def ouvrir_site(nom, url):
    webbrowser.open(url)
    print(f"\nOuverture de {nom}...")


def main():
    print("\n" + "=" * 55)
    print("                  ASSISTANT VOCAL PYTHON")
    print("=" * 55)

    print("\nAssistant prêt. Tapez 'aide' pour voir les commandes.")

    commandes = {
        "heure": afficher_heure,
        "date": afficher_date,
        "ouvrir youtube": lambda: ouvrir_site(
            "YouTube", "https://www.youtube.com"
        ),
        "ouvrir google": lambda: ouvrir_site(
            "Google", "https://www.google.com"
        ),
        "ouvrir github": lambda: ouvrir_site(
            "GitHub", "https://github.com"
        ),
        "aide": afficher_aide
    }

    while True:
        commande = input("\nCommande : ").strip().lower()

        if commande == "quitter":
            print("\nAssistant fermé.")
            break

        action = commandes.get(commande)

        if action:
            action()
        else:
            print(
                "\nCommande inconnue."
                "Tapez 'aide' pour voir les commandes disponibles."
            )

    print("=" * 55)


if __name__ == "__main__":
    main()