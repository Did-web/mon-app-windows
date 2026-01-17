from playwright.sync_api import sync_playwright

def scrape_finance():
    with sync_playwright() as p:
        print("📈 Lancement de l'extracteur (Cible : Yahoo Finance)...")
        browser = p.chromium.launch(headless=True)
        # On définit une taille de fenêtre standard pour bien voir le bouton
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        try:
            print("🌍 Connexion à Yahoo...")
            page.goto("https://fr.finance.yahoo.com/quote/%5EFCHI/components/", wait_until="networkidle")

            # --- LA MANOEUVRE COOKIES ---
            print("🍪 Mur de cookies détecté. Tentative de passage...")
            # On attend que le bouton "Accepter tout" soit réellement cliquable
            # On utilise le texte exact vu sur votre capture d'écran
            try:
                page.wait_for_selector("text=Accepter tout", timeout=10000)
                page.click("text=Accepter tout")
                print("✅ Bouton cliqué ! Accès au contenu...")
            except:
                print("ℹ️ Bouton non trouvé, tentative alternative...")
                # Plan B : on clique sur le bouton principal de la fenêtre
                page.keyboard.press("Enter") 

            # --- EXTRACTION ---
            print("⏳ Chargement du tableau des prix...")
            # On attend le tableau (le sélecteur .W(100%) est souvent utilisé par Yahoo)
            page.wait_for_selector("table", timeout=20000)
            
            print("\n" + "="*50)
            print(f"{'SYMBOLE':<10} | {'NOM':<25} | {'PRIX'}")
            print("="*50)

            # On récupère les 5 premières lignes du tableau
            lignes = page.locator("table tbody tr").all()
            for i in range(min(5, len(lignes))):
                cols = lignes[i].locator("td").all_text_contents()
                if len(cols) >= 3:
                    print(f"{cols[0]:<10} | {cols[1][:24]:<25} | {cols[2]} €")
            
            print("="*50)

        except Exception as e:
            print(f"❌ Erreur : {e}")
            page.screenshot(path="debug_v3.png")
            print("📸 Nouvelle capture 'debug_v3.png' créée.")

        finally:
            browser.close()
            print("\n✅ Session terminée.")

if __name__ == "__main__":
    scrape_finance()