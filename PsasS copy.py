class Requisito:
    #Inicializador
    def __init__(self, id=None, txt=None, prioridade=None):
        self.tipo = 'Requisito'
        self.id = id
        self.txt = txt
        self.prioridade = prioridade

    def inicializar(self):
        print("Defina id, descrição e prioridade:")
        self.id = int(input())
        self.txt = input()
        self.prioridade = int(input())

    #Função    
    def info(self):
        print("{} {}".format(self.tipo, self.id))
        print("    txt:{}".format(self.txt))
        print("    prioridade:{}".format(self.prioridade))
    
    def subir(self):
        if self.prioridade<9:
            self.prioridade +=1


print("+++++++++++++++++++Test+++++++++++++++++++++")

#Inicializando requisito único
r1 = Requisito()
r1.inicializar()
print(r1.txt)

#Inicializando lista
print("Tamanho da lista:")
num = int(input(str))
requisitos = [Requisito() for i in range(num)]
for r in requisitos:
    r.inicializar()

for r in requisitos:
    print(r.txt)

'''

# Inicialização
num = int(input(str))
requisitos = []
for i in range(num):
    id = input()
    txt = 
    requisitos.append(Requisito(1, "Primeiro req.", 2))

#Acesso e chamada
r1.info()
r1.prioridade = 3
r1.info()
r1.subir()
r1.info()


'''