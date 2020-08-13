import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
POWERSHELL_PATH = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"


def convert_ui_to_py():
    """Convert uis from QT to Python"""
    ps1_path = ROOT_DIR.joinpath('infrastructure/ui_to_py.ps1')
    subprocess.call(
        [POWERSHELL_PATH, str(ps1_path)])