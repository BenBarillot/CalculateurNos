import os

print('pve dander/pve 6.2/pvp_escri/pvp_archer')
reference = input()

#ATTAQUE TOTALE = attaque du perso + attaque de la SP + attaque du masque + attaque du tarot + armes + attaque du skill + attaque du buff + attaque de rune + attaque de charge + up de l'attaque final + 15
#ATTAQUE FINALE = ATTAQUE TOTALE x [1+ ([b]S[/b] % pour les dégâts) + (% pour les dégâts sur un type de monstre/en pvp)] x (1+% d'augmentation de dégâts à 15% de chance en pvp) x [1+ (% d'augmentation de dégâts de l'arme principale) + (% d'augmentation de dégâts de l'arme secondaire)]

print('attaque du perso min')
perso_min = input()
perso_min = int(perso_min)

print('attaque du perso max ')
perso_max = input()
perso_max = int(perso_max)

print("degats crit de l'arme")
crit_arme = input()
crit_arme = int(crit_arme)

print('attaque du masque')
attaque_masque = input()
attaque_masque = int(attaque_masque)

print('attaque tarot')
attaque_tarot = input()
attaque_tarot = int(attaque_tarot)

print('Up de votre arme +1 +2 ect')
up_arme = input()
up_arme = int(up_arme)

print("Up de l'armure adversaire")
up_armure = input()
up_armure = int(up_armure)

up_final_arme = up_arme - up_armure
up_final_arme = int(up_final_arme)

print('arme_min')
attaque_min = input()
attaque_min = int(attaque_min)

print('arme_max')
attaque_max = input()
attaque_max = int(attaque_max)

if up_final_arme == 0 
    attaque_min = int(attaque_min)
    attaque_max = int(attaque_max)

if up_final_arme == 1
    attaque_min = attaque_min*10/100 + attaque_min
    attaque_max = attaque_max*10/100 + attaque_max
    
if up_final_arme == 2
    attaque_min = attaque_min*15/100 + attaque_min
    attaque_max = attaque_max*15/100 + attaque_max

if up_final_arme == 3
    attaque_min = attaque_min*22/100 + attaque_min
    attaque_max = attaque_max*22/100 + attaque_max

if up_final_arme == 4
    attaque_min = attaque_min*32/100 + attaque_min
    attaque_max = attaque_max*32/100 + attaque_max

if up_final_arme == 5
    attaque_min = attaque_min*43/100 + attaque_min
    attaque_max = attaque_max*43/100 + attaque_max

if up_final_arme == 6
    attaque_min = attaque_min*54/100 + attaque_min
    attaque_max = attaque_max*54/100 + attaque_max

if up_final_arme == 7
    attaque_min = attaque_min*65/100 + attaque_min
    attaque_max = attaque_max*65/100 + attaque_max

if up_final_arme == 8
    attaque_min = attaque_min*90/100 + attaque_min
    attaque_max = attaque_max*90/100 + attaque_max

if up_final_arme == 9
    attaque_min = attaque_min*120/100 + attaque_min
    attaque_max = attaque_max*120/100 + attaque_max

if up_final_arme == 10
    attaque_min = attaque_min*200/100 + attaque_min
    attaque_max = attaque_max*200/100 + attaque_max

print('point sp atk')
point_sp_atk = input()
point_sp_atk = int(point_sp_atk)

print('Amélio sp atk')
amélio_sp_atk = input()
amélio_sp_atk = int(amélio_sp_atk)

print('point element sp')
point_sp_element = input()
point_sp_element = int(point_sp_element)

print('Amélio element sp')
amélio_sp_element = input()
amélio_sp_element = int(amélio_sp_element)

element_sp = int(point_sp_element + amélio_sp_element)




if point_sp_atk >= 100:
    attaque_sp = point_sp_atk*10 + 120
    attaque_sp = int(attaque_sp) + amélio_sp_atk*10
    crit_arme = crit_arme + 50
    crit_arme = int(crit_arme)
    
print(crit_arme)
print(attaque_sp)

print('attaque skill')
attaque_skill = input()
attaque_skill = int(attaque_skill)

