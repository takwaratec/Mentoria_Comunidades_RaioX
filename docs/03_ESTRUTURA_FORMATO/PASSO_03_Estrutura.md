# Passo 03: Estrutura e Formato do Produto

Neste passo, detalhamos como estruturar e empacotar a metodologia Comunidade Raio-X em produtos vendáveis de alto valor no mercado digital.

---

## 📦 Os 3 Modelos de Empacotamento

Recomendamos que você ofereça este serviço em três formatos distintos, dependendo da necessidade do cliente:

### 1. Consultoria de Implantação RX (Setup Completo)
Ideal para mentores ocupados que querem delegar a solução completa ("Done-For-You").
* **O que inclui:**
  * Importação e higienização histórica de logs do grupo do WhatsApp de turmas passadas ou da atual.
  * Criação do Banco de Dados consolidado estruturado diretamente no GitHub (JSON/Markdown).
  * Estruturação e publicação do painel dinâmico da Web (HTML/MkDocs) personalizado com a identidade da marca do cliente.
  * Entrega do roteiro de fixação de descrição e boas-vindas do grupo.
  * Suporte por 30 dias.
* **Prazo de entrega:** 7 a 10 dias úteis.

### 2. Mentoria de Implementação Coletiva (Aprenda e Delegue)
Ideal para equipes internas de grandes mentores que querem aprender o método ("Done-With-You").
* **O que inclui:**
  * 4 encontros ao vivo em grupo explicando o fluxo de ferramentas (WhatsApp export -> Script python/IA -> GitHub -> MkDocs/Git).
  * Acesso a modelos prontos de scripts e planilhas.
  * Acompanhamento prático da triagem da turma atual do mentor.
* **Duração:** 4 semanas.

### 3. Recorrência Mensal de Curadoria & Resumos Zoom (Suporte Contínuo)
Serviço recorrente que garante a manutenção da saúde do grupo durante o andamento da mentoria.
* **O que inclui:**
  * Atualização diária (ou 2x a 3x por semana, a depender da movimentação do grupo) do painel web Raio-X com novas apresentações.
  * Curadoria ativa de novos cases de sucesso.
  * Geração ágil de resumos pós-aula do Zoom (aulas gravadas são transformadas em resumos estruturados com atalhos fixados no grupo em até 2 horas pós-encontro).
* **Frequência:** Mensal.

---

## 🛠️ O Ecossistema de Ferramentas (Stack Tecnológica)

O método é executado de forma simples com as seguintes ferramentas integradas:

```
[Exportação WhatsApp] ➔ [Script Python / (Antigravity/Gemini ou Hermes/Warp/Deepseek) (IA)] ➔ [GitHub / Database (JSON/Markdown)] ➔ [MkDocs / HTML] ➔ [Hospedagem GitHub Pages / Vercel]
```

---

## 🚀 Diretrizes de Deploy: Do Protótipo (GitHub Pages) ao Painel Premium (Vercel)

Para colocar o painel no ar, seguimos dois caminhos distintos dependendo da complexidade do projeto do mentor:

### 1. Deploy do Protótipo MkDocs (GitHub Pages)
Ideal para a documentação metodológica e painéis estáticos simples de consulta rápida.

1. **Criação do Repositório Remoto:** Crie um repositório vazio no seu perfil do GitHub (ex: `ComunidadeRX-MinhaMentoria`).
2. **Vinculação do Repositório Local:**
   ```bash
   git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   git branch -M main
   git push -u origin main
   ```
3. **Publicação Automatizada:** Com o MkDocs configurado, execute o comando de deploy nativo. Ele compilará o HTML estático e publicará diretamente na branch remota `gh-pages`:
   ```bash
   mkdocs gh-deploy
   ```
   O site estará acessível imediatamente em: `https://SEU_USUARIO.github.io/SEU_REPOSITORIO/`.

### 2. Implantação do Painel Avançado/Dashboard (Vercel)
Ideal para sites dinâmicos baseados em frameworks robustos (Next.js, Nextra ou React Dashboards) com alto apelo estético, interatividade avançada e integrações de IA em tempo real.

1. **Estrutura do Projeto:** O site poderoso de produção utiliza um framework de alta performance (como Next.js) integrado à sua estrutura de repositórios no GitHub.
2. **Conexão Contínua (CI/CD):**
   * Crie uma conta gratuita na [Vercel](https://vercel.com) e vincule o seu perfil do GitHub.
   * Clique em **"Add New" ➔ "Project"** e selecione o repositório do seu painel de comunidade.
   * A Vercel detectará automaticamente o framework e configurará as instruções de build de forma padrão.
3. **Segurança de Credenciais (Variáveis de Ambiente):**
   * **NUNCA** insira chaves de API do Gemini/Deepseek ou tokens de bancos de dados diretamente nos arquivos de código.
   * No painel de configuração do projeto na Vercel, abra a aba **Environment Variables** e insira as suas chaves com segurança (ex: `GEMINI_API_KEY` ou `DEEPSEEK_API_KEY`).
4. **Deploy Automático em Produção:**
   * Clique em **"Deploy"**. A Vercel construirá o painel e fornecerá um domínio de produção com certificado SSL (ex: `suacomunidade-rx.vercel.app`).
   * A partir de agora, qualquer alteração enviada ao GitHub via `git push` disparará um novo deploy automático e seguro em tempo real.
