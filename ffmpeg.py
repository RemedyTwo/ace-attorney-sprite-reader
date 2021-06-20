from subprocess import Popen, PIPE
from typing import Tuple

path = "tools\\ffmpeg.exe"

def save_video_from_image_sequence(image_sequence: Tuple[str, ...] or list, path: str = "tmp\\Untitled", fps: int = 60):
    filename = path + ".mp4"
    process = Popen(["ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "png", "-r", str(fps), "-i", "-", "-vcodec", "png", "-qscale", "0", filename], stdin=PIPE, stdout=PIPE)
    for image in image_sequence:
        image.save(process.stdin, "PNG")
    process.stdin.close()
    process.wait()