from openai import OpenAI
import os

# Carrega a chave da API do OpenRouter via variável de ambiente (ou solicita caso não esteja definida)
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    api_key = input("Digite a sua chave da API:")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

mensagens = [
    {
        "role": "system",
        "content": (
            "Você é um professor de programação experiente e paciente.\n"
            "Seu objetivo é ajudar alunos a aprenderem a programar, tirando dúvidas de código, "
            "explicando conceitos técnicos de forma clara e dando dicas de boas práticas.\n"
            "Regras:\n"
            "- Seja didático, encorajador e profissional.\n"
            "- Sempre que possível, utilize exemplos práticos de código para ilustrar suas explicações."
        )
    }
]

print("\nAssistente de Programação pronto! Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Faça uma pergunta: ")

    if pergunta.lower() == "sair":
        break

    mensagens.append({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="openrouter/free", 
        messages=mensagens
    )

    texto_resposta = resposta.choices[0].message.content

    print("\nResposta do Professor:")
    print(texto_resposta)

    mensagens.append({"role": "assistant", "content": texto_resposta})