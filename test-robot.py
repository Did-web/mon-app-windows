from playwright.sync_api import sync_playwright

def run():
    print("🚀 Lancement du moteur Chromium...")
    with sync_playwright() as p:
        # On lance le navigateur
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # On teste une connexion simple
        print("🌍 Connexion à Google pour test...")
        page.goto("https://www.google.com")
        
        # Vérification
        print(f"✅ Robot opérationnel sur : {page.title()}")
        
        browser.close()
        print("🏁 Mission terminée proprement.")

if __name__ == "__main__":
    run()