from PySide6.QtWidgets import QLineEdit
from enviroments import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utility import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # Usa uma list compreenshion para dar um espaço extra no canto direito
        # Ao invés de ele pegar um text_margin e passar quatro vezes, pois sãõ
        # 4 parametros, faz-se uso de um for para aplicar os quatro parametros
        # unicamente
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        # ALinha o texto a direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()  # remove os espaços vazios no inicio e fim
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]
        isOperator = key in [KEYS.Key_Play, KEYS.Key_Minus, KEYS.Key_Asterisk,
                             KEYS.Key_Slash]

        if isEnter or text == '=':
            self.eqPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)
        if isDelete or text == '◀':
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()

        if isOperator:
            self.operatorPressed.emit(text)
            return event.ignore()
