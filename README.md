# ⚔️ SCARLET SCANNER
> **Status:** Blade of Miquella Edition

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Red_Team-darkred?style=for-the-badge&logo=kali-linux)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### 💻 O que é o projeto
O **Scarlet Scanner** é um script de reconhecimento de rede desenvolvido em Python. Ele atua como um *Port Scanner* básico e direto ao ponto, mapeando portas TCP em um host para identificar rapidamente quais serviços estão ativos.

O código foi construído utilizando a biblioteca nativa `socket`, executando a técnica de **TCP Connect Scanning** (método `connect_ex`) para realizar o *handshake* e validar se a porta está aceitando conexões. Este mapeamento de superfície de ataque configura o primeiro estágio fundamental de qualquer teste de penetração (Pentest) ou estudo ofensivo.

### 🛡️ Por que "Blade of Miquella Edition"?
Para não parecer apenas um nome aleatório, a escolha integra a estética do meu perfil ao propósito da ferramenta:
- **Precisão:** Assim como a personagem de *Elden Ring*, o script busca ser direto e preciso em seu "golpe" (a tentativa de conexão).
- **Identity & Theming:** O uso de referências visuais no terminal (ASCII Art) é um *easter egg*, uma prática comum na cultura hacker e de desenvolvimento para dar personalidade a ferramentas de CLI (Interface de Linha de Comando).

### ⚠️ Aviso Ético
O Scarlet Scanner foi desenvolvido estritamente para fins educacionais, estudos de segurança da informação e auditorias autorizadas. O uso desta ferramenta para escanear redes ou hosts de terceiros sem o consentimento prévio e explícito é proibido e de total responsabilidade do usuário.

### 🚀 Como utilizar
1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Clone o repositório ou baixe o arquivo `scanner.py`.
3. Abra o seu terminal e execute o arquivo:
```bash
   python scanner.py
```
4. Quando solicitado pelo terminal, insira o host alvo (você pode testar com o IP do seu roteador ou domínios de teste autorizados, como scanme.nmap.org).
