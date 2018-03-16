from server import api
import os

from dashboard_api.resources.user import User, Users

def main():
    port = int(os.environ.get("PORT", 5000))
    api.run(host='0.0.0.0', port=port)
    api.add_resource(User, '/user/<user_id>')
    api.add_resource(Users, '/user/<user_id>')

if __name__ == "__main__":
    main()