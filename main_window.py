from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtGui import QIcon
from enviroments import WINDOW_ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #  Configuração básica
        self.widgetCentral = QWidget()
        self.vLayout = QVBoxLayout()
        self.widgetCentral.setLayout(self.vLayout)
        self.setCentralWidget(self.widgetCentral)

        #  Adicionando título
        self.setWindowTitle("Calculadora")

        #  Define o ícone da aplicação

    def set_icon_app(self):
        icon = QIcon(str(WINDOW_ICON_PATH))
        # Os dois jeitos funcionam!
        self.setWindowIcon(icon)
        # app.setWindowIcon(icon)

        #  Ultima coisa a ser feita

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())  # Evita que o úsuario
        # possa maximizar a tela

    def addWidgetToVLayout(self, widget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
