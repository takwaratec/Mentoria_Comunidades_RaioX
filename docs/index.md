# 🔬 Comunidade Raio-X

<div class="rx-logo-header">
    <img src="assets/images/logo-comunidade-raiox.svg" alt="Logo Comunidade Raio-X">
    <div>
        <strong>Comunidade Raio-X</strong><br>
        <span style="color: var(--md-default-fg-color--light, #666); font-size: 0.9rem;">Método de Gestão, Curadoria Ativa e Conversão para Grupos de WhatsApp &amp; Mentorias</span>
    </div>
</div>

<img src="assets/images/banner-comunidade-raiox.png" alt="Banner Comunidade Raio-X" style="width:100%; max-width:800px; display:block; margin:10px auto; border-radius:8px;">

---

## 📊 Painel de Impacto

<div class="rx-metrics">
    <div class="rx-mcard">
        <div class="rx-mcard-val">-70%</div>
        <div class="rx-mcard-label">Suporte Repetitivo</div>
    </div>
    <div class="rx-mcard">
        <div class="rx-mcard-val">-68%</div>
        <div class="rx-mcard-label">Churn de Alunos</div>
    </div>
    <div class="rx-mcard">
        <div class="rx-mcard-val">3,4×</div>
        <div class="rx-mcard-label">ROI no Primeiro Ano</div>
    </div>
    <div class="rx-mcard">
        <div class="rx-mcard-val">+∞</div>
        <div class="rx-mcard-label">Novas Oportunidades</div>
    </div>
</div>

### 💰 Retorno sobre Investimento (Anual)

<div class="rx-chart">
    <div class="rx-chart-title">Setup (único) × Economia Anual × Upsells</div>
    <div class="rx-chart-inner">
        <div class="rx-bar-wrap">
            <div class="rx-bar rx-bar-b1" style="height:46px">R$ 8k</div>
            <div class="rx-label">Setup<br><span class="rx-sublabel">custo único</span></div>
        </div>
        <div class="rx-bar-wrap">
            <div class="rx-bar rx-bar-b2" style="height:132px">R$ 25k</div>
            <div class="rx-label">Economia<br><span class="rx-sublabel">-70% suporte</span></div>
        </div>
        <div class="rx-bar-wrap">
            <div class="rx-bar rx-bar-b3" style="height:154px">R$ 35k</div>
            <div class="rx-label">Upsells<br><span class="rx-sublabel">novos negócios</span></div>
        </div>
    </div>
</div>

### ⏱ Carga de Suporte Semanal

<div class="rx-chart">
    <div class="rx-chart-title">Antes × Depois da Implantação do RX</div>
    <div class="rx-chart-inner">
        <div class="rx-bar-wrap">
            <div class="rx-bar rx-bar-b4" style="height:154px">12h</div>
            <div class="rx-label">Antes do RX</div>
        </div>
        <div class="rx-bar-wrap">
            <div class="rx-bar rx-bar-b2" style="height:46px">3,6h</div>
            <div class="rx-label">Com RX<br><span class="rx-sublabel">-70%</span></div>
        </div>
    </div>
</div>

### 📈 Benefícios Acumulados

```mermaid
%%{init: {'theme':'base','themeVariables': {'background': 'transparent','primaryColor': '#1565c0','primaryTextColor': '#1a1a1a','lineColor': '#0288d1','fontSize': '14px','pie1': '#42a5f5','pie2': '#66bb6a','pie3': '#ffa726','pie4': '#29b6f6','pie5': '#9ccc65'}}}%%
pie showData
    title Distribuição dos Benefícios do Método RX
    "Redução de Suporte" : 30
    "Fidelização (Churn↓)" : 25
    "Upsells & Cross-Selling" : 20
    "Networking entre Membros" : 15
    "Autoridade do Mentor" : 10
```

---

