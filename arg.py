
#função apenas para printar
def funcao():
    print("Eis aqui um teste")

#função para colocar o nome antess da palavra padrão 
def funcao2(fname):
    print(fname + "Refsnes")

#função para colocar o nome depois da palavra padrão
def funcao3(lname):
    print("Refsnes" + lname)

#obs o argumento na função é apenas para nomear e especificar (aparentemente)
#conclusão: o argumento pode ter qualquer nome nesses casos
funcao()
funcao2("John")
funcao3("John")

#LISTA COMO ARGUMENTO
def lista(coisas):
    for x in coisas:
        print(x)

coisas = ["carro", "moto", "console"]

lista(coisas)

#Return, vai retornar o resultado aqui
def retorno(x):
    return 3 * x
print(retorno(9))
