from PySide6.QtWidgets import QApplication
from display import Display
from info import Info

# from PySide6.QtWidgets import QVBoxLayout
from main_window import MainWindow
import sys
from styles import setupTheme
from buttons import ButtonsGrid


if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone da aplicação
    window.set_icon_app()

    # info
    info = Info("")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText('Digite algo')  # Apaga esse conteudo quando
    # o usuario digita algo
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)
    # Button

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
