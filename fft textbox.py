# Author: Comicalistic
# This program generates a text box using the assets from Final Fantasy Tactics.
# Special thanks to Zenko for providing the portraits from their Daravon bot on FFHacktics
# Special thanks to the awesome people at FFHacktics for helping me along the way!

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import make_grid

### SET UP GLOBAL CONSTANTS HERE
WIDTH = 640
HEIGHT = 191
BACKGROUND_COLOR = "cyan"
darkgrey = (74, 73, 73)

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)

# Set the title of the pygame screen
pygame.display.set_caption("Comics Tactics Text Box Generator")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.LayeredUpdates()
# Set up text box
text_box_background = pygame.image.load("frame.png").convert_alpha()
og_height = text_box_background.get_height()
# Scale text box
text_box_scale = pygame.transform.scale(text_box_background, (640, og_height+50))

# Set up text
unit_name = input("Name? ")
print("When unit searching, generics start with f or m\n for gender. 'fsquire', 'mknight'")
unit = input("Who you looking for? ").lower()
print(unit)
speak = input("What do you want to say? ")
speak2 = input("What else do you want to say? ")
altima = pygame.font.Font("fonts/Altima.ttf", 56)
altima2 = pygame.font.Font("fonts/Altima.ttf", 43)
name = altima.render(f"{unit_name}", True, "darkred")
speak_text = altima2.render(f"{speak}", True, darkgrey)
speak2_text = altima2.render(f"{speak2}", True, darkgrey)

# Unit portaits
ramza = pygame.image.load("portraits/ramza.png").convert_alpha()
ramza_scale = pygame.transform.scale(ramza, (110, 155))

agrias = pygame.image.load("portraits/agrias.png").convert_alpha()
agrias_scale = pygame.transform.scale(agrias, (110, 155))

meliadoul = pygame.image.load("portraits/meliadoul.png").convert_alpha()
meliadoul_scale = pygame.transform.scale(meliadoul, (110,155))

gafgarion = pygame.image.load("portraits/gafgarion.png").convert_alpha()
gafgarion_scale = pygame.transform.scale(gafgarion, (110,155))

orlandeau = pygame.image.load("portraits/orlandaeu.png").convert_alpha()
orlandeau_scale = pygame.transform.scale(orlandeau, (110,155))

elmdore = pygame.image.load("portraits/elmdore.png").convert_alpha
elmdore_scale = pygame.transform.scale(elmdore, 110, 155)
# generics
fsquire = pygame.image.load("portraits/fsquire.png").convert_alpha()
fsquire_scale = pygame.transform.scale(fsquire, (110, 155))
msquire = pygame.image.load("portraits/msquire.png").convert_alpha()
msquire_scale = pygame.transform.scale(msquire, (110, 155))

mchemist = pygame.image.load("portraits/mchemist.png").convert_alpha()
mchemist_scale = pygame.transform.scale(mchemist, (110, 155))
fchemist = pygame.image.load("portraits/fchemist.png").convert_alpha()
fchemist_scale = pygame.transform.scale(fchemist, (110, 155))

fknight = pygame.image.load("portraits/fknight.png").convert_alpha()
fknight_scale = pygame.transform.scale(fknight, (110, 155))
mknight = pygame.image.load("portraits/mknight.png").convert_alpha()
mknight_scale = pygame.transform.scale(mknight, (110, 155))

farcher = pygame.image.load("portraits/farcher.png").convert_alpha()
farcher_scale = pygame.transform.scale(farcher, (110, 155))
marcher = pygame.image.load("portraits/marcher.png").convert_alpha()
marcher_scale = pygame.transform.scale(marcher, (110, 155))

fmonk = pygame.image.load("portraits/fmonk.png").convert_alpha()
fmonk_scale = pygame.transform.scale(fmonk, (110, 155))
mmonk = pygame.image.load("portraits/mmonk.png").convert_alpha()
mmonk_scale = pygame.transform.scale(mmonk, (110, 155))

fpriest = pygame.image.load("portraits/fpriest.png").convert_alpha()
fpriest_scale = pygame.transform.scale(fpriest, (110, 155))
mpriest = pygame.image.load("portraits/mpriest.png").convert_alpha()
mpriest_scale = pygame.transform.scale(mpriest, (110, 155))

fwizard = pygame.image.load("portraits/fwizard.png").convert_alpha()
fwizard_scale = pygame.transform.scale(fwizard, (110, 155))
mwizard = pygame.image.load("portraits/mwizard.png").convert_alpha()
mwizard_scale = pygame.transform.scale(mwizard, (110, 155))

