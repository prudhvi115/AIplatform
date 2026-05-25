import os
import sys
from pathlib import Path

# Add the Django project directory to the Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "sampleproj1"))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "study_platform.settings")

from study_platform.wsgi import application as app
