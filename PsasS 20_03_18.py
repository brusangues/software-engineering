class Requisito:
    def __init__(self, id=id):
        self.id = id
        self.name = type(self).__name__
        print("Digite a descrição para {} {}".format(self.name, self.id))
        self.description = input()
        self.time = 0
        self.cost = 0
    
    def updateTime(self):
        print("Digite o tempo necessário para {} {}".format(self.name, self.id))
        self.time = int(input())
    
    def updateCost(self):
        print("Digite o custo necessário para {} {}".format(self.name, self.id))
        self.cost = int(input())

    def info(self):
        print("{} {}".format(self.name, self.id))
        print("    descrição:{}".format(self.description))
        print("    tempo necessário:{}".format(self.time))
        print("    custo:{}".format(self.cost))

class Projeto(Requisito):
    def __init__(self, id=id, reqs=list()):
        Requisito.__init__(self, id)
        self.reqs = reqs
        self.time = sum([r.time for r in self.reqs])
        self.cost = sum([r.cost for r in self.reqs])
        self.eligible = False

    def checkEligibility(self):
        print("Testando tempo e custo do {} {}:".format(self.name, self.id))
        if self.time<=Time:
            print("    tempo: Ok")
        else:
            print("    tempo: Falhou")
        if self.cost<=Cost:
            print("    custo: Ok")
        else:
            print("    custo: Falhou")
        if self.time<=Time and self.cost <= Cost:
            self.eligible = True
        else:
            self.eligible = False


    def addReq(self, reqsList):
        self.reqs.extend(reqsList)
        self.time = sum([r.time for r in self.reqs])
        self.cost = sum([r.cost for r in self.reqs])
        self.checkEligibility()

    def removeReq(self, reqsList):
        self.reqs = [r for r in self.reqs if r not in reqsList]
        self.time = sum([r.time for r in self.reqs])
        self.cost = sum([r.cost for r in self.reqs])
        self.checkEligibility()

    def info(self):
        print("{} {}".format(self.name, self.id))
        print("    descrição:{}".format(self.description))
        print("    tempo necessário:{}".format(self.time))
        print("    custo:{}".format(self.cost))
        print("    eligibilidade:{}".format(self.eligible))

class CasoTeste:
    def __init__(self, id=id, expectedResult=int):
        self.id = id
        self.name = type(self).__name__
        self.expectedResult = expectedResult
        self.testResult = False

class Codigo:
    def __init__(self, id=id, project=None, testCases=list()):
        self.id = id
        self.name = type(self).__name__
        print("Digite a descrição para {} {}".format(self.name, self.id))
        self.description = input()
        self.project = project
        self.testCases = testCases
        self.passedTests = False
    
    def checkPassedTests(self):
        a = sum([t.testResult for t in self.testCases])
        b = len(self.testCases)
        if a==b: 
            self.passedTests = True
        else:
            self.passedTests = False

    def testAll(self):
        print("Testando {} {}".format(self.name, self.id))
        i = 1
        for r,t in zip(self.project.reqs, self.testCases):
            codeResult = r.id
            print("    teste {}: esperado {}, obtido {}".format(i, t.expectedResult, codeResult))
            if t.expectedResult == codeResult:
                t.testResult = True
                print("    teste {}: Ok".format(i))
            else:
                t.testResult = False
                print("    teste {}: Falhou".format(i))
            i+=1
        self.checkPassedTests()

    def info(self):
        print("{} {}".format(self.name, self.id))
        print("    descrição:{}".format(self.description))
        print("    passou testes:{}".format(bool(self.passedTests)))

class Produto:
    def __init__(self, id=id, code=None):
        self.id = id
        self.name = type(self).__name__
        print("Digite a descrição para {} {}".format(self.name, self.id))
        self.description = input()
        self.code = code
    
    def info(self):
        print("{} {}".format(self.name, self.id))
        print("    descrição:{}".format(self.description))

Time = 0
Cost = 0
def initialization():
    global Time
    global Cost
    print("Digite o tempo disponível")
    Time = int(input())
    print("Digite o dinheiro disponível")
    Cost = int(input())

def createReqs(reqsList, startId):
    print("Digite o número de requisitos")
    n = int(input())
    for i in range(startId,n+startId):
        r = Requisito(i)
        r.updateTime()
        r.updateCost()
        reqsList.append(r)

def createProject(reqsList):
    print("Deseja criar um Projeto com todos os requisitos?(s/n)")
    a = input()
    if a=='s':
        return Projeto(0,reqsList)
    else:
        print("Selecione os requisitos que deseja incluir")
        newReqsList = []
        for r in reqsList:
            print("    Deseja incluir {} {}?(s/n)".format(r.name, r.id))
            if input()=='s': newReqsList.append(r)
        return Projeto(0,newReqsList)

def updateProject(project):
    while(True):
        print("Deseja adicionar requisitos ao {} {}?(s/n)".format(project.name, project.id))
        if input()=='s':
            n = len(project.reqs) + 1
            lista_requisitos = []
            createReqs(lista_requisitos, n)
            project.addReq(lista_requisitos)
        else: break
        if not project.eligible: break
    
    while(True):
        print("Deseja remover requisitos do {} {}?(s/n)".format(project.name, project.id))
        if input()=='s':
            lista_requisitos = []
            for r in project.reqs:
                print("    Deseja remover {} {}?(s/n)".format(r.name, r.id))
                if input()=='s': lista_requisitos.append(r)
            project.removeReq(lista_requisitos)
        else: break
        if project.eligible: break

def createCode(project):
    print("Deseja implementar {} {}?(s/n)".format(project.name, project.id))
    if input()=='s':
        if project.eligible:
            testCases = []
            for r in project.reqs:
                testCases.append(CasoTeste(r.id, r.id))

            return Codigo(project.id, project, testCases)
        else:
            print("Projeto selecionado não satisfaz as restrições de tempo ou custo")

def createProduct(code):
    print("Deseja implementar {} {}?(s/n)".format(code.name, code.id))
    if input()=='s':
        if code.passedTests:
            return Produto(code.id, code)
        else:
            print("Código selecionado não passou em todos os casos de teste")

print("UFABC Disciplina: Engenharia de Software - PSasS Professor: João Marcelo Borovina Josko")
print("Aluno: Bruno Sanches Rodrigues RA: 11201721076")
print("Todas as quantidades abstratas solicitadas são números inteiros")

print("++++++++INICIALIZAÇÃO+++++++++")
initialization()

print("++++++++++REQUISITOS++++++++++")
lista_requisitos = []
createReqs(lista_requisitos, 1)

print("+++++++++++PROJETO++++++++++++")
projeto0 = createProject(lista_requisitos)
projeto0.info()
projeto0.checkEligibility()
updateProject(projeto0)
projeto0.info()

print("++++++++++++CÓDIGO++++++++++++")
codigo0 = createCode(projeto0)
codigo0.info()

print("++++++++++++TESTES++++++++++++")
codigo0.testAll()
codigo0.info()

print("+++++++++++PRODUTO++++++++++++")
produto0 = createProduct(codigo0)
produto0.info()