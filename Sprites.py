import pygame
from Settings import *
import os

# --------------------------------------------
# Player class


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.player_sprites
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.getimages()
        self.image = self.sprite_direction[1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x_pos = x * TILESIZE
        self.y_pos = y * TILESIZE
        self.rect.x = x
        self.rect.y = y

    def getimages(self):
        self.sprite_direction = [pygame.image.load(os.path.join("Player_Sprites", "PlayerU.png")).convert(),
                                 pygame.image.load(os.path.join("Player_Sprites", "PlayerD.png")).convert(),
                                 pygame.image.load(os.path.join("Player_Sprites", "PlayerL.png")).convert(),
                                 pygame.image.load(os.path.join("Player_Sprites", "PlayerR.png")).convert()]

    def movement(self, dx=0, dy=0):
        if not self.collisions(dx, dy):
            self.x_pos += dx * 5
            self.y_pos += dy * 5

        if dx > 0:
            self.image = self.sprite_direction[3]
            self.image.set_colorkey(BLACK)
        if dx < 0:
            self.image = self.sprite_direction[2]
            self.image.set_colorkey(BLACK)
        if dy > 0:
            self.image = self.sprite_direction[1]
            self.image.set_colorkey(BLACK)
        if dy < 0:
            self.image = self.sprite_direction[0]
            self.image.set_colorkey(BLACK)


    def collisions(self, dx=0, dy=0):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos + (dx * TILESIZE)) and wall.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.tele_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        return False

    def update(self):
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
        # * TILESIZE


# --------------------------------------------
# Wall class


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.player_sprites, game.wall_sprites
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        for l in range(1, 7):
            if game.level == l:
                self.image = pygame.image.load(os.path.join("Wall_Sprites", ("Level" + str(l) + "Wall" + ".png")))
                break
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

# # --------------------------------------------
# # Crate class sets


