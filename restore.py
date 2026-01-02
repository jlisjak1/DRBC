import os

# --- KONFIGURACIJA ---
# Adresa s koje skidamo (VM2)
REMOTE_IP = "172.16.78.132"
# --- PROMJENA: Korisnik na VM2 ---
REMOTE_USER = "vm2"
REMOTE_PATH = "/home/vm2/"

print("--- POČETAK OPORAVKA (RESTORE) ---")
print(f"Spajam se na VM2 kao korisnik: {REMOTE_USER}")
# Korisnik upisuje ime datoteke koju želi vratiti
backup_name = input("Unesi TOČNO ime backup datoteke (npr. web_backup_2025...tar.gz): ")

# 1. Preuzimanje (SCP s VM2 na VM1)
print(f"[*] Preuzimam {backup_name} s backup servera...")
print("Molim upišite lozinku za korisnika 'vm2' na VM2 kada se zatraži.")
scp_command = f"scp {REMOTE_USER}@{REMOTE_IP}:{REMOTE_PATH}{backup_name} ."
download_code = os.system(scp_command)

if download_code == 0:
    print("[*] Prijenos uspješan. Vraćam podatke na mjesto...")
    
    # 2. Brisanje trenutnog (oštećenog) sadržaja
    # Koristimo sudo jer /var/www/html pripada rootu
    os.system("sudo rm -rf /var/www/html/*")
    
    # 3. Raspakiravanje backupa
    restore_cmd = f"sudo tar -xzvf {backup_name} -C /"
    os.system(restore_cmd)
    
    print("\n\033[92m[USPJEH] Sustav je oporavljen! Web stranica bi trebala raditi.\033[0m")
    
    # Opcionalno: obriši preuzetu arhivu da ne smeta
    # os.remove(backup_name) 
else:
    print("\n\033[91m[GREŠKA] Ne mogu pronaći tu datoteku na VM2 ili je lozinka kriva.\033[0m")
    print(f"Provjeri postoji li {backup_name} u mapi /home/vm2/ na drugoj mašini.")