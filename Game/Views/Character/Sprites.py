from array import array
from Views.Character.SpriteSheet import SpriteSheet
from Views.Character.eSprites import eSprites
from pygame import Surface

class CharacterSprite():
    BLACK = (0, 0, 0)

    def __init__(self,path:str) -> None:
        self.sprite_sheet = SpriteSheet(path)
        self.counter_step = 0
        # Idle crop images
        self.IDLE_UP = self.sprite_sheet.image_at((6,3,18,33), CharacterSprite.BLACK) 
        self.IDLE_DOWN = self.sprite_sheet.image_at((5,35,19,33), CharacterSprite.BLACK)
        self.IDLE_LEFT = self.sprite_sheet.image_at((4,68,19,32), CharacterSprite.BLACK)
        self.IDLE_RIGHT = self.sprite_sheet.image_at((7,100,18,32), CharacterSprite.BLACK)

         # Move 1 crop images
        self.MOVE_STEP_1_UP = self.sprite_sheet.image_at((38,2,18,33), CharacterSprite.BLACK) 
        self.MOVE_STEP_1_DOWN = self.sprite_sheet.image_at((37,35,19,33), CharacterSprite.BLACK)
        self.MOVE_STEP_1_LEFT = self.sprite_sheet.image_at((36,68,19,32), CharacterSprite.BLACK)
        self.MOVE_STEP_1_RIGHT = self.sprite_sheet.image_at((39,100,18,32), CharacterSprite.BLACK)

         # Move 2 crop images
        self.MOVE_STEP_0_UP = self.sprite_sheet.image_at((70,2,18,33), CharacterSprite.BLACK) 
        self.MOVE_STEP_0_DOWN = self.sprite_sheet.image_at((69,35,19,33), CharacterSprite.BLACK)
        self.MOVE_STEP_0_LEFT = self.sprite_sheet.image_at((68,68,19,32), CharacterSprite.BLACK)
        self.MOVE_STEP_0_RIGHT = self.sprite_sheet.image_at((71,100,18,32), CharacterSprite.BLACK)

        self.MOVE_UP = [[self.MOVE_STEP_1_UP,self.IDLE_UP],[self.MOVE_STEP_0_UP,self.IDLE_UP]]
        self.MOVE_DOWN = [[self.MOVE_STEP_1_DOWN,self.IDLE_DOWN],[self.MOVE_STEP_0_DOWN,self.IDLE_DOWN]]
        self.MOVE_LEFT = [[self.MOVE_STEP_1_LEFT,self.IDLE_LEFT],[self.MOVE_STEP_0_LEFT,self.IDLE_LEFT]]
        self.MOVE_RIGHT = [[self.MOVE_STEP_1_RIGHT,self.IDLE_RIGHT],[self.MOVE_STEP_0_RIGHT,self.IDLE_RIGHT]]
        pass

    def get_move(self,position:eSprites) -> array:
        self.counter_step = (self.counter_step + 1) % 2
        if(position == eSprites.UP):
            return self.MOVE_UP[self.counter_step]
        elif(position == eSprites.DOWN):
            return self.MOVE_DOWN[self.counter_step]
        elif(position == eSprites.LEFT):
            return self.MOVE_LEFT[self.counter_step]
        elif(position == eSprites.RIGHT):
            return self.MOVE_RIGHT[self.counter_step]
        else:
            return None
