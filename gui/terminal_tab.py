from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
class TerminalTab(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        layout = QVBoxLayout()
        self.text = QTextEdit(); self.text.setReadOnly(True)
        self.entry = QLineEdit()
        btn_send = QPushButton("Gönder")
        btn_send.clicked.connect(self.send)
        layout.addWidget(self.text)
        layout.addWidget(self.entry)
        layout.addWidget(btn_send)
        conn.register_callback(self.receive)
        self.setLayout(layout)
    def send(self):
        cmd = self.entry.text()
        self.conn.send(cmd)
        self.text.append(f"> {cmd}")
        self.entry.clear()
    def receive(self, msg):
        self.text.append(f"< {msg}")
