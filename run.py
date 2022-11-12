import os

from api import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5005))
    app.run(host="0.0.0.0", port=port)
