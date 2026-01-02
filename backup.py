import os
import datetime

# --- KONFIGURACIJA ---
SOURCE = "/var/www/html"
# Adresa Backup servera (VM2)
DEST_IP = "172.16.78.132"
# --- PROMJENA: Korisnik na VM2 ---
DEST_USER = "vm2"
DEST_PATH = "/home/vm2/"

# 1. Kreiranje imena s datumom
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"web_backup_{timestamp}.tar.gz"

print(f"[*] Pakiram mapu {SOURCE} u arhivu {filename}...")
# Kreiraj arhivu lokalno
os.system(f"tar -czf {filename} {SOURCE}")

print(f"[*] Šaljem arhivu korisniku {DEST_USER} na {DEST_IP}...")
print("Molim upišite lozinku za korisnika 'vm2' na VM2 kada se zatraži.")
# Pošalji na VM2 koristeći SCP
exit_code = os.system(f"scp {filename} {DEST_USER}@{DEST_IP}:{DEST_PATH}")

# 2. Provjera i brisanje
if exit_code == 0:
    print("\n\033[92m[USPJEH] Backup je uspješno poslan na VM2!\033[0m")
    print("[*] Brišem lokalnu kopiju radi uštede prostora...")
    os.remove(filename)
else:
    print("\n\033[91m[GREŠKA] Prijenos nije uspio! Provjeri lozinku za 'vm2' ili mrežu.\033[0m")
    print("lokalna kopija je zadržana na VM1.")