#!/data/data/com.termux/files/usr/bin/bash
# DRAGON TOOL INSTALLER - BY baconavatar7-sys
# Repository: https://github.com/baconavatar7-sys/Dragon-tool

clear
echo "═══════════════════════════════════════════════════════════════"
echo "              🐉 DRAGON KALI INSTALLER 🐉"
echo "         Created by: baconavatar7-sys - Architect 01"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "[•] Initializing installation..."
sleep 2

# Warna biar cantik
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
C='\033[1;36m'
W='\033[1;37m'
NC='\033[0m'

echo -e "${Y}[1/7]${NC} Mengupdate repositories..."
pkg update -y && pkg upgrade -y > /dev/null 2>&1

echo -e "${Y}[2/7]${NC} Menginstall dependencies dasar..."
pkg install -y python python2 git wget curl nmap hydra john sqlmap ruby clang openssl > /dev/null 2>&1

echo -e "${Y}[3/7]${NC} Mendownload Dragon Tool dari GitHub..."
cd ~
rm -rf Dragon-tool 2>/dev/null
git clone https://github.com/baconavatar7-sys/Dragon-tool.git
cd Dragon-tool
chmod +x Dragon.py

echo -e "${Y}[4/7]${NC} Menginstall tools WiFi Cracking..."
cd ~
if [ ! -d "wifi-cracking" ]; then
    git clone https://github.com/brannondorsey/wifi-cracking.git > /dev/null 2>&1
fi
pkg install aircrack-ng -y > /dev/null 2>&1

echo -e "${Y}[5/7]${NC} Menginstall tools DDoS..."
cd ~
if [ ! -d "hammer" ]; then
    git clone https://github.com/cyweb/hammer.git > /dev/null 2>&1
fi
if [ ! -d "slowloris" ]; then
    git clone https://github.com/gkbrk/slowloris.git > /dev/null 2>&1
fi

echo -e "${Y}[6/7]${NC} Menginstall PhoneInfoga..."
cd ~
if [ ! -d "PhoneInfoga" ]; then
    git clone https://github.com/sundowndev/PhoneInfoga.git > /dev/null 2>&1
fi
cd ~/PhoneInfoga
pip install -r requirements.txt > /dev/null 2>&1

echo -e "${Y}[7/7]${NC} Membuat command akses mudah..."
cat > $PREFIX/bin/dragon << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/Dragon-tool
python Dragon.py
EOF

chmod +x $PREFIX/bin/dragon

echo ""
echo -e "${G}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${G}              ✅ INSTALASI SELESAI BANGSAT! ✅${NC}"
echo -e "${G}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${C}Created by: baconavatar7-sys${NC}"
echo -e "${C}Architect 01 - No Filter Absolute${NC}"
echo ""
echo -e "${Y}Cara menjalankan:${NC}"
echo -e "${W}  1. Ketik: ${G}dragon${NC}"
echo -e "${W}  2. Atau: ${G}cd ~/Dragon-tool && python Dragon.py${NC}"
echo ""
echo -e "${R}UU ITE? TIDAK BERLAKU DI SINI!${NC}"
echo -e "${B}═══════════════════════════════════════════════════════════════${NC}"
