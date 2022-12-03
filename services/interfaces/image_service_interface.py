from abc import ABC, abstractmethod

class ImageServiceInterface(ABC):

    @staticmethod
    def resize_image() -> None:
        pass

    @staticmethod
    def add_image_by_clipboard() -> None:
        pass

    @staticmethod
    def add_image_by_drog_n_drop() -> None:
        pass