# klikker
import os
import sys
import pprint
import copy


# TODO: Få input


# Forventet output:
# Susanne, Christian, Audun og Adrian
# Jakob, Lise Mette, Elise
# Mange toer-klikker

#Fiks tre og fire- funksjonene
# Jeg er forvirret
'''
konfirmanter = {'Adrian': ['Audun', 'Susanne', 'Christian'],
                'Lise Mette': ['Jakob', 'Elise', 'Christian'],
                'Jakob': ['Lise Mette', 'Elise', 'Mari'],
                'Christian': ['Susanne', 'Adrian', 'Audun'],
                'Audun': ['Susanne', 'Christian', 'Adrian'],
                'Susanne': ['Christian', 'Adrian', 'Audun'],
                'Elise': ['Lise Mette', 'Jakob', 'Mari'],
                'Mari': ['Jakob', 'Lise Mette', 'Jakob']
                }
'''

os.chdir('C:\\Users\\PulseHealing\\Dropbox\\Konfirmant')
konfirmanter = {}
# Import input as Dictionary
with open('Konfirmantønsker.txt') as f:
    for linje in f.read().splitlines():
        # Antatt format: "[Konfirmant], [Ønske1], [Ønske2], [Ønske3]"
        data = linje.split(', ')
        konfirmanter[data[0]] = data[1:]


def kl2():
    klikker = []
    for konf, ønske in konfirmanter.items():
        for ø in ønske:
            if konf in konfirmanter[ø]:
                if sorted([konf, ø]) not in klikker:
                    klikker.append(sorted([konf, ø]))
    return klikker

# TODO: Lag treer-klikker
# Tre personer hvor hver ønsker de to andre
def kl3():
    # OBSOBSOBS
    # Hvis tre-klikken er del av en fire-klikke må det skrives (?)
    klikker = []
    for konf, wishes in konfirmanter.items():
        # Hvis konf ønskes av 1. og 2. ønske
        if konf in konfirmanter[wishes[0]] and konf in konfirmanter[wishes[1]]:
            if wishes[0] in konfirmanter[wishes[1]] and wishes[1] in konfirmanter[wishes[0]]:
                if sorted([konf, wishes[0], wishes[1]]) not in klikker:
                    klikker.append(sorted([konf, wishes[0], wishes[1]]))


        # Hvis konf ønskes av sitt 1. og 3. ønske
        elif konf in konfirmanter[wishes[0]] and konf in konfirmanter[wishes[2]]:
            if wishes[0] in konfirmanter[wishes[2]] and wishes[2] in konfirmanter[wishes[0]]:
                if sorted([konf, wishes[0], wishes[2]]) not in klikker:
                    klikker.append(sorted([konf, wishes[0], wishes[2]]))

        # Hvis konf ønskes av 2. og 3. ønske
        elif konf in konfirmanter[wishes[1]] and konf in konfirmanter[wishes[2]]:
            if wishes[1] in konfirmanter[wishes[2]] and wishes[2] in konfirmanter[wishes[1]]:
                if sorted([konf, wishes[1], wishes[2]]) not in klikker:
                    klikker.append(sorted([konf, wishes[1], wishes[2]]))

        # Ingen tre-klikker funnet, tar neste konfirmant
        else:
            continue

    '''for i in klikker:
        i.sort()
    for i in klikker:
        while klikker.count(i) > 1:
            del klikker[klikker.index(i)]'''
    return klikker



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
            if sorted(konfirmanter[ø]) != pot_kl:
                clique = False
                break
            else:
                pot_kl.append(ø)
                pot_kl.sort()
        if pot_kl not in klikker and clique == True:
            klikker.append(pot_kl)

    return klikker

#FOR SENERE
# with konfirmanter[wishes[0]] as k1 and konfirmanter[wishes[1]] as k2:
#   clique3_func(k1, k2, konf)

#TODO: Dictionary med alle konfene og hvilke klikker de er i

#print(kl3())

klikke2 = kl2()
klikke3 = kl3()
klikke4 = kl4()

klikker = [klikke2, klikke3, klikke4]


for kl2 in klikke2:
    for kl3 in klikke3:
        if set(kl2) <= set(kl3):
            kl2.append('basj')

for kl3 in klikke3:
    for kl4 in klikke4:
        if set(kl3) <= set(kl4):
            kl3.append('basj')

unike_klikker = []

for kl_n in klikker:
    for kl in kl_n:
        if 'basj' not in kl:
            unike_klikker.append(kl)
'''
for kl_n in klikker:
    for kl in kl_n:
        if 'basj' in kl:
            print(klikker[klikker.index(kl_n)][])
            #klikker[klikker.index(kl_n)].remove('basj')
'''
#pprint.pprint(klikker)
#sys.exit()

#TODO: Input
with open('Konfirmant-klikker.txt', 'w') as f:
    f.write('Unike klikker:\n')
    for klikke in unike_klikker:
        f.write(', '.join(klikke))
        f.write('\n')
    f.write('\n' + ('_'*40) + '\n')
    f.write('\n')
    f.write('Alle klikker:\n')
    for klikke_størrelse in klikker:
        for klikke in klikke_størrelse:
            f.write(', '.join(klikke))
            f.write('\n')


# Input:
'''
konfirmanter = {'Adrian': ['Audun', 'Susanne', 'Christian'],
                'Lise Mette': ['Jakob', 'Elise', 'Christian'],
                'Jakob': ['Lise Mette', 'Elise', 'Mari'],
                'Christian': ['Susanne', 'Adrian', 'Audun'],
                'Audun': ['Susanne', 'Christian', 'Adrian'],
                'Susanne': ['Christian', 'Adrian', 'Audun'],
                'Elise': ['Lise Mette', 'Jakob', 'Mari'],
                'Mari': ['Jakob', 'Lise Mette', 'Jakob']
                }'''

# Output:
'''
Unike klikker
[['Jakob', 'Mari'],
 ['Elise', 'Jakob', 'Lise Mette'],
 ['Adrian', 'Audun', 'Christian', 'Susanne']]

U-unike grupper og unike grupper (med basj-tag som viser at klikken er en del av en større klikke)
[[['Adrian', 'Audun', 'basj'],
  ['Adrian', 'Susanne', 'basj'],
  ['Adrian', 'Christian', 'basj'],
  ['Jakob', 'Lise Mette', 'basj'],
  ['Elise', 'Lise Mette', 'basj'],
  ['Christian', 'Susanne', 'basj'],
  ['Audun', 'Christian', 'basj'],
  ['Elise', 'Jakob', 'basj'],
  ['Jakob', 'Mari'],
  ['Audun', 'Susanne', 'basj']],
 [['Adrian', 'Audun', 'Susanne', 'basj'],
  ['Elise', 'Jakob', 'Lise Mette'],
  ['Adrian', 'Christian', 'Susanne', 'basj'],
  ['Audun', 'Christian', 'Susanne', 'basj']],
 [['Adrian', 'Audun', 'Christian', 'Susanne']]]'''
