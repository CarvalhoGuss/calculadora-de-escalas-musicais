semitom = st = 1
tom = t = 2

unissono = primeira = 0
segundamenor = sme = st
segundamaior = sma = t
tercamenor = tme = 1.5 * t
tercamaior = tma = 2 * t
quartajusta = qaj = 2.5 * t
quartaaumentada = quintadim = qau = qid = 3 * t
quintajusta = qij = 3.5 * t
quintaaumentada = sextamenor = qia = sxme = 4 * t
sextamaior = setimadiminuta = sxma = sed = 4.5 * t
setimamenor = seme = 5 * t
setimamaior = sema = 5.5 * t
oitavajusta = 6 * t


def escala_cromatica():  # Notas sendo exibidas no menu de tons.
    escala = ('[C]', '[C#]', '[D]', '[D#]', '[E]', '[F]', '[F#]', '[G]', '[G#]', '[A]', '[A#]', '[B]')
    return escala


def conjunto_notas_caculaveis():  # Iterável de notas.
    numeronota = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B',
                  'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
    return numeronota


def formula_da_escala(modo):
    if modo == 'Jônio - Maior natural/diatônica':
        formula_geral = 'Fórmula geral: tom, tom, semitom, tom, tom, tom, semitom.'
        estrutura = [t, t, st, t, t, t, st]
    elif modo == 'Dórico':
        formula_geral = 'Fórmula geral: tom, semitom, tom, tom, tom, semitom, tom.'
        estrutura = [t, st, t, t, t, st, t]
    elif modo == 'Frígio':
        formula_geral = 'Fórmula geral: semitom, tom, tom, tom, semitom, tom, tom.'
        estrutura = [st, t, t, t, st, t, t]
    elif modo == 'Lídio':
        formula_geral = 'Fórmula geral: tom, tom, tom, semitom, tom, tom, semitom.'
        estrutura = [t, t, t, st, t, t, st]
    elif modo == 'Mixolídio':
        formula_geral = 'Fórmula geral: tom, tom, semitom, tom, tom, semitom, tom.'
        estrutura = [t, t, st, t, t, st, t]
    elif modo == 'Eólio - Escala Menor Natural':
        formula_geral = 'Fórmula geral: tom, semitom, tom, tom, semitom, tom, tom.'
        estrutura = [t, st, t, t, st, t, t]
    elif modo == 'Lócrio':
        formula_geral = 'Fórmula geral: semitom, tom, tom, semitom, tom, tom, tom.'
        estrutura = [st, t, t, st, t, t, t]
    return formula_geral, estrutura


def formula_da_escala_menor_harmonica(modo):
    if modo == 'Modo Eólio com Sétima Maior (Modo Harmônico Menor)':
        formula_geral = 'Fórmula geral: tom, semitom, tom, tom, semiton, tom+semiton, semitom.'
        estrutura = [t, st, t, t, st, 3*st, st]
    elif modo == 'Modo Lócrio Natural 6 (Modo Lócrio #6)':
        formula_geral = 'Fórmula geral: semitom, tom, tom, semiton, tom+semiton, semitom, tom.'
        estrutura = [st, t, t, st, 3*st, st, t]
    elif modo == 'Modo Jônio #5 (Modo Maior Aumentado)':
        formula_geral = 'Fórmula geral: tom, tom, tom, semiton, tom+semiton, semitom, tom.'
        estrutura = [t, t, t, st, 3*st, st, t]
    elif modo == 'Modo Dórico #4 (Modo Dórico Aumentado)':
        formula_geral = 'Fórmula geral: tom, semitom, tom+semiton, semitom, tom, tom, semitom.'
        estrutura = [t, st, 3*st, st, t, t, st]
    elif modo == 'Modo Frígio Dominante (Modo Frígio Maior)':
        formula_geral = 'Fórmula geral: semitom, tom+semiton, semitom, tom, tom, semitom, tom.'
        estrutura = [st, 3*st, st, t, t, st, t]
    elif modo == 'Modo Lídio #2 (Modo Lídio Aumentado #2)':
        formula_geral = 'Fórmula geral: tom+semiton, semitom, tom, tom, semitom, tom, tom.'
        estrutura = [3*st, st, t, t, st, t, t]
    elif modo == 'Modo Superlócrio (Modo Diminuto)':
        formula_geral = 'Fórmula geral: tom, semitom, tom, tom, semitom, tom, tom+semiton.'
        estrutura = [t, st, t, t, st, t, 3*st]
    return formula_geral, estrutura


def formula_da_escala_menor_melodica(modo):
    if modo == 'Dórico com Sétima Maior':
        formula_geral = 'Fórmula geral: tom, semitom, tom, tom, tom, semitom, semitom.'
        estrutura = [t, st, t, t, t, st, st]
    elif modo == 'Frígio com Sexta':
        formula_geral = 'Fórmula geral: semitom, tom, tom, tom, semitom, semitom, tom.'
        estrutura = [st, t, t, t, st, st, t]
    elif modo == 'Lídio com Quinta Aumentada':
        formula_geral = 'Fórmula geral:  tom, tom, tom, semitom, semitom, tom, semitom'
        estrutura = [t, t, t, st, st, t, st]
    elif modo == 'Mixolídio com Quarta Aumentada ou Lídio b7':
        formula_geral = 'Fórmula geral: tom, tom, semitom, semitom, tom, tom, semitom.'
        estrutura = [t, t, st, st, t, t, st]
    elif modo == 'Mixolídio b13':
        formula_geral = 'Fórmula geral: tom, semitom, semitom, tom, tom, semitom. tom.'
        estrutura = [t, st, st, t, t, st, t]
    elif modo == 'Lócrio com Nona':
        formula_geral = 'Fórmula geral: semiton, semitom, tom, tom, semitom, tom, tom.'
        estrutura = [st, st, t, t, st, t, t]
    elif modo == 'Superlócrio ou Escala Alterada':
        formula_geral = 'Fórmula geral: semitom, tom, tom, semitom, tom, tom, tom.'
        estrutura = [st, t, t, st, t, t, t]
    return formula_geral, estrutura


def calculo_escala(estrutura, numero_nota):
    numero_nota += -1
    escala_final = []
    escala = conjunto_notas_caculaveis()
    escala_final.append(escala[numero_nota])
    for c in range(len(estrutura)):
        numero_nota += estrutura[c]
        escala_final.append(escala[numero_nota])
    return escala_final
