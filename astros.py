import time
import random

# Base de dados dos astros com perguntas
astros = {
    "1": {
        "nome": "Lua 🌕",
        "perguntas": [
            {"texto": "Você acredita que a Lua influencia nas emoções humanas? (s/n): ", "resposta": "s"},
            {"texto": "A Lua é um planeta? (s/n): ", "resposta": "n"}
        ],
        "curiosidades": [
            "A Lua se afasta da Terra cerca de 3,8 cm por ano!",
            "A gravidade da Lua é 1/6 da gravidade da Terra."
        ]
    },
    "2": {
        "nome": "Júpiter 🪐",
        "perguntas": [
            {"texto": "Júpiter é o maior planeta do sistema solar? (s/n): ", "resposta": "s"},
            {"texto": "Júpiter possui anéis visíveis como os de Saturno? (s/n): ", "resposta": "n"}
        ],
        "curiosidades": [
            "Júpiter tem mais de 90 luas!",
            "A tempestade vermelha de Júpiter tem mais de 300 anos."
        ]
    },
    "3": {
        "nome": "Saturno 💫",
        "perguntas": [
            {"texto": "Os anéis de Saturno são feitos de gelo e poeira? (s/n): ", "resposta": "s"},
            {"texto": "Saturno é o segundo maior planeta do sistema solar? (s/n): ", "resposta": "s"}
        ],
        "curiosidades": [
            "Os anéis de Saturno têm milhares de quilômetros de extensão!",
            "Saturno tem ventos que podem chegar a 1.800 km/h."
        ]
    }
}

pontuacao = 0

def exibir_intro():
    print("🚀🌌 Bem-vinda, comandante Thami, à missão: Exploradora dos Astros!")
    print("Prepare-se para uma jornada cósmica cheia de descobertas.\n")
    time.sleep(1.5)

def mostrar_curiosidade(astro):
    curiosidade = random.choice(astros[astro]["curiosidades"])
    print(f"\n🌠 Curiosidade sobre {astros[astro]['nome']}: {curiosidade}")

def visitar_astro(astro):
    global pontuacao
    print(f"\nVocê está visitando {astros[astro]['nome']}")
    for pergunta in astros[astro]["perguntas"]:
        resposta = input(pergunta["texto"]).strip().lower()
        if resposta == pergunta["resposta"]:
            print("✅ Resposta correta!\n")
            pontuacao += 1
        else:
            print("❌ Resposta incorreta!\n")
        time.sleep(1)
    mostrar_curiosidade(astro)
    input("\nPressione Enter para voltar ao menu...")

def ver_pontuacao():
    print(f"\n⭐ Você acertou {pontuacao} perguntas até agora!")

def encerrar_missao():
    print("\n🛑 Missão finalizada, comandante Thami!")
    print(f"Você acumulou {pontuacao} pontos cósmicos.")
    if pontuacao >= 5:
        print("🌟 Você é uma verdadeira exploradora das galáxias!")
    elif pontuacao >= 3:
        print("💫 Boa viagem, comandante! Continue estudando os astros!")
    else:
        print("🌑 Missão básica concluída. Há muito mais para explorar!")
    print("Volte sempre para mais descobertas entre as estrelas!\n")

def menu_principal():
    while True:
        print("\n✨ MENU GALÁCTICO ✨")
        print("1. Visitar a Lua 🌕")
        print("2. Visitar Júpiter 🪐")
        print("3. Visitar Saturno 💫")
        print("4. Ver minha pontuação ⭐")
        print("5. Encerrar missão ❌")

        escolha = input("Digite o número da sua escolha: ").strip()

        if escolha in astros:
            visitar_astro(escolha)
        elif escolha == "4":
            ver_pontuacao()
        elif escolha == "5":
            encerrar_missao()
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Início da missão
exibir_intro()
menu_principal()