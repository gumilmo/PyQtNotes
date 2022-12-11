from PyQt6.QtWidgets import QTextEdit
from abc import ABC, abstractmethod

class TextEditServiceInterface(ABC):

    @abstractmethod
    def resize_main(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_window(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_space(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_backspace(self: QTextEdit) -> None:
        pass

    @abstractmethod
    def resize_by_font_metrics(self: QTextEdit) -> None:
        pass
    
    @abstractmethod
    def call_text_edit_context_menu(self) -> None:
        pass

    @abstractmethod
    def change_text_font_size(self) -> None:
        pass

    @abstractmethod
    def change_text_font_color(self) -> None:
        pass

    @abstractmethod
    def change_text_font_weight(self) -> None:
        pass

    @abstractmethod
    def change_text_font_italic(self) -> None:
        pass

    @abstractmethod
    def image_resize(self) -> None:
        pass