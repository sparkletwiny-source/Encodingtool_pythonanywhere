import sys

# Your Flask application's directory
project_home = "/home/Twin/encodingtool"

if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
