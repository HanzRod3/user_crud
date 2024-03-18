from mysqlconnection import connectToMySQL
from pprint import pprint


# this constructor function accepts a dictionary as input data
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    """CREATE METHOD"""

    @classmethod
    def find_all(cls):
        query = "SELECT * from users"
        list_of_dicts = connectToMySQL("user_schema").query_db(query)
        pprint(list_of_dicts)

        users = []
        for each_dict in list_of_dicts:
            user = User(each_dict)
            users.append(user)
        return users

    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES
        (%(first_name)s, %(last_name)s, %(email)s);
        """

        user_id = connectToMySQL("user_schema").query_db(query, form_data)
        return user_id

    @classmethod
    def find_by_id(cls, user_id):
        query = " SELECT * From users WHERE id = %(user_id)s;"
        data = {"user_id": user_id}
        list_of_dicts = connectToMySQL("user_schema").query_db(query, data)
        if len(list_of_dicts) == 0:
            return None
        user = User(list_of_dicts)
        return user
