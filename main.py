import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["aula6DB"]
mycol = mydb["customers"]

listaDataBaseFilter = []



while(True):
    print("Digite [1] para ler o arquivo CSV \nDigite [2] para filtrar \nDigite [3] para baixar os arquivos \nDigite [0] para sair")
    escolha = str(input("Digite o Menu que deseja entrar: "))

    if escolha == '1':
        print("Aguarde!")
        with open('C:/Users/Logatti/PycharmProjects/aula-06-04MongoDB/cadastro_estabelecimentos_cnes.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            csv_reader.__next__()
            for row in csv_reader:
                mydict = {"CNES": row[0], "UF": row[1], "IBGE": row[2], "NOME": row[3], "LOGRADOURO": row[4],
                          "BAIRRO": row[5],
                          "LATITUDE": row[6], "LONGITUDE": row[7]}

                x = mycol.insert_one(mydict)
        print("Arquivo CSV Inserido com sucesso! \n")
    if escolha == '2':
        for c in range(0, 4):
            cnes = str(input("Digite o CNES para o filtro: "))
            for x in mycol.find({"CNES": cnes},
                                {"_id": 1, "CNES": 1, "UF": 1, "IBGE": 1, "NOME": 1, "LOGRADOURO": 1, "BAIRRO": 1,
                                 "LATITUDE": 1, "LONGITUDE": 1}):
                listaDataBaseFilter.append(x)


    if escolha == '3':
        arq = open("C:/Users/Logatti/Desktop/txtpython/ResuFiltro.txt", "w+")
        for dict in listaDataBaseFilter:
            for chave in dict:
                result = f" {chave}: {str(dict[chave])}"
                arq.write(result)
            arq.write("\n\n")
        arq.close()

    if escolha == '0':
        break
