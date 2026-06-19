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

---

## 🔐 Segurança de Dados: Proteção por Senha, Links Expiráveis & Anti-Cópia na Vercel

Ao lidar com painéis na Vercel (especialmente na Modalidade B de Acompanhamento Técnico ou no envio de Prévia/Demo), é fundamental blindar a aplicação contra cópias e vazamento de dados dos alunos. Abaixo estão os códigos e fluxos práticos para implementar essa segurança.

### 1. Middleware de Autenticação por Senha e Token Temporal (Next.js)

Com o **Edge Middleware** do Next.js na Vercel, interceptamos a requisição antes de carregar a página e verificamos se o acesso está dentro do prazo contratado ou se a senha foi fornecida.

Crie o arquivo `middleware.js` na raiz do seu projeto Next.js:

```javascript
import { NextResponse } from 'next/server';
import { jwtVerify } from 'jose'; // Biblioteca leve para decodificar JWT na Edge

const JWT_SECRET = new TextEncoder().encode(process.env.JWT_SECRET || 'chave_secreta_padrao');

export async function middleware(request) {
  const { pathname, searchParams } = request.nextUrl;

  // 1. Proteger apenas as rotas de Painel e Demo
  if (pathname.startsWith('/raio-x') || pathname.startsWith('/demo')) {
    const token = searchParams.get('token') || request.cookies.get('rx-token')?.value;

    if (!token) {
      // Redireciona para página de login ou erro
      return NextResponse.redirect(new URL('/login', request.url));
    }

    try {
      // 2. Decodifica e verifica o Token de Tempo
      const { payload } = await jwtVerify(token, JWT_SECRET);
      
      // 3. Verifica se a sessão expirou
      const now = Math.floor(Date.now() / 1000);
      if (payload.exp && now > payload.exp) {
        // Token expirado (Ex: Passou das 2 horas acordadas para a Demo)
        return NextResponse.redirect(new URL('/expired', request.url));
      }

      // Se tudo estiver certo, prossegue para o painel
      const response = NextResponse.next();
      // Grava o cookie para navegação subsequente do aluno
      response.cookies.set('rx-token', token, { maxAge: 3600 * 12, httpOnly: true });
      return response;
      
    } catch (err) {
      // Token inválido ou adulterado
      return NextResponse.redirect(new URL('/login?error=invalid_token', request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/raio-x/:path*', '/demo/:path*'],
};
```

### 2. Bloqueio de Cópia e Seleção (Camada UX)

Para dificultar que o usuário copie os dados da tabela ou das sinergias, aplique as seguintes travas no frontend da aplicação:

#### CSS (Bloqueio de Seleção de Texto)
Adicione esta classe aos elementos da tabela ou de listagem no seu arquivo CSS global (`globals.css` ou `index.css`):
```css
.anti-copy {
  user-select: none; /* Chrome, Opera, Safari, Firefox */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
```

#### JavaScript (Bloqueio de Clique Direito e Atalhos de Teclado)
Adicione este hook no componente base do React/Next.js (`_app.js` ou no layout principal):
```javascript
import { useEffect } from 'react';

export default function AntiCopyWrapper({ children }) {
  useEffect(() => {
    // 1. Bloqueia o clique com o botão direito (menu de contexto)
    const handleContextMenu = (e) => e.preventDefault();
    document.addEventListener('contextmenu', handleContextMenu);

    // 2. Bloqueia atalhos comuns de cópia (Ctrl+C, Cmd+C, Ctrl+U para código fonte)
    const handleKeyDown = (e) => {
      const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
      const isCopy = (e.key === 'c' || e.key === 'C') && (isMac ? e.metaKey : e.ctrlKey);
      const isSourceCode = (e.key === 'u' || e.key === 'U') && (isMac ? e.metaKey : e.ctrlKey);
      
      if (isCopy || isSourceCode) {
        e.preventDefault();
        alert('🔒 A cópia de dados deste painel de segurança é restrita.');
      }
    };
    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('contextmenu', handleContextMenu);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  return <div className="anti-copy">{children}</div>;
}
```
