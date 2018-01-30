import os

print('pve_dander/pve_6.2/pvp_escri/pvp_archer_93/pvp_archer_hero')
reference = input('')
reference = str(reference)

print('Vous utilisez dist/cac/mag')
atk = input('')
atk = str(atk)

if reference == 'pve_dander':
    if atk == 'dist':
        from reference_dander import * 
        perso_def_base = perso_def_base_dist
        def_equip = def_equip_dist
        def_rune = def_rune_dist
        
    if atk == 'cac':
        from reference_dander import *
        perso_def_base = perso_def_base_cac
        def_equip = def_equip_cac
        def_rune = def_rune_cac
    if atk == 'mag':
        from reference_dander import *
        perso_def_base = perso_def_base_mag
        def_equip = def_equip_mag
        def_rune = def_rune_mag

if reference == 'pvp_escri':
    if atk == 'dist':
        from reference_escri import * 
        perso_def_base = perso_def_base_dist
        def_equip = def_equip_dist
        def_rune = def_rune_dist
    if atk == 'cac':
        from reference_escri import *
        perso_def_base = perso_def_base_cac
        def_equip = def_equip_cac
        def_rune = def_rune_cac
    if atk == 'mag':
        from reference_escri import *
        perso_def_base = perso_def_base_mag
        def_equip = def_equip_mag
        def_rune = def_rune_mag

if reference == 'pvp_archer_hero':
    if atk == 'dist':
        from reference_archer_nana import * 
        perso_def_base = perso_def_base_dist
        def_equip = def_equip_dist
        def_rune = def_rune_dist
    if atk == 'cac':
        from reference_archer_nana import *
        perso_def_base = perso_def_base_cac
        def_equip = def_equip_cac
        def_rune = def_rune_cac
    if atk == 'mag':
        from reference_archer_nana import *
        perso_def_base = perso_def_base_mag
        def_equip = def_equip_mag
        def_rune = def_rune_mag

if reference == 'pvp_archer_93':
    if atk == 'dist':
        from reference_archer import * 
        perso_def_base = perso_def_base_dist
        def_equip = def_equip_dist
        def_rune = def_rune_dist
        
    if atk == 'cac':
        from reference_archer import *
        perso_def_base = perso_def_base_cac
        def_equip = def_equip_cac
        def_rune = def_rune_cac
    if atk == 'mag':
        from reference_archer import *
        perso_def_base = perso_def_base_mag
        def_equip = def_equip_mag
        def_rune = def_rune_mag

#ATTAQUE TOTALE = attaque du perso + attaque de la SP + attaque du masque + attaque du tarot + armes + attaque du skill + attaque du buff + attaque de rune + attaque de charge + up de l'attaque final + 15
#ATTAQUE FINALE = ATTAQUE TOTALE x [1+ ([b]S[/b] % pour les dégâts) + (% pour les dégâts sur un type de monstre/en pvp)] x (1+% d'augmentation de dégâts à 15% de chance en pvp) x [1+ (% d'augmentation de dégâts de l'arme principale) + (% d'augmentation de dégâts de l'arme secondaire)]

print('attaque du perso min (arme enlevé fiche perso min=max)')
perso_min = input()
perso_min = int(perso_min)

print('attaque du perso max (arme enlevé fiche perso min=max) ')
perso_max = input()
perso_max = int(perso_max)

print("degats crit de l'arme + degat crit de la rune")
crit_arme = input()
crit_arme = int(crit_arme)

print('attaque du masque')
attaque_masque = input()
attaque_masque = int(attaque_masque)

print('attaque tarot')
attaque_tarot = input()
attaque_tarot = int(attaque_tarot)

print('Up de votre arme 1 2 3... Pas de + devant le chiffre')
up_arme = input()
up_arme = int(up_arme)

up_final_arme = up_arme - up_armure
up_final_arme = int(up_final_arme)


print('arme_min')
attaque_min_arme = input()
attaque_min_arme = int(attaque_min_arme)