class NormalCrate(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Crate_sprites", "BasicCrate.png")).convert()
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def check_direction(self, dx=0, dy=0):
        for side in self.game.player_sprites:
            if self.rect.left == side.rect.right and self.rect.top == side.rect.top and dx == 1:
                return True
            if self.rect.right == side.rect.left and self.rect.top == side.rect.top and dx == -1:
                return True
            if self.rect.top == side.rect.bottom and self.rect.left == side.rect.left and dy == 1:
                return True
            if self.rect.bottom == side.rect.top and self.rect.left == side.rect.left and dy == -1:
                return True

    def check_collision(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos + (dx * TILESIZE)) and wall.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.tele_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        return False

    def pushcrate(self, dx=0, dy=0):
        if not self.check_collision(dx, dy):
            self.rect.x += dx * 5
            self.rect.y += dy * 5

    def update(self):
        self.x_pos = self.rect.x
        self.y_pos = self.rect.y


class DoubleCrate(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Crate_sprites", "DoubleCrate.png")).convert()
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def check_direction(self, dx=0, dy=0):
        for side in self.game.player_sprites:
            if self.rect.left == side.rect.right and self.rect.top == side.rect.top and dx == 1:
                return True
            if self.rect.right == side.rect.left and self.rect.top == side.rect.top and dx == -1:
                return True
            if self.rect.top == side.rect.bottom and self.rect.left == side.rect.left and dy == 1:
                return True
            if self.rect.bottom == side.rect.top and self.rect.left == side.rect.left and dy == -1:
                return True

    def check_collision(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos + (dx * TILESIZE)) and wall.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.tele_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        return False

    def pushcrate(self, dx=0, dy=0):
        if not self.check_collision(dx, dy):
            self.rect.x += dx * 5
            self.rect.y += dy * 5

    def update(self):
        self.x_pos = self.rect.x
        self.y_pos = self.rect.y


class SlippyCrate(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Crate_sprites", "SlippyCrate.png")).convert()
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def check_direction(self, dx=0, dy=0):
        for side in self.game.player_sprites:
            if self.rect.left == side.rect.right and self.rect.top == side.rect.top and dx == 1:
                return True
            if self.rect.right == side.rect.left and self.rect.top == side.rect.top and dx == -1:
                return True
            if self.rect.top == side.rect.bottom and self.rect.left == side.rect.left and dy == 1:
                return True
            if self.rect.bottom == side.rect.top and self.rect.left == side.rect.left and dy == -1:
                return True

    def check_collision(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos + (dx * TILESIZE)) and wall.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.tele_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        return False

    def pushcrate(self, dx=0, dy=0):
        if not self.check_collision(dx, dy):
            self.rect.x += dx * 5
            self.rect.y += dy * 5

    def update(self):
        self.x_pos = self.rect.x
        self.y_pos = self.rect.y


class TeleCrate(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Crate_sprites", "TeleCrate.png")).convert()
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def check_direction(self, dx=0, dy=0):
        for side in self.game.player_sprites:
            if self.rect.left == side.rect.right and self.rect.top == side.rect.top and dx == 1:
                return True
            if self.rect.right == side.rect.left and self.rect.top == side.rect.top and dx == -1:
                return True
            if self.rect.top == side.rect.bottom and self.rect.left == side.rect.left and dy == 1:
                return True
            if self.rect.bottom == side.rect.top and self.rect.left == side.rect.left and dy == -1:
                return True

    def check_collision(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos + (dx * TILESIZE)) and wall.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * TILESIZE)) and side.rect.y == self.y_pos + (dy * TILESIZE):
                return True
        return False

    def check_telespot(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos + (dx * (TILESIZE * 2))) and wall.rect.y == self.y_pos + (dy * (TILESIZE * 2)):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos + (dy * (TILESIZE * 2)):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos + (dy * (TILESIZE * 2)):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos + (dy * (TILESIZE * 2)):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos + (dy * (TILESIZE * 2)):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos + (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos + (dy * (TILESIZE * 2)):
                return True
        return False

    def pushcrate(self, dx=0, dy=0):
        if not self.check_collision(dx, dy):
            self.rect.x += dx * 5
            self.rect.y += dy * 5

    def teleport(self, dx=0, dy=0):
        if self.check_collision(dx, dy):
            if not self.check_telespot(dx, dy):
                self.rect.x += ((dx * TILESIZE) * 2)
                self.rect.y += ((dy * TILESIZE) * 2)
            return True
        return False

    def update(self):
        self.x_pos = self.rect.x
        self.y_pos = self.rect.y


class TeleBackCrate(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Crate_sprites", "TeleBackCrate.png")).convert()
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def check_direction(self, dx=0, dy=0):
        for side in self.game.player_sprites:
            if self.rect.left == side.rect.right and self.rect.top == side.rect.top and dx == 1:
                return True
            if self.rect.right == side.rect.left and self.rect.top == side.rect.top and dx == -1:
                return True
            if self.rect.top == side.rect.bottom and self.rect.left == side.rect.left and dy == 1:
                return True
            if self.rect.bottom == side.rect.top and self.rect.left == side.rect.left and dy == -1:
                return True

    def check_telespot(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and wall.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.tele_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.reverse_slippy_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        return False

    def teleport(self, dx=0, dy=0):
        if not self.check_telespot(dx, dy):
            self.rect.x -= ((dx * TILESIZE) * 2)
            self.rect.y -= ((dy * TILESIZE) * 2)
            return True
        return False

    def update(self):
        self.x_pos = self.rect.x
        self.y_pos = self.rect.y


class ReverseSlippyCrate(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("Crate_sprites", "ReverseSlippyCrate.png")).convert()
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def check_direction(self, dx=0, dy=0):
        for side in self.game.player_sprites:
            if self.rect.left == side.rect.right and self.rect.top == side.rect.top and dx == 1:
                return True
            if self.rect.right == side.rect.left and self.rect.top == side.rect.top and dx == -1:
                return True
            if self.rect.top == side.rect.bottom and self.rect.left == side.rect.left and dy == 1:
                return True
            if self.rect.bottom == side.rect.top and self.rect.left == side.rect.left and dy == -1:
                return True

    def check_collision(self, dx, dy):
        for wall in self.game.wall_sprites:
            if wall.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and wall.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.basic_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.double_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.tele_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.teleback_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        for side in self.game.slippy_crate_sprite:
            if side.rect.x == (self.x_pos - (dx * (TILESIZE * 2))) and side.rect.y == self.y_pos - (dy * (TILESIZE * 2)):
                return True
        return False

    def pushcrate(self, dx=0, dy=0):
        if not self.check_collision(dx, dy):
            self.rect.x -= dx * 5
            self.rect.y -= dy * 5
            self.game.player.x_pos -= dx * 5
            self.game.player.y_pos -= dy * 5

    def update(self):
        self.x_pos = self.rect.x
        self.y_pos = self.rect.y

# --------------------------------------------
# Tile class Sets


class NormalTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(LIGHTTAN)
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def tilecheck(self):
        if self.rect.x == self.game.basic_crate.rect.x:
            if self.rect.y == self.game.basic_crate.rect.y:
                return True
            else:
                return False


class DoubleTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def tilecheck(self):
        if self.rect.x == self.game.double_crate.rect.x:
            if self.rect.y == self.game.double_crate.rect.y:
                return True
            else:
                return False


class SlippyTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def tilecheck(self):
        if self.rect.x == self.game.slippy_crate.rect.x:
            if self.rect.y == self.game.slippy_crate.rect.y:
                return True
            else:
                return False


class TeleTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def tilecheck(self):
        if self.rect.x == self.game.tele_crate.rect.x:
            if self.rect.y == self.game.tele_crate.rect.y:
                return True
            else:
                return False


class TeleBackTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def tilecheck(self):
        if self.rect.x == self.game.teleback_crate.rect.x:
            if self.rect.y == self.game.teleback_crate.rect.y:
                return True
            else:
                return False


class ReverseSlippyTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def tilecheck(self):
        if self.rect.x == self.game.reverse_slippy_crate.rect.x:
            if self.rect.y == self.game.reverse_slippy_crate.rect.y:
                return True
            else:
                return False
