# 📺 Xtream Universal IPTV

Add-on universal para Kodi compatível com qualquer servidor Xtream Codes.

## 📖 Sobre

O **Xtream Universal IPTV** é um add-on completo para Kodi que permite assistir TV ao vivo, filmes e séries de **qualquer servidor Xtream Codes**. Diferente de outros add-ons que funcionam apenas com servidores específicos, este é totalmente universal e independente.

## ✨ Recursos

- ✅ **Universal** - Compatível com qualquer servidor Xtream Codes
- ✅ **TV ao Vivo** - Assista canais ao vivo
- ✅ **Filmes** - Acesso completo ao catálogo VOD
- ✅ **Séries** - Todas as temporadas e episódios
- ✅ **EPG** - Guia de programação eletrônico
- ✅ **TMDB** - Metadados, posters e sinopses
- ✅ **F4M Proxy** - Melhor qualidade de streaming
- ✅ **Controle Parental** - Proteção por PIN para conteúdo +18
- ✅ **Busca Global** - Procure em todos os tipos de conteúdo
- ✅ **Informações da Conta** - Veja status, validade e conexões

## 🚀 Instalação

### Método 1: Via Repositório (Recomendado)
1. Baixe o repositório: `https://keltecmp-repo.github.io/repo/`
2. No Kodi: **Add-ons** → **Install from zip file**
3. Selecione o arquivo do repositório
4. Aguarde notificação de instalação
5. **Install from repository** → **Xtream Universal Repository**
6. **Video add-ons** → **Xtream Universal IPTV**
7. Clique em **Install**

### Método 2: Instalação Manual
1. Baixe o arquivo: `plugin.video.xtream-universal-X.X.X.zip`
2. No Kodi: **Add-ons** → **Install from zip file**
3. Selecione o arquivo baixado
4. Aguarde notificação de instalação bem-sucedida

## ⚙️ Configuração Inicial

### Primeiro Uso

1. **Abra o add-on** pela primeira vez
2. Uma mensagem de boas-vindas aparecerá
3. As configurações abrirão automaticamente
4. **Configure suas credenciais Xtream:**

#### DNS do Servidor
Digite o endereço completo do seu servidor Xtream:
```
http://servidor.example.com:8080
http://192.168.1.100:25461
http://myiptv.tv:2086
```

#### Usuário
Digite seu nome de usuário Xtream

#### Senha
Digite sua senha Xtream

5. **Salve as configurações**
6. O add-on perguntará se deseja alterar o **PIN de adultos** (padrão: `0000`)
7. Pronto! O add-on está configurado e pronto para uso

### Testando as Credenciais

Para verificar se suas credenciais estão corretas, teste no navegador:
```
http://SEU_DNS:PORTA/player_api.php?username=SEU_USUARIO&password=SUA_SENHA
```

Exemplo:
```
http://servidor.com:8080/player_api.php?username=joao123&password=minhasenha
```

Se retornar informações em JSON, suas credenciais estão corretas!

## 📱 Como Usar

### Menu Principal

Ao abrir o add-on, você verá:

1. **Xtream Universal IPTV** - Informações sobre o add-on
2. **Informações da Conta** - Status, validade, conexões
3. **Pesquisa Global** - Busque em TV, filmes e séries
4. **TV (Canais Ao Vivo)** - Categorias de canais
5. **Filmes** - Categorias de filmes
6. **Séries** - Categorias de séries
7. **Configurações** - Ajustes do add-on
8. **Controle Parental** - Gerenciar PIN e bloqueios

### Assistindo Conteúdo

#### TV ao Vivo
1. Clique em **TV (Canais Ao Vivo)**
2. Escolha uma categoria
3. Selecione o canal
4. Se F4M estiver ativo, escolha o modo:
   - **HLSRETRY** - Para streams M3U8 (recomendado)
   - **TSDOWNLOADER** - Para streams TS

#### Filmes
1. Clique em **Filmes**
2. Escolha uma categoria
3. Selecione o filme
4. Reprodução inicia automaticamente

#### Séries
1. Clique em **Séries**
2. Escolha uma categoria
3. Selecione a série
4. Escolha a temporada
5. Selecione o episódio

### Busca Global

1. Clique em **Pesquisa Global**
2. Digite o que procura (nome do canal, filme ou série)
3. Resultados de TV, Filmes e Séries aparecerão juntos
4. Selecione o que deseja assistir

## 🔐 Controle Parental

### Configurando o Controle Parental

1. Abra **Controle Parental** no menu principal
2. Escolha uma opção:
   - **Ativar/Desativar** - Liga ou desliga a proteção
   - **Alterar PIN** - Muda o PIN (padrão: 0000)
   - **Desbloquear sessão** - Libera conteúdo +18 por 4 horas
   - **Bloquear sessão** - Bloqueia conteúdo +18 imediatamente

### Como Funciona