print('arme_max')
attaque_max_arme = input()
attaque_max_arme = int(attaque_max_arme)

if up_final_arme == -10:
    attaque_min = attaque_min_arme*(-200/100) + attaque_min_arme
    attaque_max = attaque_max*(-200/100) + attaque_max

if up_final_arme == -9:
    attaque_min = attaque_min_arme*(-120/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-120/100) + attaque_max_arme

if up_final_arme == -8:
    attaque_min = attaque_min_arme*(-90/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-90/100) + attaque_max_arme

if up_final_arme == -7:
    attaque_min = attaque_min_arme*(-65/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-65/100) + attaque_max_arme

if up_final_arme == -6:
    attaque_min = attaque_min_arme*(-54/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-54/100) + attaque_max_arme

if up_final_arme == -5:
    attaque_min = attaque_min_arme*(-43/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-43/100) + attaque_max_arme

if up_final_arme == -4:
    attaque_min = attaque_min_arme*(-32/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-32/100) + attaque_max_arme

if up_final_arme == -3:
    attaque_min = attaque_min_arme*(-22/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-22/100) + attaque_max_arme

if up_final_arme == -2:
    attaque_min = attaque_min_arme*(-15/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-15/100) + attaque_max_arme

if up_final_arme == -1:
    attaque_min = attaque_min_arme*(-10/100) + attaque_min_arme
    attaque_max = attaque_max_arme*(-10/100) + attaque_max_arme
if up_final_arme == 0:
    attaque_min = int(attaque_min_arme)
    attaque_max = int(attaque_max_arme)

if up_final_arme == 1:
    attaque_min = attaque_min_arme*10/100 + attaque_min_arme
    attaque_max = attaque_max_arme*10/100 + attaque_max_arme
    
if up_final_arme == 2:
    attaque_min = attaque_min_arme*15/100 + attaque_min_arme
    attaque_max = attaque_max_arme*15/100 + attaque_max_arme

if up_final_arme == 3:
    attaque_min = attaque_min_arme*22/100 + attaque_min_arme
    attaque_max = attaque_max_arme*22/100 + attaque_max_arme

if up_final_arme == 4:
    attaque_min = attaque_min_arme*32/100 + attaque_min_arme
    attaque_max = attaque_max_arme*32/100 + attaque_max_arme

if up_final_arme == 5:
    attaque_min = attaque_min_arme*43/100 + attaque_min_arme
    attaque_max = attaque_max_arme*43/100 + attaque_max_arme

if up_final_arme == 6:
    attaque_min = attaque_min_arme*54/100 + attaque_min_arme
    attaque_max = attaque_max_arme*54/100 + attaque_max_arme

if up_final_arme == 7:
    attaque_min = attaque_min_arme*65/100 + attaque_min_arme
    attaque_max = attaque_max_arme*65/100 + attaque_max_arme

if up_final_arme == 8:
    attaque_min = attaque_min_arme*90/100 + attaque_min_arme
    attaque_max = attaque_max_arme*90/100 + attaque_max_arme

if up_final_arme == 9:
    attaque_min = attaque_min_arme*120/100 + attaque_min_arme
    attaque_max = attaque_max_arme*120/100 + attaque_max_arme

if up_final_arme == 10:
    attaque_min = attaque_min_arme*200/100 + attaque_min_arme
    attaque_max = attaque_max_arme*200/100 + attaque_max_arme


print('point sp atk ( en comptant les SL )')
point_sp_atk = input()
point_sp_atk = int(point_sp_atk)

print('Amélio sp atk')
amélio_sp_atk = input()
amélio_sp_atk = int(amélio_sp_atk)

print('point element sp ( en comptant les SL )')
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

else :
    attaque_sp = point_sp_atk*10
    


print('attaque skill')
attaque_skill = input()
attaque_skill = int(attaque_skill)

print('attaque buff')
attaque_buff = input()
attaque_buff = int(attaque_buff)

