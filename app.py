import os 

carros = [("Chevrolet Tracker", 120),
          ("Chevrolet Onix", 130),
          ("Chevrolet Spin", 100)
          
          ]

alugados = []


print("============")

print("Bem vindo a locadora de carros!")

print("============")


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(f"[{i}] {car[0]} - R${car[1]}/dia.")
        
        
mostrar_lista_de_carros(carros)        

while True:
    os.system("cls")
    print("============")
    print("Bem vindo a locadora de carros!")
    print("============")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())
    
    os.system("cls")
    
    if op == 0:
        mostrar_lista_de_carros(carros)
    
    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("=========")
        print("Escolha o código do carro:")
        cod_carro = int(input())
        print("Por quantos dias voce deseja alugar este carro?")
        dias = int(input())
        os.system("cls")
        
        print(f"Voce escolheu {carros[cod_carro]} por {dias} dias.")
        print(f"O aluguel totalizaria R${dias * carros[cod_carro][1]}. Deseja alugar?")
        
        print("0 - SIM | 1 - NAO")
        conf = int(input())
        
        if conf == 0:
            print(f"Parabens, voce alugou o {carros[cod_carro][0]} por {dias} dias.")
            alugados.append(carros.pop(cod_carro))
                       
        
    
    elif op == 2:
        if len(alugados) == 0:
            print("Nao ha carros para devovler!")
            
        else:
            print("Segue a lista de carros alugados. Qual voce deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print(f"Obrigado por devovler o {carros[cod_carro][0]}.")
                carros.append(carros.pop(cod))
            
    
    
    print("")
    print("==========")
    print("Digite 0 para continuar ou 1 para sair")
    if float(input()) == 1:
        break