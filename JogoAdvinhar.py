from random import *
import webbrowser
from time import sleep
palpite = 0
computador = randint(0, 10)

print("\033[35m==== JOGO DA ADIVINHAÇÃO 2.0v ====\033[0m")
print()
print("\033[32mVoltei HAHAHAHAHAHA\033[0m")
sleep(1)
carregar = " "
for _ in range(5): #Repete 4 vezes
    for i in range(4): #3 pontos de carregamento
        carregar = "." * i
        print(f"\rGerando{carregar}", end="")
        sleep(0.3)
print()
print("GEREI um número de 0 a 10, BOA SORTE!!!")
sleep(1)
jogador = int(input("Tente advinhar o número que eu gerei: "))
palpite += 1
while jogador != computador:
    try:
        jogador = int(input("Tente Novamente: "))
        if jogador == computador:
            palpite += 1
            print("\033[32mVocê ganhou!!!\033[0m")
            break
        elif jogador > computador:
            palpite += 1
            print("\033[31mQuase ganha e mim, tente outra! 0 a 10\033[0m")
            print("Não vou perder pra você 😒")
            continue
        elif jogador < computador:
            palpite += 1
            print("\033[33mHMMMM... Falta um pouco, vai com calma 😨\033[0m")
            continue
    except ValueError:
        print("Número de 0 a 10. Não espaço ou letra, seu JEGE🙄")
print(f"Você precisou de {palpite} palpites para vencer de mim")
if palpite >= 7:
    print("Falta Melhorar sua jogada. Boa Sorte na próxima vez!")
else:
    print("Tá melhor que eu, na proxima tem revanche! 😑")
    webbrowser.open("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnhjNTF6cDR1a2c2amdkNW1uZDB1bG5pY2I4dXI1YXh5cmFsdnpnNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YDYyCghm60Olyibmcb/giphy.gif")
input("Aperta ENTER para sair...")