from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

def create_gui():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Hello from PySide6!")
    layout.addWidget(label)

    window.setLayout(layout)
    window.setWindowTitle("PySide6 Hello")
    window.show()

    app.exec()

def main():
    create_gui()

if __name__ == "__main__":
    main()