> 🚨 **Sua comunidade de mentoria é gerida de forma reativa — ou sofre com silêncio e scroll infinito?** Descubra o ecossistema que reduz em até **70% o suporte básico** e ativa conexões de negócios entre seus membros, publicando painéis dinâmicos e resumos inteligentes direto na Web (**GitHub Pages & Vercel**).
>
> ➡️ **[Aprenda o Método](03_ESTRUTURA_FORMATO/PASSO_03_Estrutura.md)** ou **[Contrate a Operação Técnica](05_PRECIFICACAO/PASSO_05_Precificacao.md)**

---

## 🧭 O Ecossistema da Metodologia

```mermaid
%%{init: {'theme':'base','themeVariables': {'background': 'transparent','primaryColor': '#29b6f6','primaryTextColor': '#fff','lineColor': '#4fc3f7','fontSize': '14px','tertiaryColor': '#e1f5fe'}}}%%
graph TB
    subgraph Entrada["📥 Extração & Dados Brutos"]
        A1[Logs WhatsApp] --> A2[Triagem com IA]
        A3[Dados Alunos] --> A2
    end
    subgraph Processamento["⚙️ Engenharia de Operações"]
        B1[Diagnóstico de Perfis] --> B2[Rede de Sinergias]
        B2 --> B3[Curadoria Ativa]
        B3 --> B4[Resumos Pós-Zoom]
    end
    subgraph Entrega["🚀 Delivery & Valor"]
        C1[Painel Web] --> C2[Atalhos & Fixados]
        C2 --> C3[Networking Ativo]
        C3 --> C4[Oportunidades Upsell]
    end
    A2 --> B1
    B4 --> C1
    style Entrada fill:#29b6f622,stroke:#29b6f6,stroke-width:2px
    style Processamento fill:#0288c722,stroke:#0288c7,stroke-width:2px
    style Entrega fill:#01579b22,stroke:#01579b,stroke-width:2px
```

---

## 🗺️ Timeline de Implementação

<div class="rx-timeline">
    <div class="rx-tl-phase">📋 Diagnóstico</div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-done">Concluído</span>
        <div class="rx-tl-title">Extração de Logs Históricos</div>
        <div class="rx-tl-desc">Exportação e higienização dos logs do WhatsApp</div>
    </div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-done">Concluído</span>
        <div class="rx-tl-title">Triagem de Perfis (IA)</div>
        <div class="rx-tl-desc">Processamento com IA para diagnóstico individual</div>
    </div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-done">Concluído</span>
        <div class="rx-tl-title">Mapa de Sinergias Iniciais</div>
        <div class="rx-tl-desc">Cruzamento: nicho × localização × redes</div>
    </div>
    <div class="rx-tl-phase">⚙️ Infraestrutura</div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-active">Fazendo</span>
        <div class="rx-tl-title">Setup Repositório Git</div>
        <div class="rx-tl-desc">Banco de dados estruturado no GitHub</div>
    </div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-active">Fazendo</span>
        <div class="rx-tl-title">Deploy GitHub Pages / Vercel</div>
        <div class="rx-tl-desc">Painel interativo publicado na web</div>
    </div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-active">Fazendo</span>
        <div class="rx-tl-title">Scripts de Curadoria</div>
        <div class="rx-tl-desc">Automação de triagem e resumos</div>
    </div>
    <div class="rx-tl-phase">🚀 Operação Contínua</div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-future">Recorrente</span>
        <div class="rx-tl-title">Curadoria Semanal</div>
        <div class="rx-tl-desc">Atualização do painel com novos membros</div>
    </div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-future">Recorrente</span>
        <div class="rx-tl-title">Resumos Pós-Zoom</div>
        <div class="rx-tl-desc">Resumos executivos em até 2 horas</div>
    </div>
    <div class="rx-tl-item">
        <span class="rx-tl-tag rx-tag-future">Recorrente</span>
        <div class="rx-tl-title">Relatórios de Sinergia</div>
        <div class="rx-tl-desc">Alertas de conexões estratégicas</div>
    </div>
</div>

---

## 📈 Posicionamento de Mercado

