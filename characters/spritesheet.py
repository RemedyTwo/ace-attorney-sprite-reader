from typing import List, Tuple
from PIL import Image
from subprocess import Popen, PIPE

class Chunk:
    '''Represents piece of spritesheet.'''

    def __init__(self, first_point: tuple[int, int], last_point: tuple[int, int], position: tuple[int, int]) -> None:
        self.first_point = first_point
        self.last_point = last_point
        self.position = position
    
    def get_image(self, path: str) -> Image:
        '''Returns the Image from the Chunk.'''

        image = Image.open(path)
        return image.crop(self.get_points())

    def get_points(self) -> tuple:
        '''Returns the coordinates where the spritesheet should be cropped in a single tuple (x1, y1, x2, y2).'''

        return (self.first_point[0], self.first_point[1], self.last_point[0], self.last_point[1])

    def paste_to_image(self, path: str, image: Image, crop: tuple = None) -> Image:
        '''Paste this chunk to the image in argument.'''
        
        chunk = self.get_image(path)
        if not crop:
            return image.alpha_composite(chunk, self.position)
        else:
            cropped_chunk = chunk.crop(crop)
            new_position = (crop[0], self.position[1] + crop[1])
            return image.alpha_composite(cropped_chunk, new_position)
    
class Sprite:
    '''Represents spritesheet.'''
    
    def __init__(self, path: str, chunks: dict, resolution: tuple[int, int], x_offset: int = 0, y_offset: int = 0) -> None:
        self.path = path
        self.chunks = chunks
        self.resolution = resolution
        self.x_offset = x_offset
        self.y_offset = y_offset

    def get_chunk_image(self, expressions: Tuple[str, ...]) -> Image:
        '''Get image from chunks.'''

        image = Image.new(mode="RGBA", size=self.resolution)
        for key in expressions:
            if type(key) is tuple:
                self.chunks.get(key[0]).paste_to_image(self.path, image, key[1])
            if type(key) is str:
                self.chunks.get(key).paste_to_image(self.path, image)
            if type(key) is int:
                pass
        return image
    
    def get_image_sequence_dict(self, image_sequence: List[str]) -> dict:
        '''Get dictionnary of Image from list of expressions to avoid repetitions.'''

        dict = {}
        for image in image_sequence:
            if not dict.get(image):
                dict[image] = self.get_chunk_image(image)
        return dict
    
    def get_image_sequence(self, image_sequence: list[str] or Tuple[str, ...]) -> list:
        '''Get list of Image from list of expressions.'''

        dict = self.get_image_sequence_dict(image_sequence)
        for i in range(len(image_sequence)):
            image_sequence[i] = dict.get(tuple(image_sequence[i]))
        return image_sequence

    
def save_image_sequence_as_png(image_sequence: Tuple[str, ...], path: str) -> None:
    for index, image in enumerate(image_sequence, start=1):
        if type(image) is Image:
            image.save(path + str(index) + ".png")
    
def save_image_sequence_as_apng(image_sequence: list, path: str) -> None:
    image_sequence[0].save(path + ".apng", save_all=True, append_images=image_sequence[1:], duration=100, loop=0)

def save_video_from_image_sequence(image_sequence: Tuple[str, ...] or list, path: str = "tmp\\Untitled", fps: int = 60) -> None:
    filename = path + ".mp4"
    process = Popen(["ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "png", "-r", str(fps), "-i", "-", "-vcodec", "png", "-qscale", "0", filename], stdin=PIPE, stdout=PIPE)
    for image in image_sequence:
        image.save(process.stdin, "PNG")
    process.stdin.close()
    process.wait()