import os
import time

senha_real = input("Digite a senha: ")

caracteres = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

senha_descoberta = ""
tentativas = 0

print("\nIniciando ataque...\n")

for i in range(len(senha_real)):
    for c in caracteres:
        tentativas += 1
        tentativa_atual = senha_descoberta + c
        print(f"Tentando: {tentativa_atual}")

        if c == senha_real[i]:
            senha_descoberta += c
            print(f"Caractere encontrado: '{c}'")
            print(f"Senha descoberta até agora: {senha_descoberta}\n")
            time.sleep(0.3)  
            
            os.system("cls" if os.name == "nt" else "clear")
            break

print(f"\nSenha encontrada: {senha_descoberta}")
print(f"Número total de tentativas: {tentativas}")
