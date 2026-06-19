import re
from collections import Counter

def triagem_logs(log_text):
    print("=== PROTÓTIPO DE TRIAGEM COMUNIDADE RAIO-X ===")
    
    # Simple regex to capture: [Date Time] Sender: Message
    pattern = re.compile(r"^\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\] ([^:]+): (.*)")
    
    messages_count = Counter()
    presentations = []
    
    lines = log_text.strip().split("\n")
    for line in lines:
        m = pattern.match(line)
        if m:
            sender, msg = m.groups()
            sender = sender.strip()
            messages_count[sender] += 1
            
            # Simple heuristic for presentations: mentions "sou", "trabalho", "nicho", "cidade"
            lower_msg = msg.lower()
            if any(word in lower_msg for word in ["sou ", "trabalho", "nicho", "meu nome", "instagram"]):
                presentations.append((sender, msg[:120] + "..."))
                
    print(f"\nTotal de mensagens analisadas: {len(lines)}")
    print(f"Total de membros únicos identificados: {len(messages_count)}")
    
    print("\nRanking de Membros Mais Ativos:")
    for member, count in messages_count.most_common(5):
        print(f" - {member}: {count} mensagens")
        
    print("\nPossíveis Apresentações Identificadas:")
    for member, snippet in presentations[:3]:
        print(f" - {member}: {snippet}")
        
    print("\n=== FIM DA TRIAGEM ===")

# Example usage with mock data
mock_log = """[18/06/2026 14:02:11] Arthur Martins: Oi pessoal! Sou ator e palhaço e trabalho com mentorias de palhaçaria criativa aqui em Alagoas.
[18/06/2026 14:05:22] Ana Carolina Mattoso: Sou professora universitária e tenho uma mentoria acadêmica para processos de mestrado.
[18/06/2026 14:10:05] Arthur Martins: Que bacana, Ana! Vamos marcar uma call depois para ver sinergias.
[18/06/2026 14:12:19] Suporte: Link da gravação enviado!
"""

if __name__ == "__main__":
    triagem_logs(mock_log)