- Categorias e conteúdos com palavras-chave adultas são automaticamente protegidos
- Palavras-chave: `adult`, `adulto`, `18+`, `xxx`, `+18`, `hot`, `sexy`
- Ao tentar acessar, será solicitado o PIN
- Sessão desbloqueada dura **4 horas**
- Após 4 horas, precisa digitar o PIN novamente

## 🎨 TMDB (The Movie Database)

### Ativando TMDB

1. Vá em **Configurações**
2. Aba **TMDB - Metadados**
3. Ative **Ativar TMDB**
4. (Opcional) Cole sua **API Key do TMDB**

### Obtendo API Key TMDB

1. Acesse https://www.themoviedb.org/
2. Crie uma conta (gratuita)
3. Vá em **Configurações** → **API**
4. Solicite uma chave de API
5. Cole no add-on

### Benefícios do TMDB

- 🎬 Posters de alta qualidade
- 📝 Sinopses detalhadas
- ⭐ Avaliações e notas
- 👥 Elenco e equipe
- 📅 Datas de lançamento

## 🔧 Configurações Avançadas

### F4M Proxy

**O que é:**
Sistema de proxy local que melhora a reprodução de canais ao vivo.

**Configurações:**
- **Usar F4MTESTER** - Ativa/desativa o proxy
- **Ativar Proxy HTTP** - Inicia servidor local

**Modos disponíveis:**
- **HLSRETRY** - Para streams .m3u8 (recomendado)
- **TSDOWNLOADER** - Para streams .ts

### EPG (Guia de Programação)

**O que é:**
Mostra a programação dos canais (quando disponível no servidor).

**Configuração:**
- Vá em **Configurações** → **EPG**
- Ative **Ativar EPG**

### Modo Debug

Para diagnóstico de problemas:

1. **Configurações** → **Avançado**
2. Ative **Modo Debug**
3. Logs detalhados aparecerão no Kodi
4. Útil para reportar problemas

## ❓ Perguntas Frequentes

### Preciso de conta Xtream Codes?

Sim. Este add-on é um **player**, não fornece listas IPTV. Você precisa de:
- DNS do servidor
- Usuário
- Senha

Estes dados são fornecidos pelo seu provedor IPTV.

### O add-on funciona com M3U?

Não. Este add-on é específico para **servidores Xtream Codes**.

Para listas M3U, use:
- **IPTV Simple Client** (nativo do Kodi)
- **Outros add-ons compatíveis com M3U**

### Posso usar com vários servidores?

Atualmente, o add-on suporta **um servidor por vez**.

Para trocar de servidor:
1. Vá em **Configurações**
2. Altere DNS, usuário e senha
3. Reabra o add-on

### Esqueci meu PIN de controle parental!

1. Vá em **Configurações do Kodi**
2. **Add-ons** → **Meus add-ons** → **Video add-ons**
3. **Xtream Universal IPTV** → **Configurar**
4. Aba **Controle Parental**
5. Altere o campo **PIN** manualmente

OU

Delete o arquivo de configuração:
```
userdata/addon_data/plugin.video.xtream-universal/settings.xml
```

### Canais não estão carregando

Verifique:

1. ✅ **Credenciais corretas** - Teste no navegador
2. ✅ **Servidor online** - Pergunte ao seu provedor
3. ✅ **Internet estável** - Teste sua conexão
4. ✅ **Data de validade** - Veja em "Informações da Conta"

### Filmes/séries travando

1. **Desative o F4M Proxy** para VOD:
   - Configurações → F4M Proxy
   - Desative "Usar F4MTESTER"

2. **Ajuste o cache do Kodi**:
   - Edite `advancedsettings.xml`
   - Aumente o buffer de vídeo

3. **Teste outro servidor DNS**

## 🐛 Reportando Problemas

Se encontrar bugs ou problemas:

1. **Ative o Modo Debug**
2. **Reproduza o problema**
3. **Copie os logs do Kodi**:
   - Windows: `%APPDATA%\Kodi\kodi.log`
   - Linux: `~/.kodi/temp/kodi.log`
   - Android: `/sdcard/Android/data/org.xbmc.kodi/files/.kodi/temp/kodi.log`

4. **Reporte com detalhes:**
   - Versão do Kodi
   - Versão do add-on
   - Sistema operacional
   - Descrição do problema
   - Logs (se possível)

## 📜 Licença

GNU General Public License v3.0

## ⚠️ Aviso Legal

Este add-on é um **player** para servidores Xtream Codes.

**Os autores NÃO:**
- ❌ Hospedam conteúdo
- ❌ Distribuem listas IPTV
- ❌ Fornecem credenciais
- ❌ São afiliados a provedores IPTV

Você é responsável por:
- ✅ Obter suas próprias credenciais legalmente
- ✅ Uso do conteúdo de acordo com leis locais
- ✅ Respeitar direitos autorais

## 🙏 Créditos

- **TMDB Helper** - Metadados de filmes e séries
- **F4M Proxy** - Otimização de streaming
- **Comunidade Kodi** - Suporte e feedback

---

**Desenvolvido com ❤️ para a comunidade Kodi**

**Versão:** 1.0.0 (31/03/2026)
