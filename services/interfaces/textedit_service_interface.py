from PyQt6.QtWidgets import QTextEdit
from abc import ABC, abstractmethod

class TextEditServiceInterface(ABC):

    @abstractmethod
    def resize(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_window(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_space(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_font_metrics(self: QTextEdit) -> None:
        pass