import sys
import json
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

CURRENT_VERSION = "1.0.0"

# --- For testing, we'll use a GitHub URL OR a local file ---
# Example version.json content:
# { "version": "1.1.0", "download_url": "https://example.com/myapp-1.1.0.exe" }
VERSION_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/version.json"
# For local testing, you can also use:
# VERSION_URL = "file://C:/path/to/version.json"


class UpdateDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Qt App")
        self.resize(400, 200)

        layout = QVBoxLayout()
        self.label = QLabel(f"Current App Version: {CURRENT_VERSION}")
        self.check_button = QPushButton("Check for Updates")
        self.check_button.clicked.connect(self.check_for_update)

        layout.addWidget(self.label)
        layout.addWidget(self.check_button)
        self.setLayout(layout)

    def check_for_update(self):
        try:
            response = requests.get(VERSION_URL, timeout=5)
            data = response.json()
            latest = data.get("version")
            url = data.get("download_url")

            if latest != CURRENT_VERSION:
                reply = QMessageBox.question(
                    self, "Update Available",
                    f"A new version {latest} is available.\nDo you want to download it?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    import webbrowser
                    webbrowser.open(url)
                    self.close()  # close old app
            else:
                QMessageBox.information(self, "No Update", "You are already on the latest version.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Update check failed: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UpdateDemo()
    window.show()
    sys.exit(app.exec())