<div class="rx-pos">
  <div class="rx-pos-header">
    <div class="rx-pos-label-y">Alto Preço ▲</div>
    <div class="rx-pos-grid">
      <div class="rx-pos-q rx-pos-q1">
        <span class="rx-pos-tag">Tradicional</span>
        <div class="rx-pos-dots">
          <span class="rx-pos-dot" style="background:#e65100" title="CM Tradicional">CM</span>
          <span class="rx-pos-dot" style="background:#78909c" title="Suporte Interno">SI</span>
        </div>
        <div class="rx-pos-desc">Moderação manual<br>Baixo valor agregado</div>
      </div>
      <div class="rx-pos-q rx-pos-q2">
        <span class="rx-pos-tag">⭐ Premium (RX)</span>
        <div class="rx-pos-dots">
          <span class="rx-pos-dot" style="background:#1565c0" title="Comunidade Raio-X">RX</span>
          <span class="rx-pos-dot" style="background:#6a1b9a" title="Agência Digital">AD</span>
        </div>
        <div class="rx-pos-desc">Engenharia de dados + IA<br>Alto valor agregado</div>
      </div>
      <div class="rx-pos-q rx-pos-q3">
        <span class="rx-pos-tag">Amador</span>
        <div class="rx-pos-dots">
          <span class="rx-pos-dot" style="background:#c62828" title="Gestão Amadora">GA</span>
        </div>
        <div class="rx-pos-desc">Grupo largado<br>Perda total de valor</div>
      </div>
      <div class="rx-pos-q rx-pos-q4">
        <span class="rx-pos-tag">Superfaturado</span>
        <div class="rx-pos-dots"></div>
        <div class="rx-pos-desc">Preço alto sem entrega<br>proporcional</div>
      </div>
    </div>
    <div class="rx-pos-label-x">
      <span>Baixo Valor</span>
      <span>Alto Valor →</span>
    </div>
  </div>

  <div class="rx-pos-cards">
    <div class="rx-pos-card" style="border-left-color:#1565c0">
      <span class="rx-pos-dot-sm" style="background:#1565c0"></span>
      <strong>Comunidade Raio-X</strong> — Alto valor, preço premium justo
    </div>
    <div class="rx-pos-card" style="border-left-color:#e65100">
      <span class="rx-pos-dot-sm" style="background:#e65100"></span>
      <strong>CM Tradicional</strong> — Só moderação manual, baixo valor
    </div>
    <div class="rx-pos-card" style="border-left-color:#c62828">
      <span class="rx-pos-dot-sm" style="background:#c62828"></span>
      <strong>Gestão Amadora</strong> — Grupo abandonado, sem engajamento
    </div>
    <div class="rx-pos-card" style="border-left-color:#6a1b9a">
      <span class="rx-pos-dot-sm" style="background:#6a1b9a"></span>
      <strong>Agência Digital</strong> — Preço alto, entrega genérica
    </div>
    <div class="rx-pos-card" style="border-left-color:#78909c">
      <span class="rx-pos-dot-sm" style="background:#78909c"></span>
      <strong>Suporte Interno</strong> — Equipe própria sem método
    </div>
  </div>
</div>

---

## 🧩 Os 7 Pilares do Método

<div class="rx-pilares">
    <div class="rx-pilar rx-p1">
        <div class="rx-pilar-num">Passo 01</div>
        <div class="rx-pilar-nome">Persona</div>
        <ul><li>Diagnóstico da Dor</li><li>Perfil Ideal (ICP)</li><li>Mapeamento de Frustrações</li></ul>
    </div>
    <div class="rx-pilar rx-p2">
        <div class="rx-pilar-num">Passo 02</div>
        <div class="rx-pilar-nome">Jornada</div>
        <ul><li>Do Caos à Clareza</li><li>Pontos de Contato</li><li>Gatilhos de Engajamento</li></ul>
    </div>
    <div class="rx-pilar rx-p3">
        <div class="rx-pilar-num">Passo 03</div>
        <div class="rx-pilar-nome">Estrutura</div>
        <ul><li>Formato do Produto</li><li>Entrega Assíncrona</li><li>Stack Tecnológica</li></ul>
    </div>
    <div class="rx-pilar rx-p4">
        <div class="rx-pilar-num">Passo 04</div>
        <div class="rx-pilar-nome">Entrega</div>
        <ul><li>Curadoria Ativa</li><li>Resumos Pós-Zoom</li><li>Automação com IA</li></ul>
    </div>
    <div class="rx-pilar rx-p5">
        <div class="rx-pilar-num">Passo 05</div>
        <div class="rx-pilar-nome">Precificação</div>
        <ul><li>High Ticket</li><li>Recorrência Mensal</li><li>ROI do Cliente</li></ul>
    </div>
    <div class="rx-pilar rx-p6">
        <div class="rx-pilar-num">Passo 06</div>
        <div class="rx-pilar-nome">Oferta</div>
        <ul><li>Copy &amp; Naming</li><li>Promessa de Aceleração</li><li>Bônus Irresistíveis</li></ul>
    </div>
    <div class="rx-pilar rx-p7">
        <div class="rx-pilar-num">Passo 07</div>
        <div class="rx-pilar-nome">Aquisição</div>
        <ul><li>Auditoria Gratuita</li><li>Vendas Consultivas</li><li>Prova Social</li></ul>
    </div>
