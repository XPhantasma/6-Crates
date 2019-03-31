import pygame
import datetime
from Settings import *
from Sprites import *
from os import path
import os
import time


class MainGame:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.title_text = pygame.font.SysFont('Arial', 75, True, False)
        self.regular_text = pygame.font.SysFont('Arial', 40, False, False)
        self.small_text = pygame.font.SysFont('Arial', 20, False, False)

        self.clock = pygame.time.Clock()

        self.keypress = False

        # level variable for map levels x/6
        self.level = 1
        # Checks if crate is on correct tile
        self.basic_crate_check = False
        self.double_crate_check = False
        self.slippy_crate_check = False
        self.tele_crate_check = False
        self.teleback_crate_check = False
        self.reverse_slippy_crate_check = False

        # variables for the state of the game All false = close game
        self.run = True
        self.main_menu = True
        self.how_to_play = False
        self.game = False
        self.transition = False

        # sprite variables
        self.player_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        pygame.key.set_repeat(500, 100)
        # Sprite set for player and wall

        # Sprite set for crates
        self.basic_crate_sprite = pygame.sprite.Group()
        self.double_crate_sprite = pygame.sprite.Group()
        self.slippy_crate_sprite = pygame.sprite.Group()
        self.tele_crate_sprite = pygame.sprite.Group()
        self.teleback_crate_sprite = pygame.sprite.Group()
        self.reverse_slippy_crate_sprite = pygame.sprite.Group()

        # # Sprite set for tiles
        self.basic_tile_sprite = pygame.sprite.Group()
        self.double_tile_sprite = pygame.sprite.Group()
        self.slippy_tile_sprite = pygame.sprite.Group()
        self.tele_tile_sprite = pygame.sprite.Group()
        self.teleback_tile_sprite = pygame.sprite.Group()
        self.reverse_slippy_tile_sprite = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

        pygame.display.set_caption("6-Crates")

    # -------------------------------------------------------------
    # Universal functions
    def screenshot_path(self):
        now = datetime.datetime.now()
        return now.strftime('screenshot_%Y-%m-%d_%H_%M_%S.%f.png')

    def close_game(self):
        self.run = False
        self.main_menu = False
        self.how_to_play = False
        self.game = False

    def new(self):
        self.screen.fill((0, 0, 0))
        if self.main_menu:
            self.menu_draw_and_text()
        elif self.how_to_play:
            self.how_to_play_draw_and_text()
        elif self.game:
            self.gameplay_draw()

    # -------------------------------------------------------------
    # function for when the game is running
    def running(self):
        self.new()
        while self.main_menu:
            self.main_menu_event()

        while self.how_to_play:
            self.how_to_play_event()

        while self.game:
            self.gameplay_events()
            self.gameplay_update()

    # -------------------------------------------------------------
    # Main menu set of functions
    def menu_draw_and_text(self):
        text = self.title_text.render('6 - ', False, WHITE)
        self.screen.blit(text, (300, 40))
        crates = ['C', 'R', 'A', 'T', 'E', 'S']
        crate_color = [BROWN, YELLOW, BLUE, PURPLE, ORANGE, CYAN]

        for l in range(0, 6):
            text = self.title_text.render(str(crates[l]), False, crate_color[l])
            self.screen.blit(text, (380 + (50 * l), 40))

        pygame.draw.rect(self.screen, GREEN, [50, 150, 200, 75], 5)
        text = self.regular_text.render("Start Game", False, WHITE)
        self.screen.blit(text, (60, 160))

        pygame.draw.rect(self.screen, BLUE, [50, 300, 200, 75], 5)
        text = self.regular_text.render("How 2 Play", False, WHITE)
        self.screen.blit(text, (60, 310))

        pygame.draw.rect(self.screen, RED, [50, 450, 200, 75], 5)
        text = self.regular_text.render("Exit Game", False, WHITE)
        self.screen.blit(text, (60, 460))

        image1 = pygame.image.load(os.path.join("Crate_sprites", "BasicCrate.png")).convert()
        image2 = pygame.image.load(os.path.join("Crate_sprites", "DoubleCrate.png")).convert()
        image3 = pygame.image.load(os.path.join("Crate_sprites", "SlippyCrate.png")).convert()
        image4 = pygame.image.load(os.path.join("Crate_sprites", "TeleCrate.png")).convert()
        image5 = pygame.image.load(os.path.join("Crate_sprites", "TeleBackCrate.png")).convert()
        image6 = pygame.image.load(os.path.join("Crate_sprites", "ReverseSlippyCrate.png")).convert()
        image7 = pygame.image.load(os.path.join("Player_Sprites", "PlayerD.png")).convert()

        self.screen.blit(image1, (450, 400))
        self.screen.blit(image2, (500, 400))
        self.screen.blit(image3, (550, 400))
        self.screen.blit(image4, (475, 350))
        self.screen.blit(image5, (525, 350))
        self.screen.blit(image6, (500, 300))
        self.screen.blit(image7, (350, 400))

        pygame.display.flip()

    def main_menu_event(self):
        self.clock.tick(FPS)
        keys = pygame.key.get_pressed()
        clicks = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.run:
                    self.close_game()

            if keys[pygame.K_F12]:
                pygame.image.save(self.screen, self.screenshot_path())

            if keys[pygame.K_ESCAPE]:
                if self.run:
                    self.close_game()

            if clicks[pygame.mouse.get_pressed()[0]]:
                x, y = pygame.mouse.get_pos()
                self.menu_click_check(x, y)

    def menu_click_check(self, x_pos, y_pos):
        x = x_pos
        y = y_pos

        # checks if user clicks start game
        if 53 <= x <= 245 and 153 <= y <= 221:
            self.main_menu = False
            self.game = True
            self.transition = True
            self.gamestart_transition()
            self.new()
        # checks if user clicks howtoplay
        if 53 <= x <= 245 and 303 <= y <= 371:
            self.main_menu = False
            self.how_to_play = True
            self.new()
        # checks if user clicks exit
        if 53 <= x <= 245 and 453 <= y <= 521:
            self.close_game()

    # -------------------------------------------------------------
    # How to play set of functions Add Detailed Instructions how to play later

    def how_to_play_draw_and_text(self):
        text = self.title_text.render("Instructions", False, WHITE)
        self.screen.blit(text, (SCREENWIDTH / 4, 50))

        text = self.regular_text.render("Arrow keys = Up, Down, Left, right,", False, WHITE)
        self.screen.blit(text, (SCREENWIDTH / 8, 180))

        text = self.regular_text.render("R = Reset level", False, WHITE)
        self.screen.blit(text, (SCREENWIDTH / 8, 300))

        text = self.regular_text.render("arrow keys -> Spacebar = Interact", False, WHITE)
        self.screen.blit(text, (SCREENWIDTH / 8, 240))

        text = self.regular_text.render("Spacebar -> R = Quit to main menu", False, WHITE)
        self.screen.blit(text, (SCREENWIDTH / 8, 360))

        pygame.draw.rect(self.screen, RED, [50, 450, 200, 75], 5)
        text = self.regular_text.render("Return", False, WHITE)
        self.screen.blit(text, (60, 460))

        pygame.display.flip()

    def how_to_play_event(self):
        self.clock.tick(FPS)
        keys = pygame.key.get_pressed()
        clicks = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.run:
                    self.close_game()

            if keys[pygame.K_F12]:
                pygame.image.save(self.screen, self.screenshot_path())

            if keys[pygame.K_ESCAPE]:
                if self.run:
                    self.close_game()

            if clicks[pygame.mouse.get_pressed()[0]]:
                x, y = pygame.mouse.get_pos()
                if 53 <= x <= 245 and 453 <= y <= 521:
                    self.main_menu = True
                    self.how_to_play = False

    # -------------------------------------------------------------
    # Transition set of functions

    def gamestart_transition(self):
        self.screen.fill((0, 0, 0))

        text = self.title_text.render("Crate Characteristics", True, WHITE)
        self.screen.blit(text, (SCREENWIDTH / 8, 50))

        image = pygame.image.load(os.path.join("Crate_sprites", "BasicCrate.png")).convert()
        text1 = self.small_text.render("Basic Crate", False, LIGHTTAN)
        text2 = self.small_text.render("Pushes crate in general direction", False, LIGHTTAN)
        self.screen.blit(image, (SCREENWIDTH / 8, 150))
        self.screen.blit(text1, (SCREENWIDTH / 5, 150))
        self.screen.blit(text2, (SCREENWIDTH / 5, 175))

        image = pygame.image.load(os.path.join("Crate_sprites", "DoubleCrate.png")).convert()
        text1 = self.small_text.render("Double Crate", False, YELLOW)
        text2 = self.small_text.render("Pushes crate twice as far", False, YELLOW)
        self.screen.blit(image, (SCREENWIDTH / 8, 250))
        self.screen.blit(text1, (SCREENWIDTH / 5, 250))
        self.screen.blit(text2, (SCREENWIDTH / 5, 275))

        image = pygame.image.load(os.path.join("Crate_sprites", "SlippyCrate.png")).convert()
        text1 = self.small_text.render("Slippy Crate", False, BLUE)
        text2 = self.small_text.render("Pushed crate slides all the way", False, BLUE)
        self.screen.blit(image, (SCREENWIDTH / 8, 350))
        self.screen.blit(text1, (SCREENWIDTH / 5, 350))
        self.screen.blit(text2, (SCREENWIDTH / 5, 375))

        image = pygame.image.load(os.path.join("Crate_sprites", "TeleCrate.png")).convert()
        self.screen.blit(image, (SCREENWIDTH / 2, 150))
        text1 = self.small_text.render("Teleporting Crate", False, PURPLE)
        text2 = self.small_text.render("Pushed crate until it meets a wall", False, PURPLE)
        text3 = self.small_text.render("or crate, then teleports across one tile", False, PURPLE)
        self.screen.blit(text1, ((SCREENWIDTH / 2) + 60, 150))
        self.screen.blit(text2, ((SCREENWIDTH / 2) + 60, 175))
        self.screen.blit(text3, ((SCREENWIDTH / 2) + 60, 200))

        image = pygame.image.load(os.path.join("Crate_sprites", "TeleBackCrate.png")).convert()
        self.screen.blit(image, (SCREENWIDTH / 2, 250))
        text1 = self.small_text.render("Tele-back Crate", False, ORANGE)
        text2 = self.small_text.render("attempts to push teleports behind player", False, ORANGE)
        self.screen.blit(text1, ((SCREENWIDTH / 2) + 60, 250))
        self.screen.blit(text2, ((SCREENWIDTH / 2) + 60, 275))

        image = pygame.image.load(os.path.join("Crate_sprites", "ReverseSlippyCrate.png")).convert()
        text1 = self.small_text.render("Pushback Crate", False, CYAN)
        text2 = self.small_text.render("Pushed crate push player back twice as far", False, CYAN)
        text3 = self.small_text.render("all the way until player hits wall", False, CYAN)
        self.screen.blit(image, (SCREENWIDTH / 2, 350))
        self.screen.blit(text1, ((SCREENWIDTH / 2) + 60, 350))
        self.screen.blit(text2, ((SCREENWIDTH / 2) + 60, 375))
        self.screen.blit(text3, ((SCREENWIDTH / 2) + 60, 400))

        pygame.draw.rect(self.screen, RED, [50, 450, 200, 75], 5)
        text = self.regular_text.render("Proceed", False, WHITE)
        self.screen.blit(text, (60, 460))
        pygame.display.flip()

        self.transition_events()

    def level2_transition(self):
        self.screen.fill((0, 0, 0))
        text = self.regular_text.render("Tip: If a mistake is made, Pressing 'r'", False, WHITE)
        self.screen.blit(text, (60, 200))
        text = self.regular_text.render("will reset the level", False, WHITE)
        self.screen.blit(text, (60, 250))

        pygame.draw.rect(self.screen, RED, [50, 450, 200, 75], 5)
        text = self.regular_text.render("Proceed", False, WHITE)
        self.screen.blit(text, (60, 460))
        pygame.display.flip()

        self.transition_events()

    def winner_transition(self):
        self.screen.fill((0, 0, 0))
        text = self.title_text.render("Congratulations!", False, WHITE)
        self.screen.blit(text, (60, 60))

        text = self.regular_text.render("You've solved all 6 levels!", False, WHITE)
        self.screen.blit(text, (60, 160))

        text = self.regular_text.render("Thanks for playing.", False, WHITE)
        self.screen.blit(text, (60, 210))

        image1 = pygame.image.load(os.path.join("Crate_sprites", "BasicCrate.png")).convert()
        image2 = pygame.image.load(os.path.join("Crate_sprites", "DoubleCrate.png")).convert()
        image3 = pygame.image.load(os.path.join("Crate_sprites", "SlippyCrate.png")).convert()
        image4 = pygame.image.load(os.path.join("Crate_sprites", "TeleCrate.png")).convert()
        image5 = pygame.image.load(os.path.join("Crate_sprites", "TeleBackCrate.png")).convert()
        image6 = pygame.image.load(os.path.join("Crate_sprites", "ReverseSlippyCrate.png")).convert()
        image7 = pygame.image.load(os.path.join("Player_Sprites", "PlayerD.png")).convert()

        self.screen.blit(image1, (500, 500))
        self.screen.blit(image2, (500, 450))
        self.screen.blit(image3, (500, 400))
        self.screen.blit(image4, (500, 350))
        self.screen.blit(image5, (500, 300))
        self.screen.blit(image6, (500, 250))
        self.screen.blit(image7, (500, 200))

        pygame.draw.rect(self.screen, RED, [50, 450, 200, 75], 5)
        text = self.regular_text.render("Proceed", False, WHITE)
        self.screen.blit(text, (60, 460))
        pygame.display.flip()

        self.transition_events()

    def credits_transition(self):
        self.screen.fill((0, 0, 0))
        text = self.title_text.render("Credits", False, WHITE)
        self.screen.blit(text, (60, 60))

        text = self.regular_text.render("Programmer", False, WHITE)
        self.screen.blit(text, (60, 160))

        text = self.small_text.render("Phantasma", False, WHITE)
        self.screen.blit(text, (70, 210))

        text = self.regular_text.render("Level Design", False, WHITE)
        self.screen.blit(text, (60, 250))

        text = self.small_text.render("Phantasma", False, WHITE)
        self.screen.blit(text, (70, 300))

        text = self.regular_text.render("Gameplay Testing", False, WHITE)
        self.screen.blit(text, (60, 330))

        text = self.small_text.render("Phantasma", False, WHITE)
        self.screen.blit(text, (70, 380))

        text = self.regular_text.render("Sprite Art", False, WHITE)
        self.screen.blit(text, (460, 160))

        text = self.small_text.render("Phantasma", False, WHITE)
        self.screen.blit(text, (470, 210))

        text = self.regular_text.render("Level Testing", False, WHITE)
        self.screen.blit(text, (460, 250))

        text = self.small_text.render("Phantasma", False, WHITE)
        self.screen.blit(text, (470, 300))

        text = self.regular_text.render("Animation", False, WHITE)
        self.screen.blit(text, (460, 330))

        text = self.small_text.render("Phantasma", False, WHITE)
        self.screen.blit(text, (470, 380))

        pygame.draw.rect(self.screen, RED, [50, 450, 200, 75], 5)
        text = self.regular_text.render("Return", False, WHITE)
        self.screen.blit(text, (60, 460))
        pygame.display.flip()

        self.level = 1
        self.main_menu = True

        self.transition_events()

    def transition_events(self):
        while self.transition:
            self.clock.tick(FPS)
            keys = pygame.key.get_pressed()
            clicks = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.run:
                        self.transition = False
                        self.close_game()

                if keys[pygame.K_F12]:
                    pygame.image.save(self.screen, self.screenshot_path())

                if keys[pygame.K_ESCAPE]:
                    if self.run:
                        self.transition = False
                        self.close_game()

                if clicks[pygame.mouse.get_pressed()[0]]:
                    x, y = pygame.mouse.get_pos()
                    if 53 <= x <= 245 and 453 <= y <= 521:
                        self.transition = False

    # -------------------------------------------------------------
    # gameplay set of functions

    def gameplay_draw(self):
        self.load_level()
        # self.draw_grid()
        for row, tiles in enumerate(self.mapdata):
            for col, tile in enumerate(tiles):
                # player and wall spawning
                if tile == '1':
                    self.wall = Wall(self, col, row)
                    self.wall_sprites.add(self.wall)
                if tile == 'P':
                    self.player = Player(self, col, row)
                    self.player_sprites.add(self.player)

                # Crate spawning
                if tile == 'C':
                    self.basic_crate = NormalCrate(self, col, row)
                    self.basic_crate_sprite.add(self.basic_crate)
                    self.basic_crate.update()
                if tile == 'D':
                    self.double_crate = DoubleCrate(self, col, row)
                    self.double_crate_sprite.add(self.double_crate)
                    self.double_crate.update()
                if tile == 'S':
                    self.slippy_crate = SlippyCrate(self, col, row)
                    self.slippy_crate_sprite.add(self.slippy_crate)
                    self.slippy_crate.update()
                if tile == 'T':
                    self.tele_crate = TeleCrate(self, col, row)
                    self.tele_crate_sprite.add(self.tele_crate)
                    self.tele_crate.update()
                if tile == 'B':
                    self.teleback_crate = TeleBackCrate(self, col, row)
                    self.teleback_crate_sprite.add(self.teleback_crate)
                    self.teleback_crate.update()
                if tile == 'R':
                    self.reverse_slippy_crate = ReverseSlippyCrate(self, col, row)
                    self.reverse_slippy_crate_sprite.add(self.reverse_slippy_crate)
                    self.reverse_slippy_crate.update()

                # Tile spawning
                if tile == 'c':
                    self.basic_tile = NormalTile(self, col, row)
                    self.basic_tile_sprite.add(self.basic_tile)
                if tile == 'd':
                    self.double_tile = DoubleTile(self, col, row)
                    self.double_tile_sprite.add(self.double_tile)
                if tile == 's':
                    self.slippy_tile = SlippyTile(self, col, row)
                    self.slippy_tile_sprite.add(self.slippy_tile)
                if tile == 't':
                    self.tele_tile = TeleTile(self, col, row)
                    self.tele_tile_sprite.add(self.tele_tile)
                if tile == 'b':
                    self.teleback_tile = TeleBackTile(self, col, row)
                    self.teleback_tile_sprite.add(self.teleback_tile)
                if tile == 'r':
                    self.reverse_slippy_tile = ReverseSlippyTile(self, col, row)
                    self.reverse_slippy_tile_sprite.add(self.reverse_slippy_tile)

        # draw the wall
        self.wall_sprites.draw(self.screen)
        pygame.display.update()

    def load_level(self):
        for x in range(1, 7):
            if self.level == x:
                maplevel = path.dirname(__file__)
                self.mapdata = []
                with open(path.join(maplevel, "Map_Levels", 'Map' + str(x)), 'rt') as tile:
                    for line in tile:
                        self.mapdata.append(line)

    def gameplay_events(self):
        self.clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.run:
                    self.close_game()
            # -------------------------------------------------------------
            # Key controls for player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    for x in range(0, 10):
                        self.player.movement(dx=+1)
                        self.player.update()
                        # time.sleep(.001)
                        self.gameplay_update()

                if event.key == pygame.K_LEFT:
                    for x in range(0, 10):
                        self.player.movement(dx=-1)
                        self.player.update()
                        # time.sleep(.001)
                        self.gameplay_update()

                if event.key == pygame.K_UP:
                    for y in range(0, 10):
                        self.player.movement(dy=-1)
                        self.player.update()
                        # time.sleep(.001)
                        self.gameplay_update()

                if event.key == pygame.K_DOWN:
                    for y in range(0, 10):
                        self.player.movement(dy=+1)
                        self.player.update()
                        # time.sleep(.001)
                        self.gameplay_update()
                # -------------------------------------------------------------
                # Key controls for interacting with crates
                if keys[pygame.K_RIGHT]:
                    if event.key == pygame.K_SPACE:
                        self.interact(dx=+1)
                if keys[pygame.K_LEFT]:
                    if event.key == pygame.K_SPACE:
                        self.interact(dx=-1)
                if keys[pygame.K_UP]:
                    if event.key == pygame.K_SPACE:
                        self.interact(dy=-1)
                if keys[pygame.K_DOWN]:
                    if event.key == pygame.K_SPACE:
                        self.interact(dy=+1)

                # -------------------------------------------------------------
                # Key controls for reset and quitting game
                if event.key == pygame.K_r:
                    self.reset_level()
                if keys[pygame.K_SPACE]:
                    if event.key == pygame.K_r:
                        self.killeverything()
                        self.level = 1
                        self.main_menu = True
                        self.game = False
                if event.key == pygame.K_F12:
                    pygame.image.save(self.screen, self.screenshot_path())

        self.player.update()

        if keys[pygame.K_ESCAPE]:
            if self.run:
                self.close_game()

    def interact(self, dx=0, dy=0):

        if self.basic_crate.check_direction(dx, dy):
            for x in range(0, 10):
                self.basic_crate.pushcrate(dx, dy)
                self.basic_crate.update()
                time.sleep(.001)
                self.gameplay_update()

            self.basic_tile.tilecheck()

        if self.double_crate.check_direction(dx, dy):
            for d in range(0, 2):
                for x in range(0, 10):
                    self.double_crate.pushcrate(dx, dy)
                    self.double_crate.update()
                    time.sleep(.001)
                    self.gameplay_update()

            self.double_tile.tilecheck()

        if self.slippy_crate.check_direction(dx, dy):
            while not self.slippy_crate.check_collision(dx, dy):
                for x in range(0, 10):
                    self.slippy_crate.pushcrate(dx, dy)
                    self.slippy_crate.update()
                    time.sleep(.001)
                    self.gameplay_update()

            self.slippy_tile.tilecheck()

        if self.tele_crate.check_direction(dx, dy):
            if not self.tele_crate.teleport(dx, dy):
                for x in range(0, 10):
                    self.tele_crate.pushcrate(dx, dy)
                    self.tele_crate.update()
                    time.sleep(.001)
                    self.gameplay_update()
            self.tele_crate.update()
            self.gameplay_update()

            self.tele_tile.tilecheck()

        if self.teleback_crate.check_direction(dx, dy):
            if not self.teleback_crate.teleport(dx, dy):
                pass
            self.teleback_crate.update()
            self.gameplay_update()

            self.teleback_tile.tilecheck()

        if self.reverse_slippy_crate.check_direction(dx, dy):
            while not self.reverse_slippy_crate.check_collision(dx, dy):
                for x in range(0, 10):
                    self.reverse_slippy_crate.pushcrate(dx, dy)
                    self.reverse_slippy_crate.update()
                    self.player.update()
                    time.sleep(.001)
                    self.gameplay_update()

            self.reverse_slippy_tile.tilecheck()

        self.level_complete_check()

    def draw_sprites(self):
        # draw the wall
        self.wall_sprites.draw(self.screen)

        # draw tiles
        self.basic_tile_sprite.draw(self.screen)
        self.double_tile_sprite.draw(self.screen)
        self.slippy_tile_sprite.draw(self.screen)
        self.tele_tile_sprite.draw(self.screen)
        self.teleback_tile_sprite.draw(self.screen)
        self.reverse_slippy_tile_sprite.draw(self.screen)

        # draw crates
        self.basic_crate_sprite.draw(self.screen)
        self.double_crate_sprite.draw(self.screen)
        self.slippy_crate_sprite.draw(self.screen)
        self.tele_crate_sprite.draw(self.screen)
        self.teleback_crate_sprite.draw(self.screen)
        self.reverse_slippy_crate_sprite.draw(self.screen)

        # draw player
        self.player_sprites.draw(self.screen)

        text = self.regular_text.render("level: " + str(self.level) + "/6", False, BLACK)
        self.screen.blit(text, (25, 5))

    def killeverything(self):
        # Kill player and wall
        self.player.kill()
        self.player.remove()

        for wall in self.wall_sprites:
            wall.kill()
            wall.remove()
        # Kill ALL THE CRATES!!!
        self.basic_crate.kill()
        self.basic_crate.remove()
        self.double_crate.kill()
        self.double_crate.remove()
        self.slippy_crate.kill()
        self.slippy_crate.remove()
        self.tele_crate.kill()
        self.tele_crate.remove()
        self.teleback_crate.kill()
        self.teleback_crate.remove()
        self.reverse_slippy_crate.kill()
        self.reverse_slippy_crate.remove()

        # KILL ALL THE TILES
        self.basic_tile.kill()
        self.double_tile.kill()
        self.slippy_tile.kill()
        self.tele_tile.kill()
        self.teleback_tile.kill()
        self.reverse_slippy_tile.kill()

    def gameplay_update(self):
        self.screen.fill((0, 0, 0))
        # self.draw_grid()
        self.draw_sprites()
        pygame.display.update()

    def reset_level(self):
        self.killeverything()
        self.gameplay_draw()

    def level_complete_check(self):
        if self.basic_tile.tilecheck():
            if self.double_tile.tilecheck():
                if self.slippy_tile.tilecheck():
                    if self.tele_tile.tilecheck():
                        if self.teleback_tile.tilecheck():
                            if self.reverse_slippy_tile.tilecheck():

                                self.level += 1
                                if self.level > 6:
                                    self.game = False
                                    self.transition = True
                                    self.winner_transition()
                                    self.transition = True
                                    self.credits_transition()

                                elif self.level <= 6:

                                    self.killeverything()
                                    self.gameplay_draw()

                                if self.level == 2:
                                    self.transition = True
                                    self.level2_transition()


game = MainGame()

while game.run:
    game.running()

pygame.quit()
