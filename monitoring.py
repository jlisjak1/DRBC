import psutil
import time
import os

SERVICE = "apache2"

print(f"[*] Pokrećem nadzor servisa: {SERVICE}")
print("Pritisni Ctrl+C za prekid.")

while True:
    running = False
    # Provjeri sve procese
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == SERVICE:
            running = True
            break
    
    if running:
        # Zeleni tekst
        print(f"\033[92m[OK] {SERVICE} radi uredno.\033[0m")
    else:
        # Crveni tekst
        print(f"\033[91m[ALARM] PAŽNJA! {SERVICE} JE PAO! POTREBAN OPORAVAK!\033[0m")
    
    time.sleep(2)