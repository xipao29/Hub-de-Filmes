import json; import os
Filmes_assistidos = Filmes_para_assistir = []
opcao_tela_inicial = tela_2 = tela_2_2 = 0
os.system('cls')

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
    try:
        tela_inicial()
    except ValueError:
        os.system('cls')

# Listar filmes assistidos

    while opcao_tela_inicial == 1:
        os.system('cls')
        if os.path.exists("Filmes_assistidos.json"):
            with open("Filmes_assistidos.json", "r") as arquivo:
                Filmes_assistidos = json.load(arquivo)
                print ("")
                for i, c in enumerate(Filmes_assistidos):
                    print (f"({(i+1)}) {c}")
        else:
            print ("Não há filmes nesta lista.")
            with open("Filmes_assistidos.json", "w") as arquivo:
                json.dump(Filmes_assistidos, arquivo)
            Filmes_assistidos = []
        opcao_tela_inicial = 0

# Listar filmes para assisitir

    while opcao_tela_inicial == 2:
        os.system('cls')
        if os.path.exists("Filmes_para_assistir.json"):
            with open("Filmes_para_assistir.json", "r") as arquivo:
                Filmes_para_assistir = json.load(arquivo)
                print ("")
                for i, c in enumerate(Filmes_para_assistir):
                    print (f"({(i+1)}) {c}")
        else:
            print ("Não há filmes nesta lista.")
            with open("Filmes_para_assistir.json", "w") as arquivo:
                json.dump(Filmes_para_assistir, arquivo)
            Filmes_para_assistir = []
        opcao_tela_inicial = 0

# Localizar onde adicionar filmes

    while opcao_tela_inicial == 3:
        try:
            os.system('cls')
            tela_2 = int(input('''
[1] Filmes Assistidos
[2] Filmes Para Assistir
                           
Para qual lista você deseja adicionar um filme? '''))
            opcao_tela_inicial = 0
        except ValueError:
            os.system('cls')

# Adicionar filmes para Filmes_assistidos

        while tela_2 == 1:
            os.system('cls')
            if os.path.exists("Filmes_assistidos.json"):
                with open("Filmes_assistidos.json", "r") as arquivo:
                    Filmes_assistidos = json.load(arquivo)
            else:
                Filmes_assistidos = []
            print ("")
            Filmes_assistidos.append(str(input("Adicione seu filme: ")))
            with open("Filmes_assistidos.json", "w") as arquivo:
                json.dump(Filmes_assistidos, arquivo)
                tela_2 = 0

# Adicionar filmes para Filmes_para_assistir

        while tela_2 == 2:
            os.system('cls')
            if os.path.exists("Filmes_para_assistir.json"):
                with open("Filmes_para_assistir.json", "r") as arquivo:
                    Filmes_para_assistir = json.load(arquivo)
            else:
                Filmes_para_assistir = []
            print ("")
            Filmes_para_assistir.append(str(input("Adicione seu filme: ")))
            with open("Filmes_para_assistir.json", "w") as arquivo:
                json.dump(Filmes_para_assistir, arquivo)
                tela_2 = 0

# Localizar de onde retirar filmes 

    while opcao_tela_inicial == 4:
        try:
            os.system('cls')
            tela_2_2 = int(input('''
[1] Filmes Assistidos
[2] Filmes Para Assistir
                             
De qual lista você deseja retirar um filme? '''))
            opcao_tela_inicial = 0
        except ValueError:
            os.system('cls')
        
# Retirar filmes de Filmes_assistidos

        while tela_2_2 == 1:
            try:
                os.system('cls')
                if os.path.exists("Filmes_assistidos.json"):
                    with open("Filmes_assistidos.json", "r") as arquivo:
                        Filmes_assistidos = json.load(arquivo)
                else:
                    Filmes_assistidos = []
                print ("")
                for i, c in enumerate(Filmes_assistidos):
                    print (f"({(i+1)}) {c}")
                print ("")
                Filmes_assistidos.remove(Filmes_assistidos[(int(input('Remova seu filme: '))-1)])
                with open("Filmes_assistidos.json", "w") as arquivo:
                    json.dump(Filmes_assistidos, arquivo)
                    tela_2_2 = 0
            except ValueError:
                os.system('cls')
                
# Retirar filmes de Filmes_para_assistir

        while tela_2_2 == 2:
            try:
                os.system('cls')
                if os.path.exists("Filmes_para_assistir.json"):
                    with open("Filmes_para_assistir.json", "r") as arquivo:
                        Filmes_para_assistir = json.load(arquivo)
                else:
                    Filmes_para_assistir = []
                with open("Filmes_para_assistir.json", "w") as arquivo:
                    json.dump(Filmes_para_assistir, arquivo)
                print ("")
                for i, c in enumerate(Filmes_para_assistir):
                    print (f"({(i+1)}) {c}")
                print ("")
                Filmes_para_assistir.remove(Filmes_para_assistir[(int(input('Remova seu filme: '))-1)])
                with open("Filmes_para_assistir.json", "w") as arquivo:
                    json.dump(Filmes_para_assistir, arquivo)
                    tela_2_2 = 0
            except ValueError:
                os.system('cls')