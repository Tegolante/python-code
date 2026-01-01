import socket
import whois
import requests

def resolve_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Trovato: {ip}")
        try:
            rev = socket.gethostbyaddr(ip)
            print(f"[+] Reverse DNS: {rev[0]}")
        except:
            print("[-] Nessun reverse DNS trovato.")
        return ip
    except Exception as e:
        print(f"[!] Errore nella risoluzione DNS: {e}")
        return None

def get_whois(domain):
    try:
        w = whois.whois(domain)
        print(f"\n[+] WHOIS Info:\n- Registrante: {w.registrant_organization}\n- Indirizzo Registrante: {w.registrant_address}\n- Indirizzo Admin: {w.admin_address}\n- Organizzazione Admin: {w.admin_organization}\n- Nome Admin: {w.admin_name}\n- Tech Address: {w.tech_address}\n- Registrar Indirizzo: {w.registrar_address}\n- Registrar: {w.registrar}\n- Registrar Nome: {w.registrar_name}\n- Creato il: {w.creation_date}\n- Aggiornato il: {w.updated_date}\n- Scadenza: {w.expiration_date}\n- Email: {w.emails}")
    except Exception as e:
        print(f"[!] WHOIS fallito: {e}")

def geoip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url)
        data = r.json()
        print(f"\n[+] GeoIP Info:\n- Paese: {data['country']}\n- Regione: {data['regionName']}\n- Città: {data['city']}\n- Zip: {data['zip']}\n- Lat: {data['lat']}\n- Lon: {data['lon']}\n- Timezone: {data['timezone']}\n- ISP: {data['isp']}\n- Organizzazione: {data['org']}\n- ASN: {data['as']} Query: {data['query']}\n")
    except Exception as e:
        print(f"[!] GeoIP lookup fallito: {e}")

def main():
    print("=== ReconTool v1 ===")
    target = input("Inserisci dominio o IP target: ").strip()

    ip = resolve_dns(target)
    if ip:
        geoip_lookup(ip)
    if not target.replace(".", "").isdigit():
        get_whois(target)


main()