from playwright.sync_api import sync_playwright

def scrape_finance():
    with sync_playwright() as p:
        print("📈 Lancement de l'extracteur (Version Ruse)...")
        browser = p.chromium.launch(headless=True)
        # On simule un vrai navigateur très récent
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        try:
            print("🌍 Connexion à Yahoo...")
            page.goto("https://fr.finance.yahoo.com/quote/%5EFCHI/components/", wait_until="domcontentloaded")

            # On attend un peu que les scripts de cookies se lancent
            page.wait_for_timeout(3000)

            # --- STRATÉGIE COOKIES AGRESSIVE ---
            try:
                # On cherche n'importe quel bouton qui contient "Accepter"
                bouton = page.get_by_role("button", name="Tout accepter")
                if bouton.is_visible():
                    bouton.click()
                    print("✅ Cookies acceptés par bouton.")
            except:
                print("ℹ️ Bouton d'acceptation non cliquable, on continue.")

            # --- ATTENTE DU CONTENU ---
            print("⏳ Recherche des données boursières...")
            # Au lieu d'attendre 'table', on attend de voir le mot 'Symbole' ou 'Nom'
            page.wait_for_selector("text=Symbole", timeout=20000)
            
            # On récupère toutes les lignes qui ressemblent à des données financières
            rows = page.locator("table tbody tr").all()
            
            print("\n" + "="*50)
            print(f"{'SYMBOLE':<10} | {'NOM':<25} | {'PRIX'}")
            print("="*50)

            for i in range(min(5, len(rows))):
                texte_ligne = rows[i].inner_text().split('\t')
                # Nettoyage rapide des données
                data = rows[i].locator("td").all_text_contents()
                if len(data) >= 3:
                    print(f"{data[0]:<10} | {data[1][:24]:<25} | {data[2]} €")

            print("="*50)

        except Exception as e:
            print(f"❌ Blocage détecté : {e}")
            page.screenshot(path="debug_finance_v2.png")
            # On sauvegarde aussi le code HTML pour analyser si besoin
            with open("page_source.html", "w") as f:
                f.write(page.content())
            print("📸 Nouvelles preuves (image + HTML) enregistrées.")

        finally:
            browser.close()
            print("\n✅ Session terminée.")

if __name__ == "__main__":
    scrape_finance()