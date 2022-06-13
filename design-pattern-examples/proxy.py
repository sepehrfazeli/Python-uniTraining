import io
import time

from PIL import Image as PILImage
from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def show(self):
        pass


class RealImage(Image):
    _IMAGE_PATH = "resources/programmer-meme.jpg"

    def __init__(self):
        img_bytes = self._load_image()
        self._image = PILImage.open(io.BytesIO(img_bytes))

    def _load_image(self):
        with open(self._IMAGE_PATH, "rb") as img:
            return bytearray(img.read())

    def show(self):
        self._image.show()


class ProxyImage(Image):
    def __init__(self):
        self._real_image = None

    def show(self):
        if self._real_image is None:
            self._real_image = RealImage()
        self._real_image.show()


# instantiate objects
proxy_image = ProxyImage()
real_image = RealImage()

proxy_image.show()
time.sleep(1)