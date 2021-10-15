import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, gender):
        super().__init__()
        # image imports
        self.gender = gender

        if self.gender == "male":
            # male
            MwalkR1 = pygame.image.load('graphics/player/male/walkR1.png').convert_alpha()
            MwalkR2 = pygame.image.load('graphics/player/male/walkR2.png').convert_alpha()
            MwalkR3 = pygame.image.load('graphics/player/male/walkR3.png').convert_alpha()
            MwalkR4 = pygame.image.load('graphics/player/male/walkR4.png').convert_alpha()
            MwalkR5 = pygame.image.load('graphics/player/male/walkR5.png').convert_alpha()
            MwalkR6 = pygame.image.load('graphics/player/male/walkR6.png').convert_alpha()
            MwalkR7 = pygame.image.load('graphics/player/male/walkR7.png').convert_alpha()
            MwalkR8 = pygame.image.load('graphics/player/male/walkR8.png').convert_alpha()
            MwalkR9 = pygame.image.load('graphics/player/male/walkR9.png').convert_alpha()
            MwalkR10 = pygame.image.load('graphics/player/male/walkR10.png').convert_alpha()
            MwalkR11 = pygame.image.load('graphics/player/male/walkR11.png').convert_alpha()
            MwalkR12 = pygame.image.load('graphics/player/male/walkR12.png').convert_alpha()
            MwalkR13 = pygame.image.load('graphics/player/male/walkR13.png').convert_alpha()
            MwalkR14 = pygame.image.load('graphics/player/male/walkR14.png').convert_alpha()
            MwalkR15 = pygame.image.load('graphics/player/male/walkR15.png').convert_alpha()

            MwalkL1 = pygame.image.load('graphics/player/male/walkL1.png').convert_alpha()
            MwalkL2 = pygame.image.load('graphics/player/male/walkL2.png').convert_alpha()
            MwalkL3 = pygame.image.load('graphics/player/male/walkL3.png').convert_alpha()
            MwalkL4 = pygame.image.load('graphics/player/male/walkL4.png').convert_alpha()
            MwalkL5 = pygame.image.load('graphics/player/male/walkL5.png').convert_alpha()
            MwalkL6 = pygame.image.load('graphics/player/male/walkL6.png').convert_alpha()
            MwalkL7 = pygame.image.load('graphics/player/male/walkL7.png').convert_alpha()
            MwalkL8 = pygame.image.load('graphics/player/male/walkL8.png').convert_alpha()
            MwalkL9 = pygame.image.load('graphics/player/male/walkL9.png').convert_alpha()
            MwalkL10 = pygame.image.load('graphics/player/male/walkL10.png').convert_alpha()
            MwalkL11 = pygame.image.load('graphics/player/male/walkL11.png').convert_alpha()
            MwalkL12 = pygame.image.load('graphics/player/male/walkL12.png').convert_alpha()
            MwalkL13 = pygame.image.load('graphics/player/male/walkL13.png').convert_alpha()
            MwalkL14 = pygame.image.load('graphics/player/male/walkL14.png').convert_alpha()
            MwalkL15 = pygame.image.load('graphics/player/male/walkL15.png').convert_alpha()

            MidleL = pygame.image.load('graphics/player/male/idleL.png').convert_alpha()
            MidleR = pygame.image.load('graphics/player/male/idleR.png').convert_alpha()

            # crop
            MwalkL1 = MwalkL1.subsurface((310,10,300,500))
            MwalkL2 = MwalkL2.subsurface((310,10,300,500))
            MwalkL3 = MwalkL3.subsurface((310,10,300,500))
            MwalkL4 = MwalkL4.subsurface((310,10,300,500))
            MwalkL5 = MwalkL5.subsurface((310,10,300,500))
            MwalkL6 = MwalkL6.subsurface((310,10,300,500))
            MwalkL7 = MwalkL7.subsurface((310,10,300,500))
            MwalkL8 = MwalkL8.subsurface((310,10,300,500))
            MwalkL9 = MwalkL9.subsurface((310,10,300,500))
            MwalkL10 = MwalkL10.subsurface((310,10,300,500))
            MwalkL11 = MwalkL11.subsurface((310,10,300,500))
            MwalkL12 = MwalkL12.subsurface((310,10,300,500))
            MwalkL13 = MwalkL13.subsurface((310,10,300,500))
            MwalkL14 = MwalkL14.subsurface((310,10,300,500))
            MwalkL15 = MwalkL15.subsurface((310,10,300,500))

            MwalkR1 = MwalkR1.subsurface((1,10,300,500))
            MwalkR2 = MwalkR2.subsurface((1,10,300,500))
            MwalkR3 = MwalkR3.subsurface((1,10,300,500))
            MwalkR4 = MwalkR4.subsurface((1,10,300,500))
            MwalkR5 = MwalkR5.subsurface((1,10,300,500))
            MwalkR6 = MwalkR6.subsurface((1,10,300,500))
            MwalkR7 = MwalkR7.subsurface((1,10,300,500))
            MwalkR8 = MwalkR8.subsurface((1,10,300,500))
            MwalkR9 = MwalkR9.subsurface((1,10,300,500))
            MwalkR10 = MwalkR10.subsurface((1,10,300,500))
            MwalkR11 = MwalkR11.subsurface((1,10,300,500))
            MwalkR12 = MwalkR12.subsurface((1,10,300,500))
            MwalkR13 = MwalkR13.subsurface((1,10,300,500))
            MwalkR14 = MwalkR14.subsurface((1,10,300,500))
            MwalkR15 = MwalkR15.subsurface((1,10,300,500))

            MidleL = MidleL.subsurface((310,10,300,500))
            MidleR = MidleR.subsurface((1,10,300,500))

            # scaling
            scale=0.25

            MwalkR1 = pygame.transform.rotozoom(MwalkR1, 0, scale)
            MwalkR2 = pygame.transform.rotozoom(MwalkR2, 0, scale)
            MwalkR3 = pygame.transform.rotozoom(MwalkR3, 0, scale)
            MwalkR4 = pygame.transform.rotozoom(MwalkR4, 0, scale)
            MwalkR5 = pygame.transform.rotozoom(MwalkR5, 0, scale)
            MwalkR6 = pygame.transform.rotozoom(MwalkR6, 0, scale)
            MwalkR7 = pygame.transform.rotozoom(MwalkR7, 0, scale)
            MwalkR8 = pygame.transform.rotozoom(MwalkR8, 0, scale)
            MwalkR9 = pygame.transform.rotozoom(MwalkR9, 0, scale)
            MwalkR10 = pygame.transform.rotozoom(MwalkR10, 0, scale)
            MwalkR11 = pygame.transform.rotozoom(MwalkR11, 0, scale)
            MwalkR12 = pygame.transform.rotozoom(MwalkR12, 0, scale)
            MwalkR13 = pygame.transform.rotozoom(MwalkR13, 0, scale)
            MwalkR14 = pygame.transform.rotozoom(MwalkR14, 0, scale)
            MwalkR15 = pygame.transform.rotozoom(MwalkR15, 0, scale)


            MwalkL1 = pygame.transform.rotozoom(MwalkL1, 0, scale)
            MwalkL2 = pygame.transform.rotozoom(MwalkL2, 0, scale)
            MwalkL3 = pygame.transform.rotozoom(MwalkL3, 0, scale)
            MwalkL4 = pygame.transform.rotozoom(MwalkL4, 0, scale)
            MwalkL5 = pygame.transform.rotozoom(MwalkL5, 0, scale)
            MwalkL6 = pygame.transform.rotozoom(MwalkL6, 0, scale)
            MwalkL7 = pygame.transform.rotozoom(MwalkL7, 0, scale)
            MwalkL8 = pygame.transform.rotozoom(MwalkL8, 0, scale)
            MwalkL9 = pygame.transform.rotozoom(MwalkL9, 0, scale)
            MwalkL10 = pygame.transform.rotozoom(MwalkL10, 0, scale)
            MwalkL11 = pygame.transform.rotozoom(MwalkL11, 0, scale)
            MwalkL12 = pygame.transform.rotozoom(MwalkL12, 0, scale)
            MwalkL13 = pygame.transform.rotozoom(MwalkL13, 0, scale)
            MwalkL14 = pygame.transform.rotozoom(MwalkL14, 0, scale)
            MwalkL15 = pygame.transform.rotozoom(MwalkL15, 0, scale)

            MidleL = pygame.transform.rotozoom(MidleL, 0, scale)
            MidleR = pygame.transform.rotozoom(MidleR, 0, scale)

            self.walkR = [MwalkR1, MwalkR2, MwalkR3, MwalkR4, MwalkR5, MwalkR6, MwalkR7, MwalkR8, MwalkR9, MwalkR10, MwalkR11, MwalkR12, MwalkR13, MwalkR14, MwalkR15]
            self.walkL = [MwalkL1, MwalkL2, MwalkL3, MwalkL4, MwalkL5, MwalkL6, MwalkL7, MwalkL8, MwalkL9, MwalkL10, MwalkL11, MwalkL12, MwalkL13, MwalkL14, MwalkL15]
            self.idleL = MidleL
            self.idleR = MidleR


        elif self.gender == "female":
            # female
            FwalkR1 = pygame.image.load('graphics/player/female/walkR1.png').convert_alpha()
            FwalkR2 = pygame.image.load('graphics/player/female/walkR2.png').convert_alpha()
            FwalkR3 = pygame.image.load('graphics/player/female/walkR3.png').convert_alpha()
            FwalkR4 = pygame.image.load('graphics/player/female/walkR4.png').convert_alpha()
            FwalkR5 = pygame.image.load('graphics/player/female/walkR5.png').convert_alpha()
            FwalkR6 = pygame.image.load('graphics/player/female/walkR6.png').convert_alpha()
            FwalkR7 = pygame.image.load('graphics/player/female/walkR7.png').convert_alpha()
            FwalkR8 = pygame.image.load('graphics/player/female/walkR8.png').convert_alpha()
            FwalkR9 = pygame.image.load('graphics/player/female/walkR9.png').convert_alpha()
            FwalkR10 = pygame.image.load('graphics/player/female/walkR10.png').convert_alpha()
            FwalkR11 = pygame.image.load('graphics/player/female/walkR11.png').convert_alpha()
            FwalkR12 = pygame.image.load('graphics/player/female/walkR12.png').convert_alpha()
            FwalkR13 = pygame.image.load('graphics/player/female/walkR13.png').convert_alpha()
            FwalkR14 = pygame.image.load('graphics/player/female/walkR14.png').convert_alpha()
            FwalkR15 = pygame.image.load('graphics/player/female/walkR15.png').convert_alpha()
            FwalkR16 = pygame.image.load('graphics/player/female/walkR16.png').convert_alpha()
            FwalkR17 = pygame.image.load('graphics/player/female/walkR17.png').convert_alpha()
            FwalkR18 = pygame.image.load('graphics/player/female/walkR18.png').convert_alpha()
            FwalkR19 = pygame.image.load('graphics/player/female/walkR19.png').convert_alpha()
            FwalkR20 = pygame.image.load('graphics/player/female/walkR20.png').convert_alpha()

            FwalkL1 = pygame.image.load('graphics/player/female/walkL1.png').convert_alpha()
            FwalkL2 = pygame.image.load('graphics/player/female/walkL2.png').convert_alpha()
            FwalkL3 = pygame.image.load('graphics/player/female/walkL3.png').convert_alpha()
            FwalkL4 = pygame.image.load('graphics/player/female/walkL4.png').convert_alpha()
            FwalkL5 = pygame.image.load('graphics/player/female/walkL5.png').convert_alpha()
            FwalkL6 = pygame.image.load('graphics/player/female/walkL6.png').convert_alpha()
            FwalkL7 = pygame.image.load('graphics/player/female/walkL7.png').convert_alpha()
            FwalkL8 = pygame.image.load('graphics/player/female/walkL8.png').convert_alpha()
            FwalkL9 = pygame.image.load('graphics/player/female/walkL9.png').convert_alpha()
            FwalkL10 = pygame.image.load('graphics/player/female/walkL10.png').convert_alpha()
            FwalkL11 = pygame.image.load('graphics/player/female/walkL11.png').convert_alpha()
            FwalkL12 = pygame.image.load('graphics/player/female/walkL12.png').convert_alpha()
            FwalkL13 = pygame.image.load('graphics/player/female/walkL13.png').convert_alpha()
            FwalkL14 = pygame.image.load('graphics/player/female/walkL14.png').convert_alpha()
            FwalkL15 = pygame.image.load('graphics/player/female/walkL15.png').convert_alpha()
            FwalkL16 = pygame.image.load('graphics/player/female/walkL16.png').convert_alpha()
            FwalkL17 = pygame.image.load('graphics/player/female/walkL17.png').convert_alpha()
            FwalkL18 = pygame.image.load('graphics/player/female/walkL18.png').convert_alpha()
            FwalkL19 = pygame.image.load('graphics/player/female/walkL19.png').convert_alpha()
            FwalkL20 = pygame.image.load('graphics/player/female/walkL20.png').convert_alpha()

            FidleL = pygame.image.load('graphics/player/female/idleL.png').convert_alpha()
            FidleR = pygame.image.load('graphics/player/female/idleR.png').convert_alpha()

            scale=0.25

            FwalkR2 = pygame.transform.rotozoom(FwalkR2, 0, scale)
            FwalkR1 = pygame.transform.rotozoom(FwalkR1, 0, scale)
            FwalkR3 = pygame.transform.rotozoom(FwalkR3, 0, scale)
            FwalkR4 = pygame.transform.rotozoom(FwalkR4, 0, scale)
            FwalkR5 = pygame.transform.rotozoom(FwalkR5, 0, scale)
            FwalkR6 = pygame.transform.rotozoom(FwalkR6, 0, scale)
            FwalkR7 = pygame.transform.rotozoom(FwalkR7, 0, scale)
            FwalkR8 = pygame.transform.rotozoom(FwalkR8, 0, scale)
            FwalkR9 = pygame.transform.rotozoom(FwalkR9, 0, scale)
            FwalkR10 = pygame.transform.rotozoom(FwalkR10, 0, scale)
            FwalkR11 = pygame.transform.rotozoom(FwalkR11, 0, scale)
            FwalkR12 = pygame.transform.rotozoom(FwalkR12, 0, scale)
            FwalkR13 = pygame.transform.rotozoom(FwalkR13, 0, scale)
            FwalkR14 = pygame.transform.rotozoom(FwalkR14, 0, scale)
            FwalkR15 = pygame.transform.rotozoom(FwalkR15, 0, scale)
            FwalkR16 = pygame.transform.rotozoom(FwalkR16, 0, scale)
            FwalkR17 = pygame.transform.rotozoom(FwalkR17, 0, scale)
            FwalkR18 = pygame.transform.rotozoom(FwalkR18, 0, scale)
            FwalkR19 = pygame.transform.rotozoom(FwalkR19, 0, scale)
            FwalkR20 = pygame.transform.rotozoom(FwalkR20, 0, scale)

            FwalkL1 = pygame.transform.rotozoom(FwalkL1, 0, scale)
            FwalkL2 = pygame.transform.rotozoom(FwalkL2, 0, scale)
            FwalkL3 = pygame.transform.rotozoom(FwalkL3, 0, scale)
            FwalkL4 = pygame.transform.rotozoom(FwalkL4, 0, scale)
            FwalkL5 = pygame.transform.rotozoom(FwalkL5, 0, scale)
            FwalkL6 = pygame.transform.rotozoom(FwalkL6, 0, scale)
            FwalkL7 = pygame.transform.rotozoom(FwalkL7, 0, scale)
            FwalkL8 = pygame.transform.rotozoom(FwalkL8, 0, scale)
            FwalkL9 = pygame.transform.rotozoom(FwalkL9, 270, scale)
            FwalkL10 = pygame.transform.rotozoom(FwalkL10, 0, scale)
            FwalkL11 = pygame.transform.rotozoom(FwalkL11, 0, scale)
            FwalkL12 = pygame.transform.rotozoom(FwalkL12, 0, scale)
            FwalkL13 = pygame.transform.rotozoom(FwalkL13, 0, scale)
            FwalkL14 = pygame.transform.rotozoom(FwalkL14, 0, scale)
            FwalkL15 = pygame.transform.rotozoom(FwalkL15, 0, scale)
            FwalkL16 = pygame.transform.rotozoom(FwalkL16, 0, scale)
            FwalkL17 = pygame.transform.rotozoom(FwalkL17, 0, scale)
            FwalkL18 = pygame.transform.rotozoom(FwalkL18, 0, scale)
            FwalkL19 = pygame.transform.rotozoom(FwalkL19, 270, scale)
            FwalkL20 = pygame.transform.rotozoom(FwalkL20, 0, scale)

            FidleL = pygame.transform.rotozoom(FidleL, 0, scale)
            FidleR = pygame.transform.rotozoom(FidleR, 0, scale)

            self.walkR = [FwalkR1, FwalkR2, FwalkR3, FwalkR4, FwalkR5, FwalkR6, FwalkR7, FwalkR8, FwalkR9, FwalkR10,
                          FwalkR11, FwalkR12, FwalkR13, FwalkR14, FwalkR15, FwalkR16, FwalkR17, FwalkR18, FwalkR19, FwalkR20]
            self.walkL = [FwalkL1, FwalkL2, FwalkL3, FwalkL4, FwalkL5, FwalkL6, FwalkL7, FwalkL8, FwalkL9, FwalkL10,
                          FwalkL11, FwalkL12, FwalkL13, FwalkL14, FwalkL15, FwalkL16, FwalkL17, FwalkL18, FwalkL19, FwalkL20]
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
            self.walk_index += 0.5
        elif self.gender == "female":
            self.walk_index += 0.6

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
