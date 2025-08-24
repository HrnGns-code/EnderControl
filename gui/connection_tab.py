from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout
class ConnectionTab(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        layout = QVBoxLayout()
        h = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItems(self.conn.list_ports())
        self.btn_refresh = QPushButton("Yenile")
        self.btn_refresh.clicked.connect(self.refresh)
        self.btn_connect = QPushButton("Bağlan")
        self.btn_connect.clicked.connect(self.do_connect)
        h.addWidget(QLabel("Port:")); h.addWidget(self.cb); h.addWidget(self.btn_refresh); h.addWidget(self.btn_connect)
        layout.addLayout(h)
        self.lbl = QLabel("Durum: Kapalı")
        layout.addWidget(self.lbl)
        self.setLayout(layout)
    def refresh(self):
        self.cb.clear(); self.cb.addItems(self.conn.list_ports())
    def do_connect(self):
        port = self.cb.currentText()
        try:
            self.conn.connect(port)
            self.lbl.setText(f"Durum: Bağlı ({port})")
        except Exception as e:
            self.lbl.setText(f"Bağlantı hatası: {e}")