ftimemage = pygame.image.load("portraits/ftimemage.png").convert_alpha()
ftimemage_scale = pygame.transform.scale(ftimemage, (110, 155))
mtimemage = pygame.image.load("portraits/mtimemage.png").convert_alpha()
mtimemage_scale = pygame.transform.scale(mtimemage, (110, 155))

fsummoner = pygame.image.load("portraits/fsummoner.png").convert_alpha()
fsummoner_scale = pygame.transform.scale(fsummoner, (110, 155))
msummoner = pygame.image.load("portraits/msummoner.png").convert_alpha()
msummoner_scale = pygame.transform.scale(msummoner, (110, 155))

fthief = pygame.image.load("portraits/fthief.png").convert_alpha()
fthief_scale = pygame.transform.scale(fthief, (110, 155))
mthief = pygame.image.load("portraits/mthief.png").convert_alpha()
mthief_scale = pygame.transform.scale(mthief, (110, 155))

fmystic = pygame.image.load("portraits/fmystic.png").convert_alpha()
fmystic_scale = pygame.transform.scale(fthief, (110, 155))
mmystic = pygame.image.load("portraits/mmystic.png").convert_alpha()
mmystic_scale = pygame.transform.scale(mmystic, (110, 155))

fgeomancer =pygame.image.load("portraits/fgeomancer.png").convert_alpha()
fgeomancer_scale = pygame.transform.scale(fgeomancer, (110,155))
mgeomancer = pygame.image.load("portraits/mgeomancer.png").convert_alpha()
mgeomancer_scale = pygame.transform.scale(mgeomancer, (110,155))

forator = pygame.image.load("portraits/forator.png").convert_alpha()
forator_scale = pygame.transform.scale(forator, (110, 155))
morator = pygame.image.load("portraits/morator.png").convert_alpha() 
morator_scale = pygame.transform.scale(morator, (110,155))

fdragoon = pygame.image.load("portraits/fdragoon.png").convert_alpha()
fdragoon_scale = pygame.transform.scale(fdragoon, (110,155))
mdragoon = pygame.image.load("portraits/mdragoon.png").convert_alpha()
mdragoon_scale = pygame.transform.scale(mdragoon, (110,155))

fsamurai = pygame.image.load("portraits/fsamurai.png").convert_alpha()
fsamurai_scale = pygame.transform.scale(fsamurai, (110,155))
msamurai = pygame.image.load("portraits/msamurai.png").convert_alpha()
msamurai_scale = pygame.transform.scale(msamurai, (110,155))

fninja = pygame.image.load("portraits/fninja.png").convert_alpha()
fninja_scale = pygame.transform.scale(fninja, (110,155))
mninja = pygame.image.load("portraits/mninja.png").convert_alpha()
mninja_scale = pygame.transform.scale(mninja, (110,155))

farithmetician = pygame.image.load("portraits/farithmetician.png").convert_alpha()
farithmetician_scale = pygame.transform.scale(farithmetician, (110,155))
marithmetician = pygame.image.load("portraits/marithmetician.png").convert_alpha()
marithmetician_scale = pygame.transform.scale(marithmetician, (110,155))

fdancer = pygame.image.load("portraits/dancer.png").convert_alpha()
fdancer_scale = pygame.transform.scale(fdancer, (110,155))
mbard = pygame.image.load("portraits/mbard.png").convert_alpha()
mbard_scale = pygame.transform.scale(mbard, (110,155))

fmime = pygame.image.load("portraits/fmime.png").convert_alpha()
fmime_scale = pygame.transform.scale(fmime, (110,155))
mmime = pygame.image.load("portraits/mmime.png").convert_alpha()
mmime_scale = pygame.transform.scale(mmime, (110,155))

fdark_knight = pygame.image.load("portraits/fdarkk.png").convert_alpha()
fdark_knight_scale = pygame.transform.scale(fdark_knight, (110,155))

fonion_knight = pygame.image.load("portraits/fonion.png").convert_alpha()
fonion_knight_scale = pygame.transform.scale(fonion_knight, (110,155))

# Uncomment this code to show at grid on the screen
# grid = Sprite(make_grid())
# grid.layer = 1000
# all_sprites.add(grid)