print('attaque buff')
attaque_buff = input()
attaque_buff = int(attaque_buff)

print('attaque de la rune')
attaque_rune = input()
attaque_rune = int(attaque_rune)

print('pourcentage degat monstre/pvp')
pourcentage_mob_pvp = input()
pourcentage_mob_pvp = int(pourcentage_mob_pvp)

ATTAQUE_TOTALE_MIN = perso_max + attaque_min + attaque_sp + attaque_skill + attaque_buff + attaque_rune + 15 + attaque_masque + attaque_tarot
ATTAQUE_TOTALE_MAX = perso_min + attaque_max + attaque_sp + attaque_skill + attaque_buff + attaque_rune + 15 + attaque_masque + attaque_tarot

print('S_degat')
S_degat = input()
S_degat = int(S_degat)

print('Augmentation de degats')
augmentation = input()
augmentation = int(augmentation)



ATTAQUE_FINAL_MIN = ATTAQUE_TOTALE_MIN*((1+S_degat/100)+(pourcentage_mob_pvp)/100)
ATTAQUE_FINAL_MAX = ATTAQUE_TOTALE_MAX*((1+S_degat/100)+(pourcentage_mob_pvp)/100)



#DÉFENSE TOTALE = défense du perso + défense de la SP + défense du masque + défense du tarot + défense du chapeau + défense des résistances + défense des bijoux + défense de l'équipement + options C/B/A de rune augmentant la défense + up défense final + bonus de défense des monstres 

print('défense du perso ennemie')
perso_def_base = input()
perso_def_base = int(perso_def_base)

print('defense de la sp')
def_sp = input()
def_sp = int(def_sp)

print('defense du masque')
def_masque = input()
def_masque = int(def_masque)

print('defense du tarot')
def_tarot = input()
def_tarot = int(def_tarot)

print('defense du chapeau')
def_chapeau = input()
def_chapeau = int(def_chapeau)

print('defense des resistances')
def_res = input()
def_res = int(def_res)

print('defense des bijoux')
def_bij = input()
def_bij = int(def_bij)

print('defense equipement ')
def_equip = input()
def_equip = int(def_equip)

print('def rune')
def_rune = input()
def_rune = int(def_rune)

print('degats_crit_reduction bijou+buff+armure')
degats_crit_reduction = input()
degats_crit_reduction = int(degats_crit_reduction)



DEF_TOTALE = perso_def_base + def_sp + def_masque + def_tarot + def_chapeau + def_res + def_bij + def_equip + def_rune

#Bonus défense = ( 1 + % potion défense + % costume Nosmall + % S pour toutes les défenses + % pour la défense en PVP + % cochon chançard ? + % Huile de fleur de glace ? )

print('costume nosmall %')
cost_nos = input()
cost_nos = int(cost_nos)

print('S def')
S_def = input()
S_def = int()

print('def pvp %')
def_pvp = input()
def_pvp = int(def_pvp)

BONUS_DEF = (1 + cost_nos/100 + S_def/100 + def_pvp/100)

#DÉFENSE FINALE = DÉFENSE TOTALE x Bonus défense x Malus défense

DEFENSE_FINALE = DEF_TOTALE * BONUS_DEF 

#DÉGÂTS PHYSIQUES= (ATTAQUE FINALE - DÉFENSE FINALE) x (1 + Taille de critique)

DEGATS_PHYSIQUES_MIN = (ATTAQUE_FINAL_MIN - DEFENSE_FINALE)
DEGATS_PHYSIQUES_MAX = (ATTAQUE_FINAL_MAX - DEFENSE_FINALE)



 



#Élément du personnage = élément de l'arme principale + élément de l'arme secondaire + élément du masque + élément des résistances + élément des bijoux + élément de rune + élément du skill + élément de buff
print('element arme principale')
element_arme_principale = input()
element_arme_principale = int(element_arme_principale)

print('element arme secondaire')
element_arme_secondaire = input()
element_arme_secondaire = int(element_arme_secondaire)

print('element de la rune')
element_rune = input()
element_rune = int(element_rune)

print('element du skill')
element_skill = input()
element_skill = int(element_skill)

