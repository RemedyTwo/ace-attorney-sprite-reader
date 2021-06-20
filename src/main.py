from src.scene import Element, Scene
from src.characters import Maya

first = Element(
    background = "Kurain Village", 
    character = Maya, 
    expression = ("yes", "anim"), 
    length = 60, 
    effect = None
)
scene = Scene(first)

scene.export_to_video("tmp\\tmp", 60)