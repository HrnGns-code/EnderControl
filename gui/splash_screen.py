from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont
class SplashScreen(QWidget):
    finished = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.finish_delay = 2000
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(400, 300)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pix = QLabel()
        pix.setPixmap(QPixmap("assets/icon.png").scaled(100,100))
        layout.addWidget(pix)
        lbl1 = QLabel("EnderKontrol")
        lbl1.setFont(QFont("Arial", 24))
        layout.addWidget(lbl1)
        lbl2 = QLabel("Creality Ender‑3 V3 SE için gelişmiş kontrol arayüzü")
        lbl2.setFont(QFont("Arial", 10))
        layout.addWidget(lbl2)
        lbl3 = QLabel("Uygulama başlatılıyor...")
        lbl3.setFont(QFont("Arial", 12))
        layout.addWidget(lbl3)
        self.setLayout(layout)
        QTimer.singleShot(self.finish_delay, self.on_finish)
    def on_finish(self):
        self.finished.emit()
        self.close()
