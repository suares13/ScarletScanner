# ⚔️ Scarlet Scanner 

> **Status:** Blade of Miquella Edition

O **Scarlet Scanner** é um script de reconhecimento de rede desenvolvido em Python. Ele atua como um *Port Scanner* básico, capaz de mapear portas TCP abertas em um host alvo para identificar serviços ativos.

### 🛡️ Por que "Blade of Miquella Edition"?
Para não parecer apenas um nome aleatório, a escolha integra a estética do meu perfil ao propósito da ferramenta:
- **Precisão:** Assim como a personagem, o script busca ser direto e preciso em seu "golpe" (a tentativa de conexão).
- **Identity & Theming:** O uso de referências de *Elden Ring* no terminal é um "easter egg" visual, uma prática comum na cultura hacker e de desenvolvimento para dar personalidade a ferramentas de CLI (Interface de Linha de Comando).

### 🧠 Conceitos Aplicados
- **Bibliotecas Nativa:** Uso do módulo `socket` para gerenciar conexões de rede.
- **TCP Connect Scanning:** O script utiliza o método `connect_ex` para realizar o *handshake* e validar se a porta está aceitando conexões.
- **Surface Mapping:** O primeiro estágio de qualquer teste de penetração (Pentest) ou estudo de Red Team.

### 🚀 Como utilizar
1. Certifique-se de ter o Python 3 instalado.
2. Execute o arquivo:
   ```bash
   python scanner.py
