import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from apps.buganizer.controller import register_routes
from flask import Flask


def create_app() -> Flask:
  app = Flask(__name__)
  register_routes(app)
  return app


def main():
  app = create_app()
  app.run(host="0.0.0.0", port=8081, debug=True)


if __name__ == "__main__":
  main()




