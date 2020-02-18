class Requisito:
    #Inicializador
    def __init__(self, id, prioridade):
        self.tipo = 'Requisito'
        self.id = id
        self.prioridade = prioridade
    #Função    
    def info(self):
        print("{} {}".format(self.tipo, self.id))
        print("   prioridade:{}".format(self.prioridade))

# Inicialização
r1 = Requisito("01", 0)
r2 = Requisito("02", 9)

#Acesso
print("r1 p = {}".format(r1.prioridade))
if r1.prioridade < r2.prioridade:
    print("r1.prioridade < r2.prioridade")

#Chamada de função
r1.info()


print("+++++++++++++++++++Test+++++++++++++++++++++")


