import characters
import ffmpeg
from characters import spritesheet
from paths import *
from PIL import Image

class Element:
    def __init__(self, background: str=None, character=type, expression: tuple or list or str=None, length: int=None, effect: str=None):
        self.background = backgrounds.get(background)
        self.character = character
        self.expression = character.get(length, expression)
        self.effect = effect

class Scene:
    def __init__(self, *elements: Element) -> None:
        self.elements = elements
    
    def get_image_sequence(self):
        image_sequence = []
        last_background = ""
        for element in self.elements:
            if element.background != None:
                last_background = element.background
            background = last_background
            for frame in element.expression[1]:
                tmp = [background, frame]
                image_sequence.append(tuple(tmp))
        dict = self.get_image_sequence_dict(element.expression[0], image_sequence)
        for i in range(len(image_sequence)):
            image_sequence[i] = dict.get(tuple(image_sequence[i]))
        return image_sequence

    def get_image_sequence_dict(self, sprite: spritesheet.Sprite, image_sequence: list or tuple):
        dict = {}
        for image in image_sequence:
            if not dict.get(image):
                expression = image[-1]
                character_sprite = sprite.get_chunk_image(expression)
                background = Image.open(image[0])
                coordinates_center = get_top_left_coordinates_to_center(background.size, sprite.resolution, sprite)
                background.alpha_composite(character_sprite, coordinates_center)
                dict[image] = background
        return dict

    def export_to_video(self, path: str = "Untitled", fps: int = 60):
        '''Exports scene to video.'''
        image_sequence = self.get_image_sequence()
        ffmpeg.save_video_from_image_sequence(image_sequence, path, fps)

def get_top_left_coordinates_to_center(background_resolution: tuple[int, int], foreground_resolution: tuple[int, int], sprite: spritesheet.Sprite = None) -> tuple[int, int]:
    '''Get upper left coordinates in order to center an image into another.'''

    x = ((background_resolution[0]//2)-(foreground_resolution[0]//2)) + sprite.x_offset
    y = (background_resolution[1] - foreground_resolution[1]) + sprite.y_offset
    return (x, y)