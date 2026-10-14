# Assistente de IA - Professor de Programação com OpenRouter

Este projeto é um assistente de Inteligência Artificial interativo que utiliza a API do **OpenRouter** e possui uma **persona customizada de um professor de programação**, focado em explicar conceitos técnicos, tirar dúvidas de código e incentivar boas práticas de desenvolvimento de forma didática.

---

##  Funcionalidades

- **Persona de Professor:** Configurado via prompt de sistema (`system role`) para adotar uma postura paciente, didática, profissional e voltada ao ensino de programação.
- **Histórico de Conversa:** Mantém o contexto de todo o papo durante a execução para que você possa tirar dúvidas sequenciais sobre códigos.
- **Loop Interativo via Terminal:** Funciona continuamente até que o usuário digite `sair`.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `openai`** (compatível com a API do OpenRouter)
- **OpenRouter API** (utilizando modelos gratuitos, como `openrouter/free`)

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar as dependências
```bash
pip install openai
```

### 3. Configurar a Chave da API (OpenRouter)
Para evitar expor sua chave de API publicamente no código, utilize uma variável de ambiente:

- **No Linux / macOS:**
  ```bash
  export OPENROUTER_API_KEY="sua_chave_aqui"
  ```

- **No Windows (Prompt de Comando):**
  ```cmd
  set OPENROUTER_API_KEY=sua_chave_aqui
  ```

- **No Windows (PowerShell):**
  ```powershell
  $env:OPENROUTER_API_KEY="sua_chave_aqui"
  ```

*(Nota: Se a variável de ambiente não estiver configurada, o script pedirá para você colar a chave diretamente no terminal ao iniciar).*

### 4. Executar o Assistente
```bash
python main.py
```

---

##  Exemplo de Uso no Terminal

```text
Assistente de Programação pronto! Digite 'sair' para encerrar.

Faça uma pergunta: O que é uma função em Python e para que serve?
Resposta do Professor:
Olá! Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica...
```
