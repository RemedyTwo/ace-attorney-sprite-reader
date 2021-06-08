from PIL import Image
        
class Chunk:
    def __init__(self, first_point: tuple, last_point: tuple, position: tuple) -> None:
        self.first_point = first_point
        self.last_point = last_point
        self.position = position
    
    def get_points(self) -> tuple:
        return (self.first_point[0], self.first_point[1], self.last_point[0], self.last_point[1])
    
    def get_image(self, path: str) -> Image:
        image = Image.open(path)
        return image.crop(self.get_points())

    def paste_chunk_to_image(self, path: str, image: Image, crop: tuple="") -> Image:
        spritesheet = Image.open(path)
        chunk = spritesheet.crop(self.get_points())
        if not crop:
            return image.alpha_composite(chunk, self.position)
        else:
            cropped_chunk = chunk.crop(crop)
            new_position = (crop[0], self.position[1] + crop[1])
            return image.alpha_composite(cropped_chunk, new_position)
    
class Sprite:
    def __init__(self, path: str, chunks: dict, resolution: tuple) -> None:
        self.path = path
        self.chunks = chunks
        self.resolution = resolution

    def get_chunk_image(self, expressions: tuple) -> Image:
        image = Image.new(mode="RGBA", size=self.resolution)
        for key in expressions:
            if type(key) is tuple:
                self.chunks.get(key[0]).paste_chunk_to_image(self.path, image, key[1])
            if type(key) is str:
                self.chunks.get(key).paste_chunk_to_image(self.path, image)
        return image