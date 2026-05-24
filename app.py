from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget, 
    QPushButton, 
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout
)
import sys
import asyncio
from qasync import QEventLoop, asyncSlot
from controllers import (
    turn_off,
    turn_on,
    disconnect_plug
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This is my Application")

        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(2000, 2000))
        self.resize(QSize(1000, 1000))


        container = QWidget()
        self.setCentralWidget(container)
        layout = QHBoxLayout()
        container.setLayout(layout)

        self.on_button = QPushButton("Turn ON")
        self.on_button.setObjectName("on_button")
        self.on_button.clicked.connect(self.turn_on_plug)
        self.on_button.setFixedSize(QSize(200, 200))
        
        self.off_button = QPushButton("Turn OFF")
        self.off_button.setObjectName("off_button")
        self.off_button.clicked.connect(self.turn_off_plug)
        self.off_button.setFixedSize(QSize(200, 200))

        layout.addWidget(self.on_button)
        layout.addWidget(self.off_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(30)



    @asyncSlot()
    async def turn_on_plug(self):
        await turn_on()
    @asyncSlot()
    async def turn_off_plug(self):
        await turn_off()

    async def cleanup(self):
        await disconnect_plug()

app = QApplication(sys.argv)
with open("style/main.qss", "r") as file:
    app.setStyleSheet(file.read())

loop = QEventLoop(app)
asyncio.set_event_loop(loop)

window = MainWindow()
window.show()

async def app_close_event():
    await window.cleanup()


app.aboutToQuit.connect(
    lambda: asyncio.create_task(app_close_event())
)

with loop:
    loop.run_forever()
