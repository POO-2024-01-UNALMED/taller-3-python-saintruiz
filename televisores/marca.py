class Marca:
    def __init__(self, nombre) -> None:
        self.__nombre=nombre

    def set(self,nombre) -> None:
        self.__nombre=nombre

    def get(self) -> str:
        return self.__nombre