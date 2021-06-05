from PIL import Image
        
class Chunk:
    def __init__(self, first_point: tuple, last_point: tuple, position: tuple) -> None:
        self.first_point = first_point
        self.last_point = last_point
        self.position = position
        self.path = ""
    
    def get_image(self) -> Image:
        return Image.open(self.path).crop((self.first_point[0], self.first_point[1], self.last_point[0], self.last_point[1]))

class Sprite:
    def __init__(self, path: str, chunks: tuple) -> None:
        self.path = path
        self.chunks = chunks
        for chunk in chunks:
            chunk.path = path

    def get_chunk(self, index: int) -> Chunk:
        return self.chunks[index]



if __name__ == '__main__':
    paths = {
        "Pensive": "assets\\graphics\\gs1\\animation\\characters\\pl0100.png",
        "Sad": "assets\\graphics\\gs1\\animation\\characters\\pl0100.png",
        "Malicious": "assets\\graphics\\gs1\\animation\\characters\\pl0100.png",
        "Surprised": "assets\\graphics\\gs1\\animation\\characters\\pl0100.png",
        "Idle": "assets\\graphics\\gs1\\animation\\characters\\pl0101.png",
        "Shocked": "assets\\graphics\\gs1\\animation\\characters\\pl0101.png",
        "Depressed": "assets\\graphics\\gs1\\animation\\characters\\pl0102.png",
        "Angry": "assets\\graphics\\gs1\\animation\\characters\\pl0102.png",
        "Worried": "assets\\graphics\\gs1\\animation\\characters\\pl0102.png",
        "Crying": "assets\\graphics\\gs1\\animation\\characters\\pl0102.png",
        "Motivated": "assets\\graphics\\gs1\\animation\\characters\\pl0102.png",
        "Happy": "assets\\graphics\\gs1\\animation\\characters\\pl0103.png",
        "Assistant Idle": "assets\\graphics\\gs1\\animation\\characters\\pl0104.png",
        "Assistant Angry": "assets\\graphics\\gs1\\animation\\characters\\pl0104.png",
        "Assistant Exasperated": "assets\\graphics\\gs1\\animation\\characters\\pl0104.png",
        "Assistant Fighting": "assets\\graphics\\gs1\\animation\\characters\\pl0104.png",
        "Assistant Thinking": "assets\\graphics\\gs1\\animation\\characters\\pl0104.png",
        "Maid Idle": "assets\\graphics\\gs3\\animation\\characters\\pl2900.png",
        "Maid Happy": "assets\\graphics\\gs3\\animation\\characters\\pl2900.png",
        "Maid Shocked": "assets\\graphics\\gs3\\animation\\characters\\pl2900.png"
    }
    happy_main = Chunk((35, 26), (660, 971), (0, 23))
    happy_anim1 = Chunk((756, 3), (1187, 755), (127, 0))
    happy_sleeve = Chunk((1188, 702), (1121, 745), (559, 969))
    happy_bottom = Chunk((720, 756), (1241, 863), (39, 969))
    happy_anim2 = Chunk((1242, 13), (1673, 809), (127, 10))
    happy_eyes1 = Chunk((54, 972), (269, 1025), (235, 246))
    happy_eyes2 = Chunk((54, 1026), (269, 1079), (235, 246))
    happy_mouth1 = Chunk((54, 1080), (269, 1187), (235, 327))
    happy_excited = Chunk((270, 972), (485, 1187), (235, 213))
    happy_mouth2 = Chunk((108, 1188), (215, 1295), (289, 321))

    happy = Sprite(
        path=paths.get("Happy"), 
        chunks=(
            happy_main,
            happy_anim1,
            happy_sleeve,
            happy_bottom,
            happy_anim2,
            happy_eyes1,
            happy_eyes2,
            happy_mouth1,
            happy_excited,
            happy_mouth2
        )
    )
    
    image = Image.new(mode="RGBA", size=(626, 1077))

    sprite = happy.get_chunk(1).get_image()
    image.paste(sprite, happy.get_chunk(1).position, sprite)
    image.show()
