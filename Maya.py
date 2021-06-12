from PIL.Image import NONE
from spritesheet import *

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

happy = Sprite(
    path=paths.get("Happy"),
    chunks={
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
    resolution=(626, 1077)
)

yes_anim = happy.get_chunk_image_sequence(
    ("main", "sleeve", "bottom") * 10,
    ("main", "sleeve", "bottom", "eyes1", "mouth1") * 6, # 6 frames
    ("main", "sleeve", "bottom", "excited") * 27, # 27 frames
    (("main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "sleeve", "bottom", "anim1") * 4, # 4 frames
    (("main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "sleeve", "bottom", "anim2") * 8, # 8 frames
    (("main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "sleeve", "bottom", "anim1") * 4,
    ("main", "sleeve", "bottom", "excited") * 10
)

def get_yes_speaking(length: int) -> list:
    image_sequence = []
    mouth_counter = 0
    eye_counter = 0

    for i in range(0, length):
        current_frame = ["main", "sleeve", "bottom"]
        if mouth_counter < 8:
            pass
        elif mouth_counter < 17:
            current_frame.append("mouth1")
        elif mouth_counter < 26:
            current_frame.append("mouth2")
        elif mouth_counter < 35:
            current_frame.append("mouth1")

        if eye_counter < 72:
            pass
        elif eye_counter < 78:
            current_frame.append("eyes1")
        elif eye_counter < 84:
            current_frame.append("eyes2")
        elif eye_counter < 90:
            current_frame.append("eyes1")

        mouth_counter += 1
        if mouth_counter > 35:
            mouth_counter = 0
        eye_counter += 1
        if eye_counter > 90:
            eye_counter = 0
        
        image_sequence.append(happy.get_chunk_image(current_frame))
        print("Image " + str(i) + " prête.")
    return image_sequence


save_video_from_image_sequence(get_yes_speaking(60*30), "tmp\\tmp", 60)