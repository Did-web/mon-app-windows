from playwright.sync_api import sync_playwright

def scrape_finance():
    with sync_playwright() as p:
        print("📈 Lancement de l'extracteur financier (Mode Robuste)...")
        # On lance Chromium
        browser = p.chromium.launch(headless=True)
        # On définit un "user agent" pour ne pas être détecté comme un simple robot
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            print("🌍 Connexion à Yahoo Finance...")
            page.goto("https://fr.finance.yahoo.com/quote/%5EFCHI/components/", timeout=60000)

            # --- GESTION DES COOKIES ---
            print("🍪 Vérification des cookies...")
            # On cherche un bouton qui contient "Accepter" ou "Tout accepter"
            try:
                # Cette méthode est plus fiable que les ID qui changent
                page.get_by_role("button", name="Tout accepter").click(timeout=5000)
                print("✅ Cookies acceptés.")
            except:
                print("ℹ️ Pas de bouton de cookies détecté ou déjà accepté.")

            # --- EXTRACTION DES DONNÉES ---
            print("⏳ Attente du tableau des cours...")
            # On attend que le tableau contenant les prix apparaisse
            page.wait_for_selector('table', timeout=20000)
            
            print("\n" + "="*45)
            print(f"{'ACTION':<25} | {'PRIX':<10} | {'VAR'}")
            print("="*45)

            # On récupère les lignes (tr) du corps du tableau (tbody)
            lignes = page.query_selector_all('table tbody tr')

            for ligne in lignes[:5]: # On limite aux 5 premières
                colonnes = ligne.query_selector_all('td')
                if len(colonnes) >= 5:
                    nom = colonnes[1].inner_text()      # 2ème colonne : Nom
                    prix = colonnes[2].inner_text()     # 3ème colonne : Dernier cours
                    variation = colonnes[4].inner_text() # 5ème colonne : Variation %
                    print(f"{nom[:24]:<25} | {prix:<10} | {variation}")

            print("="*45)

        except Exception as e:
            print(f"❌ Une erreur est survenue : {e}")
            # En cas d'erreur, on prend une photo pour comprendre
            page.screenshot(path="debug_finance.png")
            print("📸 Capture d'écran 'debug_finance.png' enregistrée.")

        finally:
            browser.close()
            print("\n✅ Session terminée.")

if __name__ == "__main__":
    scrape_finance()