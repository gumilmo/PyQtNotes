from abc import ABC, abstractmethod


class MainServiceInterface(ABC):

    @abstractmethod
    def delete_widget(self):
        pass

    @abstractmethod
    def move_widget(self):
        pass

    @abstractmethod
    def create_new_window(self):
        pass
