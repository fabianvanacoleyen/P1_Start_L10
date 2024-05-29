# Enkele imports
import pygame, sys, breakout_module as b

# Variabelen
venster_breedte = 590
venster_hoogte = 480
bal_positie = [venster_breedte // 2, venster_hoogte // 2]
bal_grootte = 10
blok_breedte = 60
blok_hoogte = 20
blok_rijen = 5
blok_kolommen = venster_breedte // (blok_breedte + 5)
peddel_positie = [venster_breedte //2, venster_hoogte - 20] # Ook een lijst van x- en y- coördinaat. x = midden, y = venster_hoogte - 20
peddel_breedte = 60
peddel_hoogte = 10
peddel_snelheid = 5
klok = pygame.time.Clock()
spel_voorbij = False

# Initialiseer pygame
venster = b.setup_venster(venster_breedte, venster_hoogte)
bal_snelheid = b.initialiseer_bal()
blokken = b.initialiseer_blokken(blok_rijen, blok_kolommen, blok_breedte, blok_hoogte)

def teken_spel():
    global blokken
    venster.fill( (0,0,0) )
    pygame.draw.rect(venster, (255, 255, 255) ,
    (peddel_positie[0] - peddel_breedte // 2, peddel_positie[1], peddel_breedte, peddel_hoogte))

    pygame.draw.circle(venster, (255, 255, 255), bal_positie, bal_grootte)

    for blok in blokken:
        pygame.draw.rect(venster, (255, 255, 255), blok)
    
    pygame.display.update()
def beweeg_peddel():
    toetsen = pygame.key.get_pressed()

    if toetsen[pygame.K_LEFT]:
       peddel_positie[0] -= peddel_snelheid
    if toetsen[pygame.K_RIGHT]:
       peddel_positie[0] += peddel_snelheid

def is_spel_voorbij():
    return (bal_positie[1] >= venster_hoogte or len(blokken) ==0)


while not spel_voorbij:								# Hoofdlus
    for event in pygame.event.get():	# Eventlus
        if event.type == pygame.QUIT:	# Controle van het event
            pygame.quit()
            sys.exit()
    bal_positie, bal_snelheid = b.update_bal()
    teken_spel()	
    beweeg_peddel()
    spel_voorbij = is_spel_voorbij()
    klok.tick(60)			

