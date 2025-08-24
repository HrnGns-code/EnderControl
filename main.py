import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.splash_screen import SplashScreen
def main():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.finish_delay = 2000  # milisaniye
    window = MainWindow()
    def show_main():
        window.show()
    splash.finished.connect(show_main)
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
