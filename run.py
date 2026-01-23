import os
from app import app, db

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # Get port from environment variable, default to 5000 for local dev
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" is required for Render to route traffic to your app
    app.run(host="0.0.0.0", port=port, debug=False)