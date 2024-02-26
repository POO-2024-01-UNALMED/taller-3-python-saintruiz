class Control:
    def enlazar(self, tv) -> None:
        self.__tv=tv
        tv.setControl(self)

    def setTv(self, tv) -> None:
        self.enlazar(tv)
    def getTv(self):
        return self.__tv
    
    
    def turnOn(self) -> None:
        self.__tv.turnOn()
    def turnOff(self) -> None:
        self.__tv.turnOff()
    
    def canalUp(self) -> None:
        self.__tv.canalUp()
    def canalDown(self) -> None:
        self.__tv.canalDown()

    def volumenUp(self) -> None:
        self.__tv.volumenUp()
    def volumenDown(self) -> None:
        self.__tv.volumenDown()

    def setCanal(self, int) -> None:
        self.__tv.setCanal(int)
    def setVolumen(self, int) -> None:
        self.__tv.setVolumen(int)