ELEMENT_PERSONNAGE = element_arme_principale + element_arme_secondaire + element_rune + element_skill +element_sp

#Élément de la fée = (Attaque finale + 100) x % de la fée
print('pourcentage de la fée')
fee = input()
fee = int(fee)

element_fee_min = (ATTAQUE_FINAL_MIN + 100)*fee/100
element_fee_max = (ATTAQUE_FINAL_MAX + 100)*fee/100
#Résistance adversaire = Résistance de la fiche perso de l'adversaire + résistance de rune de son armure + buff de résistance - débuff de résistance - baisse de résistance de nos équipements - baisse de résistance de rune de notre arme utilisée

print("res de l'adversaire")
res_adv = input()
res_adv = int(res_adv)

print("res rune")
res_rune = input()
res_rune = int(res_rune)

print('baisse res de notre stuff')
baisse_res = input()
baisse_res = int(baisse_res)

RES_ADV = res_adv + res_rune - baisse_res

print('Bonus elementaire')
bonus_elementaire = input()
bonus_elementaire = int(bonus_elementaire)

#ÉLÉMENT FINAL = [Élément du perso+ (Attaque finale + 100) x % de la fée ] x (1 + % Bonus élémentaire) x (100% - % résistance finale de l'adversaire)



DEGAT_ELEMENTS_MIN = (ELEMENT_PERSONNAGE+ (ATTAQUE_FINAL_MIN+ 100)*fee/100)*(1 + bonus_elementaire/100)*(1 - RES_ADV/100) #bonus_elementaire% a changé bonus elem
DEGAT_ELEMENTS_MAX = (ELEMENT_PERSONNAGE+ (ATTAQUE_FINAL_MAX+ 100)*fee/100)*(1 + bonus_elementaire/100)*(1 - RES_ADV/100)

#Dégâts = dégâts physiques + dégâts d'élément + dégâts de moral
ELEMENT_AUGMENTATION_MIN = (((ELEMENT_PERSONNAGE + element_fee_min)*(1 + (bonus_elementaire/100)))*(augmentation/100))*((1 - ((res_adv - baisse_res)/100)))
ELEMENT_AUGMENTATION_MAX = (((ELEMENT_PERSONNAGE + element_fee_max)*(1 + (bonus_elementaire/100)))*(augmentation/100))*((1 - ((res_adv - baisse_res)/100)))

DEGATS_MIN = DEGATS_PHYSIQUES_MIN + DEGAT_ELEMENTS_MIN
DEGATS_MAX = DEGATS_PHYSIQUES_MAX + DEGAT_ELEMENTS_MAX
DEGATS_AUGMENTE_MIN = DEGATS_MIN*(1 + augmentation/100) 
DEGATS_AUGMENTE_MAX = DEGATS_MAX*(1 + augmentation/100)
DEGATS_CRIT_MIN = (DEGATS_PHYSIQUES_MIN*(1 + ((crit_arme - degats_crit_reduction)/100)) + DEGATS_PHYSIQUES_MIN)
DEGATS_CRIT_MAX = (DEGATS_PHYSIQUES_MAX*(1 + (crit_arme/100)) + DEGATS_PHYSIQUES_MAX)
CRIT_AUGMENTE_MIN = (((DEGATS_CRIT_MIN) + (((DEGATS_MIN*augmentation/100 - DEFENSE_FINALE + ELEMENT_AUGMENTATION_MIN)))))
CRIT_AUGMENTE_MAX = (((DEGATS_CRIT_MAX) + (((DEGATS_MAX*augmentation/100 - DEFENSE_FINALE + ELEMENT_AUGMENTATION_MAX)))))


print('degats minimum',DEGATS_MIN)
print('degats max',DEGATS_MAX)
print('degats augmente min',DEGATS_AUGMENTE_MIN)
print('degats augmente max ', DEGATS_AUGMENTE_MAX)
print('degats crit min', DEGATS_CRIT_MIN)
print('degats crit max', DEGATS_CRIT_MAX)
print('degats augmente crit min',CRIT_AUGMENTE_MIN)
print('degats augmente crit max',CRIT_AUGMENTE_MAX)
os.system('pause')
