class Marca:
    def __init__(self, nombre) -> None:
        self.__nombre=nombre

    def setNombre(self,nombre) -> None:
        self.__nombre=nombre

    def getNombre(self) -> str:
        return self.__nombre