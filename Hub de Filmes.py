import json; import os
Filmes_assistidos = Filmes_para_assistir = []
opcao_tela_inicial = tela_2 = 0

# Tela inicial 

def tela_inicial():
    global opcao_tela_inicial
    opcao_tela_inicial = (int(input(('''
[1] Lista de Filmes Assistidos 📃
[2] Lista de Filmes Para Assistir 📋
[3] Adicionar Filmes ➕
[4] Retirar Filmes ➖
[5] Sair ❌
                                     
O que você deseja acessar? '''))))

# Loop de funcionamento do programa

while opcao_tela_inicial != 5:
    tela_inicial()

# Listar filmes assistidos

    if opcao_tela_inicial == 1:
        if os.path.exists("Filmes_assistidos.json"):
            with open("Filmes_assistidos.json", "r") as arquivo:
                Filmes_assistidos = json.load(arquivo)
                print ("")
                for i, c in zip(Filmes_assistidos, range(0, len(Filmes_assistidos))):
                    print (f"({c+1}) {i}")
        else:
            print ("Não há filmes nesta lista.")
            with open("Filmes_assistidos.json", "w") as arquivo:
                json.dump(Filmes_assistidos, arquivo)
            Filmes_assistidos = []

# Listar filmes para assisitir

    if opcao_tela_inicial == 2:
        if os.path.exists("Filmes_para_assistir.json"):
            with open("Filmes_para_assistir.json", "r") as arquivo:
                Filmes_para_assistir = json.load(arquivo)
                print ("")
                for i, c in zip(Filmes_para_assistir, range(0, len(Filmes_para_assistir))):
                    print (f"({c+1}) {i}")
        else:
            print ("Não há filmes nesta lista.")
            with open("Filmes_para_assistir.json", "w") as arquivo:
                json.dump(Filmes_para_assistir, arquivo)
            Filmes_para_assistir = []

# Localizar onde adicionar filmes

    if opcao_tela_inicial == 3:
        tela_2 = int(input('''
[1] Filmes Assistidos
[2] Filmes Para Assistir
                           
Para qual lista você deseja adicionar um filme? '''))

# Adicionar filmes para Filmes_assistidos

        if tela_2 == 1:
            if os.path.exists("Filmes_assistidos.json"):
                with open("Filmes_assistidos.json", "r") as arquivo:
                    Filmes_assistidos = json.load(arquivo)
            else:
                Filmes_assistidos = []
            print ("")
            Filmes_assistidos.append(str(input("Adicione seu filme: ")))
            with open("Filmes_assistidos.json", "w") as arquivo:
                json.dump(Filmes_assistidos, arquivo)

# Adicionar filmes para Filmes_para_assistir

        if tela_2 == 2:
            if os.path.exists("Filmes_para_assistir.json"):
                with open("Filmes_para_assistir.json", "r") as arquivo:
                    Filmes_para_assistir = json.load(arquivo)
            else:
                Filmes_para_assistir = []
            print ("")
            Filmes_para_assistir.append(str(input("Adicione seu filme: ")))
            with open("Filmes_para_assistir.json", "w") as arquivo:
                json.dump(Filmes_para_assistir, arquivo)

# Localizar de onde retirar filmes 

    if opcao_tela_inicial == 4:
        tela_2_2 = int(input('''
[1] Filmes Assistidos
[2] Filmes Para Assistir
                             
De qual lista você deseja retirar um filme? '''))
        
# Retirar filmes de Filmes_assistidos

        if tela_2_2 == 1:
            if os.path.exists("Filmes_assistidos.json"):
                with open("Filmes_assistidos.json", "r") as arquivo:
                    Filmes_assistidos = json.load(arquivo)
            else:
                Filmes_assistidos = []
            print ("")
            for i, c in zip(Filmes_assistidos, range(0, len(Filmes_assistidos))):
                print (f"({c+1}) {i}")
            print ("")
            Filmes_assistidos.remove(Filmes_assistidos[(int(input('Remova seu filme: '))-1)])
            with open("Filmes_assistidos.json", "w") as arquivo:
                json.dump(Filmes_assistidos, arquivo)
                
# Retirar filmes de Filmes_para_assistir

        if tela_2_2 == 2:
            if os.path.exists("Filmes_para_assistir.json"):
                with open("Filmes_para_assistir.json", "r") as arquivo:
                    Filmes_para_assistir = json.load(arquivo)
            else:
                Filmes_para_assistir = []
            with open("Filmes_para_assistir.json", "w") as arquivo:
                json.dump(Filmes_para_assistir, arquivo)
            print ("")
            for i, c in zip(Filmes_para_assistir, range(0, len(Filmes_para_assistir))):
                print (f"({c+1}) {i}")
            print ("")
            Filmes_para_assistir.remove(Filmes_para_assistir[(int(input('Remova seu filme: '))-1)])
            with open("Filmes_para_assistir.json", "w") as arquivo:
                json.dump(Filmes_para_assistir, arquivo)