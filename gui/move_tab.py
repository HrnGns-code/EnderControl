from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QSpinBox
class MoveTab(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        layout = QVBoxLayout()
        h_step = QHBoxLayout()
        h_step.addWidget(QLabel("Adım (mm):"))
        self.step = QSpinBox()
        self.step.setRange(1, 100)
        self.step.setValue(10)
        h_step.addWidget(self.step)
        layout.addLayout(h_step)
        axes = ['X', 'Y', 'Z']
        for axis in axes:
            h = QHBoxLayout()
            btn_neg = QPushButton(f"{axis}-")
            btn_pos = QPushButton(f"{axis}+")
            btn_neg.clicked.connect(lambda _, ax=axis: self.move(ax, -1))
            btn_pos.clicked.connect(lambda _, ax=axis: self.move(ax, 1))
            h.addWidget(btn_neg)
            h.addWidget(btn_pos)
            layout.addLayout(h)
        home = QPushButton("Home All")
        home.clicked.connect(lambda: self.conn.send("G28"))
        layout.addWidget(home)
        self.setLayout(layout)
    def move(self, axis, direction):
        dist = self.step.value() * direction
        self.conn.send(f"G91\nG1 {axis}{dist} F3000\nG90")
