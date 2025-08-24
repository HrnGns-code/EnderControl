import serial, serial.tools.list_ports, threading, time
class PrinterConnection:
    def __init__(self):
        self.ser = serial.Serial()
        self.listener = None
    def list_ports(self):
        return [p.device for p in serial.tools.list_ports.comports()]
    def connect(self, port, baud=115200):
        self.ser.port, self.ser.baudrate, self.ser.timeout = port, baud, 1
        self.ser.open()
        self.listener = threading.Thread(target=self._read_loop, daemon=True)
        self.listener.start()
    def disconnect(self):
        if self.ser.is_open:
            self.ser.close()
    def send(self, cmd):
        if self.ser.is_open:
            self.ser.write((cmd + "\n").encode())
    def _read_loop(self):
        while self.ser.is_open:
            try:
                line = self.ser.readline().decode(errors='ignore').strip()
                if line:
                    for cb in getattr(self, 'callbacks', []):
                        cb(line)
            except:
                break
    def register_callback(self, fn):
        self.callbacks = getattr(self, 'callbacks', []) + [fn]
