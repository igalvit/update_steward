from abc import ABC, abstractclassmethod


class Updater(ABC):

    @abstractclassmethod
    def update_system(self):
        pass

    @abstractclassmethod
    def needs_restart(self):
        pass
