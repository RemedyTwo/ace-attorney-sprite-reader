from characters import *

class Maya:
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
            "happy_main": Chunk((35, 26), (35 + 626, 26 + 946), (0, 23)), # pixel haut gauche inclus, pixel bas droite exclus, position haut gauche inclus
            "happy_anim1": Chunk((756, 3), (756 + 432, 3 + 753), (127, 0)),
            "happy_sleeve": Chunk((1188, 702), (1188 + 38, 702 + 44), (559, 969)),
            "happy_bottom": Chunk((720, 756), (720 + 522, 756 + 108), (37, 969)),
            "happy_anim2": Chunk((1242, 13), (1242 + 432, 13 + 797), (127, 10)),
            "happy_eyes1": Chunk((54, 972), (54 + 216, 972 + 54), (235, 246)),
            "happy_eyes2": Chunk((54, 1026), (54 + 216, 1026 + 54), (235, 246)),
            "happy_mouth1": Chunk((54, 1080), (54 + 216, 1080 + 108), (235, 327)),
            "happy_excited": Chunk((270, 972), (270 + 216, 972 + 216), (235, 213)),
            "happy_mouth2": Chunk((108, 1188), (108 + 108, 1188 + 108), (289, 321))
        },
        resolution=(626, 1077)
    )

    image1 = happy.get_chunk_image(expressions=("happy_main", "happy_sleeve", "happy_bottom"))
    image2 = happy.get_chunk_image(expressions=(("happy_main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "happy_sleeve", "happy_bottom", "happy_anim1"))
    image3 = happy.get_chunk_image(expressions=(("happy_main", (0, 490 - 23, 0 + 626, 490 + 479 - 23)), "happy_sleeve", "happy_bottom", "happy_anim2"))

    sequence = (image1, image2, image3)
    for index, image in enumerate(sequence, start=1):
        image.save("tmp\\happy" + str(index) + ".png")
    image1.save("tmp\\tmp.apng", save_all=True, append_images=[image2, image3, image2], duration=100, loop=0)