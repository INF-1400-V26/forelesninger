# Sudoku - brute force pseudokode

løs_sudoku(delvis_utfylt_sudoku):

    for neste blanke rute:
        finn gyldige verdier
        for hver gyldige verdi:
            fyll inn verdien
            prøv å løse resten (med løs_sudoku)
            hvis løsning funnet,
                returner løsning
    (ingen av verdiene fungerte)
    "visk ut" verdi
    returner "ingen løsning"
        
