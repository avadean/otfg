

class Element:
    def __init__(self, symbol, Z):
        self.symbol = symbol[0].upper() + symbol[1:].lower()
        self.Z = Z

    def __eq__(self, other):
        return True if self.symbol == other.symbol else False


elements = ['H' ,                                                                                                 'He',
            'Li', 'Be',                                                             'B' , 'C' , 'N' , 'O' , 'F' , 'Ne',
            'Na', 'Mg',                                                             'Al', 'Si', 'P' , 'S' , 'Cl', 'Ar',
            'K' , 'Ca', 'Sc', 'Ti', 'V' , 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y' , 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I' , 'Xe',
            'Cs', 'Ba',
            'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
            'Hf', 'Ta', 'W' , 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
            'Fr', 'Ra',
            'Ac', 'Th', 'Pa', 'U' , 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
            'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og' ]

periodicTable = { symbol : Element(symbol, Z) for Z, symbol in enumerate(elements, 1)}


# Definitions of pseudopotentials.
ps_def = { "C19" : { "H"  : "1|0.6|13|15|17|10(qc=8)",
                     "He" : "1|1.0|12|14|16|10(qc=7)",
                     "Li" : "1|1.0|14|16|18|10U:20(qc=7)",
                     "Be" : "2|1.0|14|16|18|10U:20:21(qc=7)",
                     "B"  : "2|1.2|12|14|16|20:21(qc=8)",
                     "C"  : "2|1.4|10|12|13|20:21(qc=7)",
                     "N"  : "2|1.1|14|16|18|20:21(qc=7)",
                     "O"  : "2|1.1|17|20|23|20:21(qc=8)",
                     "F"  : "2|1.2|14|16|18|20:21(qc=7)",
                     "Ne" : "2|1.4|10|12|13|20:21(qc=6)",
                     "Na" : "2|1.3|14|16|18|20U:30:21(qc=7)",
                     "Mg" : "3|1.8|7|8|9|20U:30:21:32",
                     "Al" : "3|2.2|2.2|1.4|4|5|5|30:31:32U2U2",
                     "Si" : "3|1.8|5|6|7|30:31:32",

                     "Fe" : "3|2.4|2.4|1.0|8|9|10|40:41:32U2U2(qc=5.5)",

                     "Mt" : "1|2.5|7|8|9|70:62:53"
                     }
           }

# Groundstate occupations.
gs_occ = { 0   : [10,20,21,30,31,32,40,41,42,43,50,51,52,53,54,60,61,62,70,71],     # nl quantum numbers
           1   : [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # H
           2   : [ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # He
           3   : [ 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Li
           4   : [ 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Be
           5   : [ 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # B
           6   : [ 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # C
           7   : [ 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # N
           8   : [ 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # O
           9   : [ 2, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # F
           10  : [ 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Ne
           11  : [ 2, 2, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Na
           12  : [ 2, 2, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Mg
           13  : [ 2, 2, 6, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Al
           14  : [ 2, 2, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Si

           26  : [ 2, 2, 6, 2, 6, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Fe

           109 : [ 2, 2, 6, 2, 6,10, 2, 6,10,14, 2, 6,10,14, 0, 2, 6, 7, 2, 0]      # Mt
          }

gs_config = { 1   : '1s1',                                                                              # H
              2   : '1s2',                                                                              # He
              3   : '1s2 2s1',                                                                          # Li
              4   : '1s2 2s2',                                                                          # Be
              5   : '1s2 2s2 2p1',                                                                      # B
              6   : '1s2 2s2 2p2',                                                                      # C
              7   : '1s2 2s2 2p3',                                                                      # N
              8   : '1s2 2s2 2p4',                                                                      # O
              9   : '1s2 2s2 2p5',                                                                      # F
              10  : '1s2 2s2 2p6',                                                                      # Ne
              11  : '1s2 2s2 2p6 3s1',                                                                  # Na
              12  : '1s2 2s2 2p6 3s2',                                                                  # Mg
              13  : '1s2 2s2 2p6 3s2 3p1',                                                              # Al
              14  : '1s2 2s2 2p6 3s2 3p2',                                                              # Si

              26  : '1s2 2s2 2p6 3s2 3p6 3d6 4s2',                                                      # Fe

              109 : '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d7 7s2'      # Mt
             }