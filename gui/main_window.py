from PyQt6.QtWidgets import QMainWindow, QTabWidget
from gui.connection_tab import ConnectionTab
from gui.move_tab import MoveTab
from gui.temperature_tab import TemperatureTab
from gui.gcode_tab import GCodeTab
from gui.terminal_tab import TerminalTab
from core.printer_connection import PrinterConnection
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EnderKontrol")
        self.setFixedSize(800, 600)
        self.conn = PrinterConnection()
        tabs = QTabWidget()
        self.t_conn = ConnectionTab(self.conn)
        self.t_move = MoveTab(self.conn)
        self.t_temp = TemperatureTab(self.conn)
        self.t_gcode = GCodeTab(self.conn)
        self.t_term = TerminalTab(self.conn)
        tabs.addTab(self.t_conn, "🔌 Bağlantı")
        tabs.addTab(self.t_move, "🎮 Eksenler")
        tabs.addTab(self.t_temp, "🔥 Sıcaklık")
        tabs.addTab(self.t_gcode, "📁 G‑code")
        tabs.addTab(self.t_term, "💬 Terminal")
        self.setCentralWidget(tabs)
