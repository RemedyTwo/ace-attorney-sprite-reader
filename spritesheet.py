from PIL import Image
from subprocess import Popen, PIPE

class Chunk:
    '''Represents piece of spritesheet.'''

    def __init__(self, first_point: tuple, last_point: tuple, position: tuple) -> None:
        self.first_point = first_point
        self.last_point = last_point
        self.position = position
    
    def get_points(self) -> tuple:
        '''Returns the coordinates where the spritesheet should be cropped in a single tuple (x1, y1, x2, y2).'''
        return (self.first_point[0], self.first_point[1], self.last_point[0], self.last_point[1])
    
    def get_image(self, path: str) -> Image:
        image = Image.open(path)
        return image.crop(self.get_points())

    def paste_to_image(self, path: str, image: Image, crop: tuple="") -> Image:
        '''Paste this chunk to the image in argument.'''
        
        spritesheet = Image.open(path)
        chunk = spritesheet.crop(self.get_points())
        if not crop:
            return image.alpha_composite(chunk, self.position)
        else:
            cropped_chunk = chunk.crop(crop)
            new_position = (crop[0], self.position[1] + crop[1])
            return image.alpha_composite(cropped_chunk, new_position)
    
class Sprite:
    '''Represents spritesheet.'''
    
    def __init__(self, path: str, chunks: dict, resolution: tuple) -> None:
        self.path = path
        self.chunks = chunks
        self.resolution = resolution

    def get_chunk_image(self, expressions: tuple) -> Image:
        image = Image.new(mode="RGBA", size=self.resolution)
        for key in expressions:
            if type(key) is tuple:
                self.chunks.get(key[0]).paste_to_image(self.path, image, key[1])
            if type(key) is str:
                self.chunks.get(key).paste_to_image(self.path, image)
            if type(key) is int:
                pass
        return image
    
    def get_chunk_image_sequence(self, *expressions: tuple or list) -> list:
        image_sequence = []
        for expression in expressions:
            image_sequence.append(self.get_chunk_image(expression))
        return image_sequence
    
def save_image_sequence_as_png(image_sequence: tuple, path: str) -> None:
    for index, image in enumerate(image_sequence, start=1):
        if type(image) is Image:
            image.save(path + str(index) + ".png")
    
def save_image_sequence_as_apng(image_sequence: list, path: str) -> None:
    image_sequence[0].save(path + ".apng", save_all=True, append_images=image_sequence[1:], duration=100, loop=0)

def save_video_from_image_sequence(image_sequence: tuple or list, path: str, fps: int):
    filename = path + ".mp4"
    process = Popen(["ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "png", "-r", str(fps), "-i", "-", "-vcodec", "png", "-qscale", "0", filename], stdin=PIPE, stdout=PIPE)
    for image in image_sequence:
        image.save(process.stdin, "PNG")
    process.stdin.close()
    process.wait()