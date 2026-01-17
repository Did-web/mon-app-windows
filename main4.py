from playwright.sync_api import sync_playwright

def scrape_finance_brave():
    with sync_playwright() as p:
        print("🚀 Lancement de l'extracteur (Cible : Yahoo Finance)...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        try:
            print("🌍 Connexion à Yahoo...")
            page.goto("https://fr.finance.yahoo.com/quote/%5EFCHI/components/", wait_until="networkidle")

            # --- MANOEUVRE ANTI-BLOCAGE COOKIES ---
            print("🍪 Gestion du mur de cookies...")
            
            # 1. On clique sur "Aller à la fin" pour débloquer le bouton Accepter
            try:
                page.click("text=Aller à la fin", timeout=5000)
                print("⏬ Défilement vers le bas effectué.")
                page.wait_for_timeout(1000) # Petite pause pour laisser l'animation finir
            except:
                print("ℹ️ Bouton 'Aller à la fin' non trouvé, peut-être déjà en bas.")

            # 2. On clique enfin sur "Accepter tout"
            try:
                page.click("text=Accepter tout", timeout=5000)
                print("✅ Cookies acceptés !")
            except:
                print("⚠️ Impossible de cliquer sur Accepter tout. Tentative de forcing...")
                page.keyboard.press("Enter")

            # --- EXTRACTION DES DONNÉES ---
            print("⏳ Chargement du tableau des prix...")
            # On attend un sélecteur plus spécifique au tableau financier
            page.wait_for_selector("table", timeout=20000)
            
            print("\n" + "="*55)
            print(f"{'SYMBOLE':<10} | {'NOM':<28} | {'PRIX'}")
            print("="*55)

            # Extraction propre
            lignes = page.locator("table tbody tr").all()
            for i in range(min(5, len(lignes))):
                cols = lignes[i].locator("td").all_text_contents()
                if len(cols) >= 3:
                    # On nettoie le nom pour qu'il ne dépasse pas
                    nom_propre = cols[1].split(' (')[0] 
                    print(f"{cols[0]:<10} | {nom_propre[:27]:<28} | {cols[2]} €")
            
            print("="*55)

        except Exception as e:
            print(f"❌ Blocage persistant : {e}")
            page.screenshot(path="debug_final.png")
            print("📸 Regardez 'debug_final.png' pour voir le résultat.")

        finally:
            browser.close()
            print("\n✅ Mission terminée.")

if __name__ == "__main__":
    scrape_finance_brave()