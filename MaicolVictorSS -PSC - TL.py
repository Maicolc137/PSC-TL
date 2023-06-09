#A função calcular_imc(peso, altura) recebe o peso e a altura de uma pessoa e calcula o IMC (peso dividido pelo quadrado da altura)
def calcular_imc(peso, altura):
    altura
    imc = peso / (altura ** 2)
    return imc

#dados do arquivo DATASET
dados = [
    ["Felipe", "Neves da Hora", 70.6, 1.69],
    ["Sandro", "Barbosa", 90.5, 1.73],
    ["Maycon", "da Silva Ferreira", 100.01, 1.82],
    ["Jeferson", "Oliveira", 80.04, 1.75],
    ["Manuel", "Gomes Vieira", 63.05, 1.8],
    ["Emanuel", "da Silva", 87.5, 1.61],
    ["Isis", "Santanna de Deus", 59, 1.6],
    ["Maria", "Santana Bezerra", 63.8, 1.75],
    ["Alessandro", "Viana", 69.53, 1.83],
    ["Sandro", "Barbosa", 75, 1.54],
    ["Almir", "Valente", 87.86, 1.8],
    ["Bruno", "Santana Filho", 68.63, 1.65],
    ["Marta", "Santos Oliveira", 63.55, 1.72],
    ["Michele", "Santanna Da Silva", 68, 1.7],
    ["Alex", "Da Silva", 78.08, 1.85],
    ["Daniel", "Alexandre", 54.05, 1.78],
    ["Manuella", "Pereira", 68.36, 1.69],
    ["Matheus", "Silva", 92.3, 2.01],
    ["Giuderlan", "Antonio Neto", 80.25, 1.98],
    ["Geisa", "Ferreira Da Silva", 75.05, 1.65],
    ["Neymar", "Josefino Andrade", 110, 1.77],
    ["João", "Michelango", 160, 1.59],
    ["Gabriela", "Xavier Ferreira", 58, 1.7],
    ["Michelangelo", "de La Siena", 100, 1.9],
    ["Ivanor", "de Jesus", 75.68, 1.7],
    ["Cienne", "Augusta Conceição", 56.05, 1.57],
    ["Arthur", "Santana", 66.06, 1.75],
    ["Amaro", "Luiz", 90.05, 2.68],
    ["Alzenrau", "Silva", 65, 1.97],
    ["Caio", "Sena", 50.01, 1.33],
    ["Romildo", "da Silva", 89.05, 1.73],
    ["Lindomar", "Catillo", 68.22, 1.53],
    ["Felizberto", "Felizmino da Felicidade", 86.5, 1.86],
    ["Caroline", "da boa Mente", 78.05, 1.87],
    ["Bruna", "Giuseppe", 75.1, 1.78],
    ["Carlos", "Magno", 101.9, 1.69],
    ["Adailton", "Ferreira", 55.98, 1.6],
    ["Jandersson", "Almeida Santos", 105.35, 1.99],
    ["Joao", "Joaquim José da Silva", 98.05, 1.89],
    ["Allan", "Santana", 76.12, 1.85],
    ["Danielle", "Santos", 55.09, 1.62],
    ["Valdevino", "Soares", 60.2, 1.68],
    ["Maria", "Silva Pereira", 65.87, 2.56],
    ["Ivanorvilson", "Alberto Lima", 58, 1.53],
    ["Camelia", "Joselina", 96.05, 1.23],
    ["Medinchina", "Casais", 120.05, 1.93],
    ["Alcebíades", "Augustino da Assunção", 86, 1.8],
    ["Masha", "Alcântara", 89, 1.89],
    ["Livia", "Duarte", 54.06, 1.45],
    ["Romerson", "Simpson Silva", 90.11, 1.75],
    ["Mirelle", "da Fonseca Filha", 59.9, 1.62],
    ["Sregio", "Carvalho", 87.05, 2.98],
    ["Filadélfio", "Alfrônio", 98.2, 1.95],
    ["Marcos", "Silva", 70.14, 1.7],
    ["Afreim", "Isotopo", 78.89, 1.51],
    ["Agatha", "Barreto Da Silva", 54, 1.68],
    ["Emmanoel", "Junior", 73, 1.55],
    ["Eliza", "Trindade", 68.07, 1.67],
    ["Aminoã", "Gabriela Ferraz", 68, 1.95],
    ["Melissa", "Fagundes", 65.07, 1.4],
    ["Dean", "Winchester", 85, 1.56],
    ["Liumar", "Santos Oliveira", 67, 1.58],
    ["Adalfreda", "da Silva Ferreira", 65.02, 1.78],
    ["Jean", "Santos", 45.78, 1.6],
    ["Anita", "Oliveira"],
    ["Jeane", "Santana", 35.2, 1.45],
    ["Pablo", "Vittar", 1.78, 75.99],
    ["Weliton", "Viana", 70.2, 1.73],
    ["Quixote", "de la Mancha", 90, 1.9],
    ["Arthur", "Carvalho Jose", 87.06, 1.65],
    ["Eliane", "Santos", 80.2, 1.9],
    ["Ezrael", "Martins", 69.55, 1.89],
    ["Dulcinesia", "del Troboso", 56.9, 1.66],
    ["Leonardo", "Oliveira Castro", 67.05, 1.97],
    ["Aldiran", "Sousa", 78.23, 1.98],
    ["Josefina", "Bezerra Oliveira", 86, 1.75],
    ["Pirlo", "James Silva", 91.11, 1.69],
    ["Caio", "Correira Silva", 78.07, 1.8],
    ["Gilmar", "de Santana", 86.05, 1.67],
    ["Josefa", "Serafina", 60.6, 1.6],
    ["Cameloro", "CRISPIM", 90.3, 2.3],
    ["Policarpo", "Quaresma", 86.5, 1.56],
    ["Baskara", "da Silva Ferrrrrreira", 90, 1.89],
    ["Fiuki", "Filho", 69.55, 1.78],
    ["Fátima", "Bernardes", 60.9, 1.78],
    ["Sergio", "Malandro", 75.03, 1.6],
    ["Theo", "Farias", 86.65, 1.68],
    ["Wallace", "Bonner", 93.2, 1.8],
    ["Yumi", "Bachió", 78.6, 1.75],
    ["Emily", "Souza Ribeiro", 65.07, 1.65],
    ["Whind", "Piauí", 69.2, 1.7],
    ["Alane", "Silva", 29.3, 1.3],
    ["Luana", "Lima Ferreira", 78.06, 1.48],
    ["Inoswaldo", "Kamacho", 140.4, 1.56],
    ["Luna", "Lunara Lua", 70, 1.86],
    ["Hulk", "Jose", 35.5, 1.2],
    ["Maria", "Gomes", 58.05, 1.56],
    ["Paulo", "Rocha", 98.07, 2],
    ["Luane", "Santana Teixeira", 50.78, 1.5]
]
#percorre cada "pessoa" na lista de dados.
for pessoa in dados:
    
    #concatena o primeiro nome e o sobrenome da pessoa, convertendo-os para letras maiúsculas, e armazena o resultado na variável nome.
    nome = pessoa[0].upper() + " " + pessoa[1].upper()

    #teste 1 para verificação de dados
    if len(pessoa) >= 4:
        peso = pessoa[2]
        altura = pessoa[3]
        #teste2
        if altura > 2.5:
            print(f"{nome} tem altura inválida: {altura}")
        else:
            #chama a função calcular_imc para calcular o IMC da pessoa com base no peso e na altura, e armazena o resultado na variável imc.
            imc = calcular_imc(peso, altura)

            #exibe o nome da pessoa e o valor do IMC formatado com duas casas decimais.
            print(f"{nome} {imc:.2f}")
    else:
        print(f"Valores de peso ou altura ausentes para {nome}")