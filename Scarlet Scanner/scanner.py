import socket
from datetime import datetime

# Estética do terminal
print("-" * 50)
print("Scarlet Port Scanner - Blade of Miquella Edition")
print("-" * 50)

# Alvo (podes testar com o IP do teu router ou 'scanme.nmap.org')
import socket

print("""
      /\\
     /  \\
    /    \\     SCARLET SCANNER
   /      \\    Blade of Miquella Edition
  /________\\
""")

target = input("Digite o host para escanear (ex: scanme.nmap.org): ")

# Portas comuns que hackers costumam testar
ports = [21, 22, 25, 53, 80, 443, 3306, 8080]

print(f"\nIniciando reconhecimento no alvo: {target}\n")
print("-" * 30)

for port in ports:
    # Criando o socket para testar a conexão
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # Tempo de espera de 1 segundo
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"[⚔️] CRITICAL HIT! Porta {port} está vulnerável! ABERTA ✅")
    else:
        print(f"[ ] Porta {port}: fechada")
        
    sock.close()

print("-" * 30)
print("\nReconhecimento finalizado.")