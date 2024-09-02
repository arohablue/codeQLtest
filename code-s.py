import sqlite3

class PostDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def getPostsByPostid(self, postid):
        """
        Fetches posts from the database based on postid.
        Uses parameterized queries to avoid SQL injection.

        Args:
        postid (int): The ID of the post.

        Returns:
        list: A list of tuples containing user names and post comments.
        """
        sqlText = """
        SELECT users.name, post.comment 
        FROM users 
        JOIN post ON users.userid = post.userid 
        WHERE post.postid = ?
        """
        params = (postid,)
        return self.queryDB(sqlText, params)

    def queryDB(self, sqlText, params):
        """
        Executes a query on the database and fetches the results.

        Args:
        sqlText (str): The SQL query to be executed.
        params (tuple): Parameters to be used in the query.

        Returns:
        list: A list of tuples containing the results of the query.
        """
        cursor = self.conn.cursor()
        cursor.execute(sqlText, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db = PostDatabase('example.db')
    postid = 1
    posts = db.getPostsByPostid(postid)
    for post in posts:
        print(f"User: {post[0]}, Comment: {post[1]}")
    db.close()
