from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QHBoxLayout
class TemperatureTab(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        layout = QVBoxLayout()
        self.nozzle = QSpinBox(); self.nozzle.setRange(0, 300)
        self.bed = QSpinBox(); self.bed.setRange(0, 120)
        btn_n = QPushButton("Nozzle Ayarla")
        btn_b = QPushButton("Yatak Ayarla")
        btn_n.clicked.connect(lambda: conn.send(f"M104 S{self.nozzle.value()}"))
        btn_b.clicked.connect(lambda: conn.send(f"M140 S{self.bed.value()}"))
        layout.addWidget(QLabel("Nozzle Sıcaklığı:")); layout.addWidget(self.nozzle); layout.addWidget(btn_n)
        layout.addWidget(QLabel("Yatak Sıcaklığı:")); layout.addWidget(self.bed); layout.addWidget(btn_b)
        btn_get = QPushButton("Sıcaklık Oku")
        btn_get.clicked.connect(lambda: conn.send("M105"))
        layout.addWidget(btn_get)
        self.setLayout(layout)
