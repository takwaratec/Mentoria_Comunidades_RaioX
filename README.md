# Comunidade Raio-X 🔬

> **🧭 O Método de Gestão, Curadoria Ativa e Conversão para Grupos de WhatsApp & Mentorias**

<img src="docs/assets/images/banner-comunidade-raiox.png" alt="Banner Comunidade Raio-X" width="100%">

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Acessar-29b6f6?style=for-the-badge&logo=githubpages&logoColor=white)](https://takwaratec.github.io/Mentoria_Comunidades_RaioX/)
[![MkDocs Material](https://img.shields.io/badge/MkDocs-Material-29b6f6?style=for-the-badge&logo=materialdesign&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![License](https://img.shields.io/badge/Licen%C3%A7a-CC--BY--4.0-29b6f6?style=for-the-badge)](LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-29b6f6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/takwaratec/Mentoria_Comunidades_RaioX)

---

**Transforme seu grupo de WhatsApp em um Ativo Estratégico de Inteligência Corporativa.**

Este repositório contém a documentação da metodologia **Comunidade Raio-X**, um sistema prático baseado em 7 passos para mentores e infoprodutores otimizarem seus grupos de alunos no WhatsApp, gerando alto engajamento, reduzindo suporte reativo e criando convergências de negócios para upsell de novos produtos.

---

## 📊 Impacto Comprovado

| Métrica | Antes do RX | Com RX | Redução |
|---------|:-----------:|:------:|:-------:|
| Horas/semana de suporte repetitivo | 12h | 3,6h | **-70%** |
| Rotatividade de alunos (churn) | 25% | 8% | **-68%** |
| Networking entre membros | 0 (inexistente) | Ativo e mapeado | **+∞** |
| Oportunidades de upsell | Nenhuma | Constante | **Novo canal** |

---

## 🚀 O que é a Comunidade Raio-X?

Muitos mentores possuem grupos de WhatsApp cheios, mas **frios e desorganizados**. O Método Comunidade Raio-X resolve essa dor através de:

1. 🧪 **Triagem Científica de Logs** — Conversão automática de históricos de conversas em perfis estruturados.
2. 🔗 **Mapeamento de Sinergias** — Cruzamento de dados de negócios entre os participantes para criar eixos temáticos.
3. 🧑‍🏫 **Curadoria e Acompanhamento Ativo** — Geração rápida de resumos de encontros síncronos (Zoom) e fixação de atalhos.
4. 🖥️ **Painel Interativo na Web** — Publicação de um relatório dinâmico (Raio-X) que serve de orientação para a comunidade.

---

## 🔄 Pipeline de Operação

```mermaid
graph LR
    A[Logs WhatsApp] --> B[Triagem com IA]
    B --> C[Diagnóstico de Perfis]
    C --> D[Rede de Sinergias]
    D --> E[Curadoria Ativa]
    E --> F[Painel Web do Aluno]
    F --> G[Fidelização & Upsell]
    style A fill:#29b6f6,color:#fff
    style G fill:#0288d1,color:#fff
```

---

## 📚 Os 7 Passos da Metodologia

| Passo | Descrição | Link |
|:-----:|-----------|:----:|
| **01** | Diagnóstico de quem precisa da otimização | [Abrir](docs/01_DIAGNOSTICO_PERSONA/PASSO_01_Persona.md) |
| **02** | Do caos e silêncio à clareza estratégica | [Abrir](docs/02_JORNADA_MENTORADO/PASSO_02_Jornada.md) |
| **03** | Modelos de entrega do produto | [Abrir](docs/03_ESTRUTURA_FORMATO/PASSO_03_Estrutura.md) |
| **04** | Rotinas de curadoria, IA e resumos Zoom | [Abrir](docs/04_ENTREGA_ACOMPANHAMENTO/PASSO_04_Entrega.md) |
| **05** | Modelos High Ticket e recorrência mensal | [Abrir](docs/05_PRECIFICACAO/PASSO_05_Precificacao.md) |
| **06** | Roteiro de copy e posicionamento | [Abrir](docs/06_OFERTA_NAMING/PASSO_06_Oferta.md) |
| **07** | Vendas consultivas e auditorias gratuitas | [Abrir](docs/07_ESTRATEGIA_VENDAS/PASSO_07_Vendas.md) |
| **📖** | Glossário de termos técnicos | [Abrir](docs/GLOSSARIO.md) |
| **📅** | Agende sua auditoria gratuita | [Abrir](docs/AGENDAMENTO.md) |

---

## 💻 Scripts

No diretório `scripts/`, você encontrará protótipos de automação para processamento de logs do WhatsApp:

```bash
python scripts/triagem_wapp_mock.py
```

---

## 🛠️ Rodar localmente

```bash
pip install mkdocs mkdocs-material
mkdocs serve
# Acesse: http://127.0.0.1:8000/
```

---

## 🌐 Deploy Automático

Este repositório possui **GitHub Actions** configurado. A cada push na branch `main`, o MkDocs faz o build automaticamente e publica em:

➡️ **https://takwaratec.github.io/Mentoria_Comunidades_RaioX/**

---

> [!TIP]
> Para visualizar todos os diagramas interativos, acesse a **[página principal no GitHub Pages](https://takwaratec.github.io/Mentoria_Comunidades_RaioX/)** — os gráficos Mermaid são renderizados dinamicamente no navegador.

---
&copy; 2026 Comunidade Raio-X. Todos os direitos reservados.
