# klikker
import pprint
import copy

# Forventet output:
# Susanne, Christian, Audun og Adrian
# Jakob, Lise Mette, Elise
# Mange toer-klikker

#Fiks tre og fire- funksjonene
# Jeg er forvirret

konfirmanter = {'Adrian': ['Audun', 'Susanne', 'Christian'],
                'Lise Mette': ['Jakob', 'Elise', 'Christian'],
                'Jakob': ['Lise Mette', 'Elise', 'Mari'],
                'Christian': ['Susanne', 'Adrian', 'Audun'],
                'Audun': ['Susanne', 'Christian', 'Adrian'],
                'Susanne': ['Christian', 'Adrian', 'Audun'],
                'Elise': ['Lise Mette', 'Jakob', 'Mari'],
                'Mari': ['Jakob', 'Lise Mette', 'Jakob']
                }

def kl2():
    klikker = []
    for konf, ønske in konfirmanter.items():
        for ø in ønske:
            if konf in konfirmanter[ø]:
                if sorted([konf, ø]) not in klikker:
                    klikker.append(sorted([konf, ø]))
    return klikker
'''
# TODO: Lag treer-klikker
# Tre personer hvor hver ønsker de to andre
def kl3():
    klikker3 = []
    for konf, ønsker in konfirmanter.items():
        for p in [[ønsker[0], ønsker[1]],
                  [ønsker[0], ønsker[1]],
                  [ønsker[1], ønsker[2]]
                  ]:
                  #kluss
                  for ø in p:
                        kopi = copy.deepcopy(p)
                        kopi.remove(p.index(ø))
                        if not (konf og p[0]) in konfirmant[p]:
                            break
                        else:
                            if not sorted([konf, p ,ø]) in klikker3:
                                klikker3.append(sorted[konf, p, ø])
    return klikker3

'''


# For firer-klikke
def kl4():
    klikker = []
    for konf, ønsker in konfirmanter.items():
        clique = True
        kopi = copy.deepcopy(ønsker)
        pot_kl = kopi + [konf]
        for ø in ønsker:
            assert ø in pot_kl, 'not ø in pot_kl'
            pot_kl.remove(ø)
            if sorted(konfirmant[ø]) != pot_kl:
                clique = False
                break
            else:
                pot_kl.append(ø)
                pot_kl.sort()
        if pot_kl not in klikker and clique == True:
            klikker.append(pot_kl)
            print('new clique')

    return klikker


'''
def klN():
    kl2 , kl3, kl4 = [], [], []
    for konf, ønsker in konfirmanter.items():
        for flere_ønsker in konfirmanter[ønsker]:'''

#print(kl2())
print(kl4())
