figuras_negras = {
    't1' : "torre negro",
    'c1' : "caballo negro",
    'a1' : "alfil negro",
    'k1' : "rey negro",
    'q1' : "reina negro",
    }

peones_negros = {
    'p1' : "peón negro",
    }

figuras_blancas = {
    't2' : "torre blanca",
    'c2' : "caballo blanca",
    'a2' : "alfil blanca",
    'k2' : "rey blanca",
    'q2' : "reina blanca",
    'p2' : "peón blanco",
    }

peones_blancos = {
    'p2' : "peón blanco",
    }

def desplegar_tablero():
    for i in tablero:
        print(i)

fichas_negras = list(figuras_negras)
fichas_blancas = list(figuras_blancas)
peon_negro = list(peones_negros)
peon_blanco = list(peones_blancos)
tablero = [[], [], [], [], [], [], [], []]
tablero[0] = tablero[0] + fichas_negras
tablero[7] = tablero[7] + fichas_blancas
for i in range(8):
    tablero[1] += peon_negro
    tablero[6] += peon_blanco

desplegar_tablero()