# Create a background image (if you will load an image from a file for 
# the background, you can change this next line to load an image)
background = screen.copy()
screen.blit(background, (0, 0))
screen.blit(text_box_scale, (0, 0))
# Name
screen.blit(name, (145, 10))
# Text
screen.blit(speak_text, (145, 60))
screen.blit(speak2_text, (145, 90))
# Choose portrait via prefix
try:
    if unit == "ramza":
        screen.blit(ramza_scale, (25, 20))
    elif unit == "agrias":
        screen.blit(agrias_scale, (25, 20))
    elif unit == "meliadoul":
        screen.blit(meliadoul_scale, (25,20))
    elif unit == "fsquire":
        screen.blit(fsquire_scale, (25, 20))
    elif unit == "msquire":
        screen.blit(msquire_scale, (25, 20))
    elif unit == "mchemist":
        screen.blit(mchemist_scale, (25, 20))
    elif unit == "fchemist":
        screen.blit(fchemist_scale, (25, 20))
    elif unit == "fknight":
        screen.blit(fknight_scale, (25, 20))
    elif unit == "farcher":
        screen.blit(farcher_scale, (25, 20))
    elif unit == "marcher":
        screen.blit(marcher_scale, (25, 20))
    elif unit == "fmonk":
        screen.blit(fmonk_scale, (25, 20))
    elif unit == "mmonk":
        screen.blit(mmonk_scale, (25, 20))
    elif unit == "fpriest":
        screen.blit(fpriest_scale, (25, 20))
    elif unit == "mpriest":
        screen.blit(mpriest_scale, (25, 20))
    elif unit == "fwizard":
        screen.blit(fwizard_scale, (25, 20))
    elif unit == "mwizard":
        screen.blit(mwizard_scale, (25, 20))
    elif unit == "ftimemage":
        screen.blit(ftimemage_scale, (25, 20))
    elif unit == "mtimemage":
        screen.blit(mtimemage_scale, (25, 20))
    elif unit == "fsummoner":
        screen.blit(fsummoner_scale, (25, 20))
    elif unit == "msummoner":
        screen.blit(msummoner_scale, (25, 20))
    elif unit == "fknight":
        screen.blit(fknight_scale, (25, 20))
    elif unit == "mknight":
        screen.blit(mknight_scale, (25, 20))
    elif unit == "fthief":
        screen.blit(fthief_scale, (25, 20))
    elif unit == "mthief":
        screen.blit(mthief_scale, (25, 20))
    elif unit == "fmystic":
        screen.blit(fmystic_scale, (25,20))
    elif unit == "mmystic":
        screen.blit(mmystic_scale, (25,20))
    elif unit == "fgeomancer":
        screen.blit(fgeomancer_scale, (25,20))
    elif unit == "mgeomancer":
        screen.blit(mgeomancer_scale, (25,20))
    elif unit == "forator":
        screen.blit(forator_scale, (25,20))
    elif unit == "morator":
        screen.blit(morator_scale, (25,20))
    elif unit == "fdragoon":
        screen.blit(fdragoon_scale,(25,20))
    elif unit == "mdragoon":
        screen.blit(mdragoon_scale, (25,20))
    elif unit == "fsamurai":
        screen.blit(fsamurai_scale, (25, 20))
    elif unit == "msamurai":
        screen.blit(msamurai_scale, (25,20))
    elif unit == "fninja":
        screen.blit(fninja_scale, (25,20))
    elif unit == "mninja":
        screen.blit(mninja_scale, (25,20))
    elif unit == "farithmetician":
        screen.blit(farithmetician_scale, (25,20))
    elif unit  == "marithmetician":
        screen.blit(marithmetician_scale, (25,20))
    elif unit == "dancer":
        screen.blit(fdancer_scale, (25,20))
    elif unit == "fmime":
        screen.blit(fmime_scale, (25,20))
    elif unit == "mmime":
        screen.blit(mmime_scale, (25,20))
    elif unit == "fdarkk":
        screen.blit(fdark_knight_scale, (25,20))
    elif unit == "fonion":
        screen.blit(fonion_knight_scale, (25,20))
    elif unit == "orlandeau":
        screen.blit(orlandeau_scale, (25,20))
    elif unit == "gafgarion":
        screen.blit(gafgarion_scale, (25,20))
    elif unit == "elmdore":
        screen.blit(elmdore_scale, (25, 20))
except:
    print("Invalid unit!")
    unit = input("Who you looking for? ").lower()
### SET UP YOUR GAME HERE


# Main Loop
running = True
while running:
    # Set the frame rate to 60 frames per second
    clock.tick(60)
    
    ### MANAGE IN-GAME EVENTS HERE
    pygame.image.save(screen, "textbox.png")
    for event in pygame.event.get():
        # If the quit (X) button is pressed, end the program
        if event.type == QUIT:
            running = False
            
        
            
    ### MANAGE IN-GAME LOGIC HERE
    
    

    # Update the sprites' locations
    all_sprites.update()

    # Redraw the background where the sprites were
    all_sprites.clear(screen, background)

    # Redraw the sprites
    all_sprites.draw(screen)
    
    # Flip the changes to the screen to the computer display
    pygame.display.flip()
    