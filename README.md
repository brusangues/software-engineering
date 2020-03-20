# software-engineering

Universidade Federal do ABC
Disciplina: Engenharia de Software - Processo de Software as a Software
Professor: João Marcelo Borovina Josko
Aluno: Bruno Sanches Rodrigues

![Diagrama UML para entendimento do código](https://raw.githubusercontent.com/brusangues/software-engineering/master/PSasS%20UML.png)

### Link para visualização do código na plataforma Repl.it:
### https://repl.it/@BrunoSanches/ES-PSasS-Bruno-Sanches-Rodrigues

### Link para executar o código online:
### https://ES-PSasS-Bruno-Sanches-Rodrigues.brunosanches.repl.run

## Abaixo, um exemplo de execução:
```
UFABC Disciplina: Engenharia de Software - PSasS
Professor: João Marcelo Borovina Josko
Aluno: Bruno Sanches Rodrigues RA: 11201721076
++++++++++++++++++++++++++++++
Para utilizar, digite as quantidades inteiras ou responda com uma das letras 's' o
u 'n'
++++++++INICIALIZAÇÃO+++++++++
Digite o tempo disponível
>>10
Digite o dinheiro disponível
>>10
++++++++++REQUISITOS++++++++++
Digite o número de requisitos
>>4
Digite a descrição para Requisito 1
>>Primeiro requisito funcional
Digite o tempo necessário para Requisito 1
>>2
Digite o custo necessário para Requisito 1
>>3
Digite a descrição para Requisito 2
>>Segundo req
Digite o tempo necessário para Requisito 2
>>3
Digite o custo necessário para Requisito 2
>>4
Digite a descrição para Requisito 3
>>Terceiro req
Digite o tempo necessário para Requisito 3
>>1
Digite o custo necessário para Requisito 3
>>2
Digite a descrição para Requisito 4
>>Quarto req
Digite o tempo necessário para Requisito 4
>>10
Digite o custo necessário para Requisito 4
>>5
+++++++++++PROJETO++++++++++++
Deseja criar um Projeto com todos os requisitos?(s/n)
>>n
Selecione os requisitos que deseja incluir
    Deseja incluir Requisito 1?(s/n)
>>s
    Deseja incluir Requisito 2?(s/n)
>>s
    Deseja incluir Requisito 3?(s/n)
>>s
    Deseja incluir Requisito 4?(s/n)
>>n
Digite a descrição para Projeto 0
>>Primeiro projeto
Projeto 0
    descrição:Primeiro projeto
    tempo necessário:6
    custo:9
    eligibilidade:False
Testando tempo e custo do Projeto 0:
    tempo: disponível 10, necessário 6
    dinheiro: disponível 10, necessário 9
    tempo: Ok
    custo: Ok
Deseja adicionar requisitos ao Projeto 0?(s/n)
>>s
Digite o número de requisitos
>>2
Digite a descrição para Requisito 4
>>Quarto req
Digite o tempo necessário para Requisito 4
>>3
Digite o custo necessário para Requisito 4
>>1
Digite a descrição para Requisito 5
>>Quinto req
Digite o tempo necessário para Requisito 5
>>1
Digite o custo necessário para Requisito 5
>>2
Testando tempo e custo do Projeto 0:
    tempo: disponível 10, necessário 10
    dinheiro: disponível 10, necessário 12
    tempo: Ok
    custo: Falhou
Deseja remover requisitos do Projeto 0?(s/n)
>>s
    Deseja remover Requisito 1?(s/n)
>>s
    Deseja remover Requisito 2?(s/n)
>>n
    Deseja remover Requisito 3?(s/n)
>>n
    Deseja remover Requisito 4?(s/n)
>>n
    Deseja remover Requisito 5?(s/n)
>>n
Testando tempo e custo do Projeto 0:
    tempo: disponível 10, necessário 8
    dinheiro: disponível 10, necessário 9
    tempo: Ok
    custo: Ok
Projeto 0
    descrição:Primeiro projeto
    tempo necessário:8
    custo:9
    eligibilidade:True
++++++++++++CÓDIGO++++++++++++
Deseja implementar Projeto 0 como um código?(s/n)
>>s
Digite a descrição para Codigo 0
>>Primeiro código
Codigo 0
    descrição:Primeiro código
    passou testes:False
++++++++++++TESTES++++++++++++
Deseja testar Codigo 0?(s/n)
>>s
Testando Codigo 0
    teste 1: esperado 2, obtido 2
    teste 1: Ok
    teste 2: esperado 3, obtido 3
    teste 2: Ok
    teste 3: esperado 4, obtido 4
    teste 3: Ok
    teste 4: esperado 5, obtido 5
    teste 4: Ok
Codigo 0
    descrição:Primeiro código
    passou testes:True
+++++++++++PRODUTO++++++++++++
Deseja implementar Codigo 0 como um produto?(s/n)
>>s
Digite a descrição para Produto 0
>>Primeiro produto
Produto 0
    descrição:Primeiro produto
Está satisfeito com o Produto 0?(s/n)
>>s
++++++++++++++FIM+++++++++++++
```