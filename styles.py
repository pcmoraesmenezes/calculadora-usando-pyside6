#  https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html

import qdarktheme
from enviroments import PRIMARY_COLOR
from enviroments import DARKER_PRIMARY_COLOR
from enviroments import DARKEST_PRIMARY_COLOR


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',  # definindo o tema
        corner_shape='rounded',  # deixa as caixas com formato redondo
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}"
            },
        },
        additional_qss=qss
    )