</div>

---

## 🌟 Prova Social

<div class="rx-test">
    "Depois da implantação do Raio-X, meu grupo de WhatsApp deixou de ser um depósito de avisos. Em 15 dias, dois alunos fecharam uma parceria que nunca teriam descoberto sem o mapeamento de sinergias."
    <cite>— Mentor de Alta Performance (SP)</cite>
</div>

<div class="rx-test">
    "O resumo pós-Zoom em 2 horas mudou o engajamento. Minha equipe economiza 12h por semana."
    <cite>— Infoprodutor Health &amp; Wellness (MG)</cite>
</div>

---

## 🚀 Navegue pelos 7 Passos

<div class="rx-stepper">
<a href="01_DIAGNOSTICO_PERSONA/PASSO_01_Persona.md"><span class="rx-step-num">1</span> Diagnóstico da Persona</a>
<a href="02_JORNADA_MENTORADO/PASSO_02_Jornada.md"><span class="rx-step-num">2</span> Jornada do Mentorado</a>
<a href="03_ESTRUTURA_FORMATO/PASSO_03_Estrutura.md"><span class="rx-step-num">3</span> Estrutura e Formato</a>
<a href="04_ENTREGA_ACOMPANHAMENTO/PASSO_04_Entrega.md"><span class="rx-step-num">4</span> Entrega e Acompanhamento</a>
<a href="05_PRECIFICACAO/PASSO_05_Precificacao.md"><span class="rx-step-num">5</span> Precificação</a>
<a href="06_OFERTA_NAMING/PASSO_06_Oferta.md"><span class="rx-step-num">6</span> Oferta e Naming</a>
<a href="07_ESTRATEGIA_VENDAS/PASSO_07_Vendas.md"><span class="rx-step-num">7</span> Canais de Aquisição</a>
</div>

---

## 📖 Glossário

Termos como *High Ticket*, *ICP*, *Cross-Selling* ou *Churn* explicados em português no **[Glossário do Método](GLOSSARIO.md)**.

👉 **[Acessar Glossário →](GLOSSARIO.md)**

---

## 🛠️ Rodar Localmente

```bash
pip install mkdocs mkdocs-material
mkdocs serve
# http://127.0.0.1:8000/
```

---

<div class="rx-cta">
    <h3>🚀 Pronto para transformar sua comunidade?</h3>
    <p><strong>1️⃣</strong> <a href="https://takwaratec.github.io/Mentoria_Comunidades_RaioX/03_ESTRUTURA_FORMATO/PASSO_03_Estrutura.html">Aprenda o método e faça você mesmo</a><br>
    <strong>2️⃣</strong> <a href="https://takwaratec.github.io/Mentoria_Comunidades_RaioX/05_PRECIFICACAO/PASSO_05_Precificacao.html">Contrate nossa operação técnica especializada</a><br>
    <strong>3️⃣</strong> <a href="https://takwaratec.github.io/Mentoria_Comunidades_RaioX/AGENDAMENTO.html">Agende uma auditoria gratuita do seu grupo</a></p>
</div>


