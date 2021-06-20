from src.paths import *
from src.characters.spritesheet import *

# pensive = Sprite(
#     path = characters.get("Maya").get("Pensive"),
#     chunks = {
#         "main": Chunk
#     }
# )

happy = Sprite(
    path = characters.get("Maya").get("Happy"),
    chunks = {
        "main": Chunk((35, 26), (35 + 626, 26 + 946), (0, 23)), # pixel haut gauche inclus, pixel bas droite exclus, position haut gauche inclus
        "anim1": Chunk((756, 3), (756 + 432, 3 + 753), (127, 0)),
        "sleeve": Chunk((1188, 702), (1188 + 38, 702 + 44), (559, 969)),
        "bottom": Chunk((720, 756), (720 + 522, 756 + 108), (37, 969)),
        "anim2": Chunk((1242, 13), (1242 + 432, 13 + 797), (127, 10)),
        "eyes1": Chunk((54, 972), (54 + 216, 972 + 54), (235, 246)),
        "eyes2": Chunk((54, 1026), (54 + 216, 1026 + 54), (235, 246)),
        "mouth1": Chunk((54, 1080), (54 + 216, 1080 + 108), (235, 327)),
        "excited": Chunk((270, 972), (270 + 216, 972 + 216), (235, 213)),
        "mouth2": Chunk((108, 1188), (108 + 108, 1188 + 108), (289, 321))
    },
    resolution = (626, 1077),
    x_offset = 0,
    y_offset = 108
)

def get(length: int = 0, framerate: int = 60, *expression):
    dict = {
        "yes": {
            "idle": (happy, get_yes_idle(length, framerate)),
            "speaking": (happy, get_yes_speaking(length, framerate)),
            "anim": (happy, get_yes_anim(framerate))
        }   
    }
    for element in expression:
        for key in element:
            dict = dict.get(key)
    return dict

def get_yes_anim(framerate: int = 60) -> list[str]:
    image_sequence = []
    ratio = framerate // 60
    for _ in range(10 * ratio):
        image_sequence.append(("main", "sleeve", "bottom"))
    for _ in range(6 * ratio):
        image_sequence.append(("main", "sleeve", "bottom", "eyes1", "mouth1"))
    for _ in range(27 * ratio):
        image_sequence.append(("main", "sleeve", "bottom", "excited"))
    for _ in range(4 * ratio):
        image_sequence.append((("main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "sleeve", "bottom", "anim1"))
    for _ in range(8 * ratio):
        image_sequence.append((("main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "sleeve", "bottom", "anim2"))
    for _ in range(4 * ratio):
        image_sequence.append((("main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "sleeve", "bottom", "anim1"))
    for _ in range(10 * ratio):
        image_sequence.append(("main", "sleeve", "bottom", "excited"))
    return image_sequence

def get_yes(length: int, eyes: bool = True, mouth: bool = False, framerate: int = 60) -> list[str]:
    image_sequence = []
    mouth_counter = 0
    eye_counter = 0
    ratio = framerate // 60
    for i in range(length):
        current_frame = ["main", "sleeve", "bottom"]
        if mouth:
            if mouth_counter < 8 * ratio:
                pass
            elif mouth_counter < 17 * ratio:
                current_frame.append("mouth1")
            elif mouth_counter < 26 * ratio:
                current_frame.append("mouth2")
            elif mouth_counter < 35 * ratio:
                current_frame.append("mouth1")
            mouth_counter += 1
            if mouth_counter > 35 * ratio:
                mouth_counter = 0
        if eyes:
            if eye_counter < 72 * ratio:
                pass
            elif eye_counter < 78 * ratio:
                current_frame.append("eyes1")
            elif eye_counter < 84 * ratio:
                current_frame.append("eyes2")
            elif eye_counter < 90 * ratio:
                current_frame.append("eyes1")
            eye_counter += 1
            if eye_counter > 90 * ratio:
                eye_counter = 0
        image_sequence.append(tuple(current_frame)) # turning into tuple so they can be used as key later
    return image_sequence

def get_yes_idle(length: int, framerate: int = 60) -> list[str]:
    return get_yes(length, eyes=True, mouth=False)

def get_yes_speaking(length: int, framerate: int = 60) -> list[str]:
    return get_yes(length, eyes=True, mouth=True)