print('attaque de la rune (attaque supplémentaire)')
attaque_rune = input()
attaque_rune = int(attaque_rune)

print('pourcentage degat monstre/pvp/fée/bonus degat(chapeau) (additionner le tout) Ne pas mettre de %')
pourcentage_mob_pvp = input()
pourcentage_mob_pvp = int(pourcentage_mob_pvp)

print('Diminue def en pvp %')
diminue_def = input()
diminue_def = int(diminue_def)

MALUS_DEF = 1 - (diminue_def/100)
ATTAQUE_TOTALE_MIN = perso_max + attaque_min_arme + attaque_sp + attaque_skill + attaque_buff + attaque_rune + 15 + attaque_masque + attaque_tarot
ATTAQUE_TOTALE_MAX = perso_min + attaque_max_arme + attaque_sp + attaque_skill + attaque_buff + attaque_rune + 15 + attaque_masque + attaque_tarot

print('S_degat')
S_degat = input()
S_degat = int(S_degat)

print('Augmentation de degats (Arme principal + arme secondaire, resultats de laddition)')
augmentation = input()
augmentation = int(augmentation)



ATTAQUE_FINAL_MIN = ATTAQUE_TOTALE_MIN*((1+S_degat/100)+(pourcentage_mob_pvp)/100)
ATTAQUE_FINAL_MAX = ATTAQUE_TOTALE_MAX*((1+S_degat/100)+(pourcentage_mob_pvp)/100)



#DÉFENSE TOTALE = défense du perso + défense de la SP + défense du masque + défense du tarot + défense du chapeau + défense des résistances + défense des bijoux + défense de l'équipement + options C/B/A de rune augmentant la défense + up défense final + bonus de défense des monstres 
#def_sp = def_sp*10

DEF_TOTALE = perso_def_base + def_sp + def_masque + def_tarot + def_chapeau + def_res + def_bij + def_equip + def_rune

#Bonus défense = ( 1 + % potion défense + % costume Nosmall + % S pour toutes les défenses + % pour la défense en PVP + % cochon chançard ? + % Huile de fleur de glace ? )



BONUS_DEF = (1 + cost_nos/100 + S_def/100 + def_pvp/100)

#DÉFENSE FINALE = DÉFENSE TOTALE x Bonus défense x Malus défense

DEFENSE_FINALE = (DEF_TOTALE*BONUS_DEF)*MALUS_DEF

#DÉGÂTS PHYSIQUES= (ATTAQUE FINALE - DÉFENSE FINALE) x (1 + Taille de critique)

DEGATS_PHYSIQUES_MIN = (ATTAQUE_FINAL_MIN - DEFENSE_FINALE)
DEGATS_PHYSIQUES_MAX = (ATTAQUE_FINAL_MAX - DEFENSE_FINALE)



 



#Élément du personnage = élément de l'arme principale + élément de l'arme secondaire + élément du masque + élément des résistances + élément des bijoux + élément de rune + élément du skill + élément de buff
print('element arme principale + secondaire (resultat de laddition')
element_arme_principale = input()
element_arme_principale = int(element_arme_principale)

print('element bijou/res/chapeaucost/aile')
element_arme_secondaire = input()
element_arme_secondaire = int(element_arme_secondaire)

print('element de la rune ( Augmente l"élément de X%)')
element_rune = input()
element_rune = int(element_rune)

print('element du skill')
element_skill = input()
element_skill = int(element_skill)

ELEMENT_PERSONNAGE = element_arme_principale + element_arme_secondaire + element_rune + element_skill +element_sp

#Élément de la fée = (Attaque finale + 100) x % de la fée
print('pourcentage de la fée, pas de %')
fee = input()
fee = int(fee)

element_fee_min = (ATTAQUE_FINAL_MIN + 100)*fee/100
element_fee_max = (ATTAQUE_FINAL_MAX + 100)*fee/100
#Résistance adversaire = Résistance de la fiche perso de l'adversaire + résistance de rune de son armure + buff de résistance - débuff de résistance - baisse de résistance de nos équipements - baisse de résistance de rune de notre arme utilisée

