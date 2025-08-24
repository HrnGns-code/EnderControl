from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit
import time
class GCodeTab(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        layout = QVBoxLayout()
        self.log = QTextEdit(); self.log.setReadOnly(True)
        self.btn = QPushButton("G-code Dosyası Seç ve Yazdır")
        self.btn.clicked.connect(self.send_file)
        layout.addWidget(self.btn)
        layout.addWidget(self.log)
        self.setLayout(layout)
    def send_file(self):
        path, _ = QFileDialog.getOpenFileName(filter="G-code (*.gcode)")
        if not path: return
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith(";"):
                    self.conn.send(line)
                    self.log.append(f"> {line}")
                    time.sleep(0.1)  # Yazıcıya boğmadan gönder
