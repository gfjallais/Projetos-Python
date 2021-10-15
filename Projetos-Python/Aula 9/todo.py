from itertools import *

dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

periodos = ["D", "N"]

def buildTurns(profs):
    """Esta funcao recebe uma lista profs de profissionais, e constroi uma
    lista de tuplas. Cada tupla possui quatro elementos:
    - Um dia da semana;
    - Um periodo de trabalho (dia ou noite);
    - Um nome de profissional
    - Um indice indicando qual eh aquele turno. O primeiro turno (Seg/D) possui
    indice 1. O segundo turno (Seg/N) possui indice 2, o terceiro turno (Ter/D)
    possui indice 3, e assim por diante.
    """
    turns = product(dias, periodos)
    tXprof = zip(turns, cycle(profs), count(1))
    return ([a, b, c, d] for (a, b), c, d in tXprof)

def printCSV(profs):
    """Esta funcao recebe uma lista de profissionais, e imprime uma tabela
    CSV com os turnos, usando as colunas: indice, dia, periodo e profissional:
    """
    if not profs:
        return None
    else:
        print("indice, dia, periodo, profissional")
        # TODO: imprima o resto do arquivo CSV aqui. Esta rotina devera retornar
        # a string 'fim'. Assim, nao altere o comando de retorno. Insira, logo
        # apos esse comentario, codigo para construir a lista de turnos, e
        # imprimir a tabela CSV.
        turnos = ([d, a, b, c] for [a, b, c, d] in buildTurns(profs))
        for turno in turnos:
            print(turno)
        return 'fim'

def firstDay(profs, prof):
    """Esta funcao imprime o primeiro dia em que trabalha o profissional 'prof'.
    Caso 'prof' nao esteja presente na lista profs, ou nao exista em um turno
    valido, a funcao precisa retornar a string 'Inexistente'
    """
    agenda = buildTurns(profs)
    for turno in agenda:
        if prof in turno:
            return turno[0] 
    return "Inexistente"

def countTurns(profs, prof):
    """Esta funcao retorna o numero de turnos em que trabalha o profissional
    'prof'. Caso 'prof' nao trabalhe em algum turno, entao a funcao retorna
    zero.
    """
    count = 0
    agenda = buildTurns(profs)
    for turno in agenda:
        if turno[2] == prof:
            count += 1
    if count == 0:
        return 0
    else:
        return count

def payTurns(profs, prof):
    """Esta funcao retorna o salario semanal de um profissional, assumindo que
    cada turno diurno lhe paga 1000 e cada turno noturno lhe paga 1333.
    Caso 'prof' nao trabalhe em algum turno, a funcao deve retornar zero.
    """
    salario = 0
    agenda = buildTurns(profs)
    for turno in agenda:
        if prof in turno:
            if turno[1] == 'D':
                salario += 1000
            elif turno[1] == 'N':
                salario += 1333
    if salario == 0:
        return 0
    else:
        return salario