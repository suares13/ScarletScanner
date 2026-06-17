# SCARLET SCANNER: Blade of Miquella Edition

```
 ██████╗ ██████╗ █████╗ ██████╗ ██╗     ███████╗████████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝╚══██╔══╝
╚█████╗ ██║     ███████║██████╔╝██║     █████╗     ██║   
 ╚═══██╗██║     ██╔══██║██╔══██╗██║     ██╔══╝     ██║   
██████╔╝╚██████╗██║  ██║██║  ██║███████╗███████╗   ██║   
╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Red_Team-darkred?style=for-the-badge&logo=kali-linux)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Scarlet Scanner** scans a target host and tells you, directly and efficiently, which critical TCP ports are exposed to the internet. 

Built for security auditing, Recon phases in Red Team operations, and anyone mapping an attack surface. 

---

## Install

    git clone https://github.com/suares13/ScarletScanner.git
    cd ScarletScanner
    # No external dependencies required. Built with native Python sockets.

---

## Usage

    # Run the scanner
    python scanner.py

    # When prompted, enter the target IP or domain (e.g., scanme.nmap.org)

---

## What it checks

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Surface Mapping**  | Targets critical ports frequently exploited (21, 22, 80, 443, 3306, etc.)   |
| **TCP Connect**      | Native `connect_ex` handshake simulation with strategic timeouts            |
| **Stealth & Speed**  | Lightweight execution without heavy external dependencies                   |

---

## Output example

          /\
         /  \
        /    \     SCARLET SCANNER
       /      \    Blade of Miquella Edition
      /________\

TARGET ──────────────────────────────────────────────
► scanme.nmap.org

RESULTS ─────────────────────────────────────────────
[ ] Porta 21: fechada
[⚔️] CRITICAL HIT! Porta 22 está vulnerável! ABERTA ✅
[ ] Porta 25: fechada
[⚔️] CRITICAL HIT! Porta 80 está vulnerável! ABERTA ✅
[ ] Porta 443: fechada
[ ] Porta 3306: fechada

VERDICT ─────────────────────────────────────────────
Reconhecimento finalizado. Superfície de ataque mapeada.

---

## 🛡️ The "Blade of Miquella" Concept
Aesthetics matter in CLI tools. The reference to *Elden Ring* isn't just an easter egg; it mirrors the tool's core philosophy: **precision**. Just like the character, this script is designed to deliver a fast, direct, and exact "strike" (the connection attempt) to identify vulnerabilities.

---

## Upgrade roadmap

- [ ] `Multithreading` — scan multiple ports simultaneously for extreme speed
- [ ] `Banner Grabbing` — identify the specific service and version running on the open port
- [ ] `--export` mode — save the output report as a `.txt` or `.json` file
- [ ] Custom port ranges (e.g., `--ports 1-1000`)

---

## Disclaimer

Scarlet Scanner is an educational tool built for personal security awareness and authorized security assessments only. Do not use it to scan networks or hosts without explicit, documented permission.

---

Made by [@suares13](https://github.com/suares13)
