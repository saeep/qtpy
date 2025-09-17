import requests
from PySide6 import QtWidgets

CURRENT_VERSION = "1.1.0"  # 🔹 lower than version.json so update will show
VERSION_URL = "https://raw.githubusercontent.com/saeep/qtpy/main/version.json"

def check_for_update():
    try:
        response = requests.get(VERSION_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        latest_version = data.get("version", "")
        download_url = data.get("url", "")

        if latest_version and latest_version > CURRENT_VERSION:
            QtWidgets.QMessageBox.information(
                None,
                "Update Available",
                f"A new version ({latest_version}) is available!\n\nDownload here:\n{download_url}"
            )
        else:
            QtWidgets.QMessageBox.information(
                None,
                "Up to Date",
                f"You are using the latest version ({CURRENT_VERSION})."
            )

    except Exception as e:
        QtWidgets.QMessageBox.warning(None, "Update Check Failed", str(e))

