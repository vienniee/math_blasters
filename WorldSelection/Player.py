import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, gender):
        super().__init__()
        # image imports
        self.gender = gender

        if self.gender == "male":
            # male
            
            MwalkR1 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walk', 'adventurer-run-00.png')).convert_alpha()
            MwalkR2 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walk', 'adventurer-run-01.png')).convert_alpha()
            MwalkR3 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walk', 'adventurer-run-02.png')).convert_alpha()
            MwalkR4 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walk', 'adventurer-run-03.png')).convert_alpha()
            MwalkR5 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walk', 'adventurer-run-04.png')).convert_alpha()
            MwalkR6 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walk', 'adventurer-run-05.png')).convert_alpha()

            MwalkL1 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walkL', 'adventurer-runL-00.png')).convert_alpha()
            MwalkL2 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walkL', 'adventurer-runL-01.png')).convert_alpha()
            MwalkL3 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walkL', 'adventurer-runL-02.png')).convert_alpha()
            MwalkL4 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walkL', 'adventurer-runL-03.png')).convert_alpha()
            MwalkL5 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walkL', 'adventurer-runL-04.png')).convert_alpha()
            MwalkL6 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'walkL', 'adventurer-runL-05.png')).convert_alpha()

            MidleL = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'idleL', 'L0.png')).convert_alpha()
            MidleR = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'male', 'idle', '0.png')).convert_alpha()

            # crop
            # MwalkL1 = MwalkL1.subsurface((310,10,300,500))
            # MwalkL2 = MwalkL2.subsurface((310,10,300,500))
            # MwalkL3 = MwalkL3.subsurface((310,10,300,500))
            # MwalkL4 = MwalkL4.subsurface((310,10,300,500))
            # MwalkL5 = MwalkL5.subsurface((310,10,300,500))
            # MwalkL6 = MwalkL6.subsurface((310,10,300,500))

            # MwalkR1 = MwalkR1.subsurface((1,10,300,500))
            # MwalkR2 = MwalkR2.subsurface((1,10,300,500))
            # MwalkR3 = MwalkR3.subsurface((1,10,300,500))
            # MwalkR4 = MwalkR4.subsurface((1,10,300,500))
            # MwalkR5 = MwalkR5.subsurface((1,10,300,500))
            # MwalkR6 = MwalkR6.subsurface((1,10,300,500))

            # MidleL = MidleL.subsurface((310,10,300,500))
            # MidleR = MidleR.subsurface((1,10,300,500))

            # scaling
            scale=3

            MwalkR1 = pygame.transform.rotozoom(MwalkR1, 0, scale)
            MwalkR2 = pygame.transform.rotozoom(MwalkR2, 0, scale)
            MwalkR3 = pygame.transform.rotozoom(MwalkR3, 0, scale)
            MwalkR4 = pygame.transform.rotozoom(MwalkR4, 0, scale)
            MwalkR5 = pygame.transform.rotozoom(MwalkR5, 0, scale)
            MwalkR6 = pygame.transform.rotozoom(MwalkR6, 0, scale)

            MwalkL1 = pygame.transform.rotozoom(MwalkL1, 0, scale)
            MwalkL2 = pygame.transform.rotozoom(MwalkL2, 0, scale)
            MwalkL3 = pygame.transform.rotozoom(MwalkL3, 0, scale)
            MwalkL4 = pygame.transform.rotozoom(MwalkL4, 0, scale)
            MwalkL5 = pygame.transform.rotozoom(MwalkL5, 0, scale)
            MwalkL6 = pygame.transform.rotozoom(MwalkL6, 0, scale)

            MidleL = pygame.transform.rotozoom(MidleL, 0, scale)
            MidleR = pygame.transform.rotozoom(MidleR, 0, scale)

            self.walkR = [MwalkR1, MwalkR2, MwalkR3, MwalkR4, MwalkR5, MwalkR6]
            self.walkL = [MwalkL1, MwalkL2, MwalkL3, MwalkL4, MwalkL5, MwalkL6]
            self.idleL = MidleL
            self.idleR = MidleR


        elif self.gender == "female":
            # female
            FwalkR1 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '0.png')).convert_alpha()
            FwalkR2=pygame.image.load(os.path.join(os.path.dirname(
                    __file__), 'player', 'female', 'walk', '1.png')).convert_alpha()
            FwalkR3 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '2.png')).convert_alpha()
            FwalkR4 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '3.png')).convert_alpha()
            FwalkR5 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '4.png')).convert_alpha()
            FwalkR6 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '5.png')).convert_alpha()
            FwalkR7 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '6.png')).convert_alpha()
            FwalkR8 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walk', '7.png')).convert_alpha()
            
            FwalkL1 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L0.png')).convert_alpha()
            FwalkL2 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L1.png')).convert_alpha()
            FwalkL3 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L2.png')).convert_alpha()
            FwalkL4 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L3.png')).convert_alpha()
            FwalkL5 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L4.png')).convert_alpha()
            FwalkL6 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L5.png')).convert_alpha()
            FwalkL7 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L6.png')).convert_alpha()
            FwalkL8 = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'walkL', 'L7.png')).convert_alpha()

            FidleL = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'idleL', 'L0.png')).convert_alpha()
            FidleR = pygame.image.load(os.path.join(os.path.dirname(
                __file__), 'player', 'female', 'idle', '0.png')).convert_alpha()

            # crop
            FwalkL1 = FwalkL1.subsurface((20,0,40,44))
            FwalkL2 = FwalkL2.subsurface((20,0,40,44))
            FwalkL3 = FwalkL3.subsurface((20,0,40,44))
            FwalkL4 = FwalkL4.subsurface((20,0,40,44))
            FwalkL5 = FwalkL5.subsurface((20,0,40,44))
            FwalkL6 = FwalkL6.subsurface((20,0,40,44))
            FwalkL7 = FwalkL7.subsurface((20,0,40,44))
            FwalkL8 = FwalkL8.subsurface((20,0,40,44))

            FwalkR1 = FwalkR1.subsurface((7,0,40,44))
            FwalkR2 = FwalkR2.subsurface((7,0,40,44))
            FwalkR3 = FwalkR3.subsurface((7,0,40,44))
            FwalkR4 = FwalkR4.subsurface((7,0,40,44))
            FwalkR5 = FwalkR5.subsurface((7,0,40,44))
            FwalkR6 = FwalkR6.subsurface((7,0,40,44))
            FwalkR7 = FwalkR7.subsurface((7,0,40,44))
            FwalkR8 = FwalkR8.subsurface((7,0,40,44))

            FidleL = FidleL.subsurface((20,0,40,44))
            FidleR = FidleR.subsurface((7,0,40,44))

            # scaling
            scale=3
            FwalkR2 = pygame.transform.rotozoom(FwalkR2, 0, scale)
            FwalkR1 = pygame.transform.rotozoom(FwalkR1, 0, scale)
            FwalkR3 = pygame.transform.rotozoom(FwalkR3, 0, scale)
            FwalkR4 = pygame.transform.rotozoom(FwalkR4, 0, scale)
            FwalkR5 = pygame.transform.rotozoom(FwalkR5, 0, scale)
            FwalkR6 = pygame.transform.rotozoom(FwalkR6, 0, scale)
            FwalkR7 = pygame.transform.rotozoom(FwalkR7, 0, scale)
            FwalkR8 = pygame.transform.rotozoom(FwalkR8, 0, scale)


            FwalkL1 = pygame.transform.rotozoom(FwalkL1, 0, scale)
            FwalkL2 = pygame.transform.rotozoom(FwalkL2, 0, scale)
            FwalkL3 = pygame.transform.rotozoom(FwalkL3, 0, scale)
            FwalkL4 = pygame.transform.rotozoom(FwalkL4, 0, scale)
            FwalkL5 = pygame.transform.rotozoom(FwalkL5, 0, scale)
            FwalkL6 = pygame.transform.rotozoom(FwalkL6, 0, scale)
            FwalkL7 = pygame.transform.rotozoom(FwalkL7, 0, scale)
            FwalkL8 = pygame.transform.rotozoom(FwalkL8, 0, scale)

            FidleL = pygame.transform.rotozoom(FidleL, 0, scale)
            FidleR = pygame.transform.rotozoom(FidleR, 0, scale)

            self.walkR = [FwalkR1, FwalkR2, FwalkR3, FwalkR4, FwalkR5, FwalkR6, FwalkR7, FwalkR8]
            self.walkL = [FwalkL1, FwalkL2, FwalkL3, FwalkL4, FwalkL5, FwalkL6, FwalkL7, FwalkL8]
            self.idleL = FidleL
            self.idleR = FidleR


        self.direction = "R"
        self.walk_index = 0

        self.image = self.idleR
        self.rect = self.image.get_rect(midbottom=(80, 400))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.rect.x += 2
            self.direction = "R"
            if self.rect.right >= 1000:
                self.rect.right = 1000

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.rect.x -= 2
            self.direction = "L"
            if self.rect.left <= 0:
                self.rect.x = 0

    def destroy(self):
        self.kill()

    def animation_state(self):
        keys = pygame.key.get_pressed()

        # walking
        if self.gender == "male":
            self.walk_index += 0.1
        elif self.gender == "female":
            self.walk_index += 0.1

        # reset index
        if self.walk_index >= len(self.walkL):
            self.walk_index = 0

        if(self.direction == "R" and (keys[pygame.K_d] or keys[pygame.K_RIGHT])):
            self.image = self.walkR[int(self.walk_index)]

        if(self.direction == "L" and (keys[pygame.K_a] or keys[pygame.K_LEFT])):
            self.image = self.walkL[int(self.walk_index)]

        # idle
        if(self.direction == "R" and not(keys[pygame.K_d] or keys[pygame.K_RIGHT])):
            self.walk_index = 0
            self.image = self.idleR

        if(self.direction == "L" and not(keys[pygame.K_a] or keys[pygame.K_LEFT])):
            self.walk_index = 0
            self.image = self.idleL

    def update(self):
        self.player_input()
        self.animation_state()
