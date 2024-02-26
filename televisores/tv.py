class TV:
    #propiedades iniciales de cada televisor
    numTV=0

    def __init__(self, marca, estado) -> None:
        self.__marca=marca
        self.__estado=estado
        self.__canal=1
        self.__volumen=1
        self.__precio=500
        TV.numTV+=1

    @classmethod
    def setNumTV(cls, num) -> None:
        cls.numTV=num
    @classmethod
    def getNumTV(cls) -> int:
        return cls.numTV


    def setMarca(self, marca) -> None:
        self.__marca=marca
    def getMarca(self):
        return self.__marca


    def setCanal(self, canal) -> None :
        if  self.__estado == True and canal>=1 and canal<=120:
            self.__canal=canal
    def getCanal(self) -> int:
        return self.__canal
    def canalUp(self) -> None:
        if self.__estado==True and self.__canal>=1 and self.__canal<120:
            self.__canal+=1
    def canalDown(self) -> None:
        if self.__estado==True and self.__canal>1 and self.__canal<=120:
            self.__canal-=1
    

    def setPrecio(self, precio) -> None:
        self.__precio=precio
    def getPrecio(self) -> int:
        return self.__precio


    def setVolumen(self,volumen) -> None:
        if self.__estado==True and volumen>=0 and volumen<=7:
            self.__volumen=volumen
    def getVolumen(self) -> int:
        return self.__volumen
    def volumenUp(self) -> None:
        if self.__estado==True and self.__volumen>=0 and self.__volumen<7:
            self.__volumen+=1
    def volumenDown(self) -> None:
        if self.__estado==True and self.__volumen>0 and self.__volumen<=7:
            self.__volumen-=1
    
    

    def setControl(self, control) -> None:
        self.__control=control
    def getControl(self):
        return self.__control
    
    def turnOn(self) -> None:
        self.__estado=True
    def turnOff(self) -> None:
        self.__estado=False
    def getEstado(self) -> bool:
        return self.__estado

    