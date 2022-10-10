from array import array
from Views.Character.SpriteSheet import SpriteSheet
from Views.Character.eSprites import eSprites
from pygame import Surface

class CharacterSprite():
    BLACK = (0, 0, 0)

    def __init__(self,path:str) -> None:
        self.sprite_sheet = SpriteSheet(path)
        # Idle crop images
        self.IDLE_UP = self.sprite_sheet.image_at((6,3,18,33), CharacterSprite.BLACK) 
        self.IDLE_DOWN = self.sprite_sheet.image_at((5,35,19,33), CharacterSprite.BLACK)
        self.IDLE_LEFT = self.sprite_sheet.image_at((4,68,19,32), CharacterSprite.BLACK)
        self.IDLE_RIGHT = self.sprite_sheet.image_at((7,100,18,32), CharacterSprite.BLACK)
        # Up crop images
        self.MOVE_UP = [self.sprite_sheet.image_at((38,2,18,33), CharacterSprite.BLACK),self.sprite_sheet.image_at((70,2,18,33), CharacterSprite.BLACK)]
        # Down crop images
        self.MOVE_DOWN = [self.sprite_sheet.image_at((37,35,19,33), CharacterSprite.BLACK),self.sprite_sheet.image_at((69,35,19,33), CharacterSprite.BLACK)]
        # Left crop images
        self.MOVE_LEFT = [self.sprite_sheet.image_at((36,68,19,32), CharacterSprite.BLACK),self.sprite_sheet.image_at((68,68,19,32), CharacterSprite.BLACK)]
        # Right crop images
        self.MOVE_RIGHT = [self.sprite_sheet.image_at((39,100,18,32), CharacterSprite.BLACK),self.sprite_sheet.image_at((71,100,18,32), CharacterSprite.BLACK)]
        pass

    def get_idle(self,position:eSprites) -> Surface:
        if(position == eSprites.UP):
            return self.IDLE_UP
        elif(position == eSprites.DOWN):
            return self.IDLE_DOWN
        elif(position == eSprites.LEFT):
            return self.IDLE_LEFT
        elif(position == eSprites.RIGHT):
            return self.IDLE_RIGHT
        else:
            return None

    def get_move(self,position:eSprites) -> array:
        if(position == eSprites.UP):
            return self.MOVE_UP
        elif(position == eSprites.DOWN):
            return self.MOVE_DOWN
        elif(position == eSprites.LEFT):
            return self.MOVE_LEFT
        elif(position == eSprites.RIGHT):
            return self.MOVE_RIGHT
        else:
            return None