res_adv

print('baisse res de notre stuff')
baisse_res = input()
baisse_res = int(baisse_res)

RES_ADV = res_adv - baisse_res

print('Bonus elementaire (0% pour le même élément, 30 si fée contre rien ect...)')
bonus_elementaire = input()
bonus_elementaire = int(bonus_elementaire)

#ÉLÉMENT FINAL = [Élément du perso+ (Attaque finale + 100) x % de la fée ] x (1 + % Bonus élémentaire) x (100% - % résistance finale de l'adversaire)



DEGAT_ELEMENTS_MIN = (ELEMENT_PERSONNAGE+ (ATTAQUE_FINAL_MIN+ 100)*fee/100)*(1 + bonus_elementaire/100)*(1 - RES_ADV/100) #bonus_elementaire% a changé bonus elem
DEGAT_ELEMENTS_MAX = (ELEMENT_PERSONNAGE+ (ATTAQUE_FINAL_MAX+ 100)*fee/100)*(1 + bonus_elementaire/100)*(1 - RES_ADV/100)

#Dégâts = dégâts physiques + dégâts d'élément + dégâts de moral
ELEMENT_AUGMENTATION_MIN = (((ELEMENT_PERSONNAGE + element_fee_min)*(1 + (bonus_elementaire/100)))*(augmentation/100))*((1 - ((res_adv - baisse_res)/100)))
ELEMENT_AUGMENTATION_MAX = (((ELEMENT_PERSONNAGE + element_fee_max)*(1 + (bonus_elementaire/100)))*(augmentation/100))*((1 - ((res_adv - baisse_res)/100)))

DEGATS_MIN = DEGATS_PHYSIQUES_MIN + ELEMENT_AUGMENTATION_MIN
DEGATS_MAX = DEGATS_PHYSIQUES_MAX + ELEMENT_AUGMENTATION_MAX
DEGATS_AUGMENTE_MIN = ((ATTAQUE_FINAL_MIN + ELEMENT_AUGMENTATION_MIN)*(1 + augmentation/100)) - DEFENSE_FINALE
DEGATS_AUGMENTE_MAX = ((ATTAQUE_FINAL_MAX + ELEMENT_AUGMENTATION_MAX)*(1 + augmentation/100)) - DEFENSE_FINALE
DEGATS_CRIT_MIN = (DEGATS_PHYSIQUES_MIN*(1 + ((crit_arme - degats_crit_reduction)/100))) + ELEMENT_AUGMENTATION_MIN
DEGATS_CRIT_MAX = (DEGATS_PHYSIQUES_MAX*(1 + ((crit_arme - degats_crit_reduction)/100))) + ELEMENT_AUGMENTATION_MAX
CRIT_AUGMENTE_MIN = (((DEGATS_MIN*(1 + ((crit_arme - degats_crit_reduction)/100))) + (((ATTAQUE_FINAL_MIN*augmentation/100 + ELEMENT_AUGMENTATION_MIN)))))
CRIT_AUGMENTE_MAX = (((DEGATS_MAX*(1 + ((crit_arme - degats_crit_reduction)/100))) + (((ATTAQUE_FINAL_MAX*augmentation/100 + ELEMENT_AUGMENTATION_MAX)))))


print('Dégats minimum',DEGATS_MIN)
print('Dégats max',DEGATS_MAX)
print('Dégats augmente min',DEGATS_AUGMENTE_MIN)
print('Dégats augmente max ', DEGATS_AUGMENTE_MAX)
print('Dégats crit min', DEGATS_CRIT_MIN)
print('Dégats crit max', DEGATS_CRIT_MAX)
print('Dégats augmente crit min',CRIT_AUGMENTE_MIN)
print('Dégats augmente crit max',CRIT_AUGMENTE_MAX)
os.system('pause')
