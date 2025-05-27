import os, sys
from PIL import Image, ImageTk

def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "assets", relative_path)

def img(path_in_assets: str) -> ImageTk.PhotoImage:
    ip = resource_path(path_in_assets)
    return ImageTk.PhotoImage(Image.open(ip))
