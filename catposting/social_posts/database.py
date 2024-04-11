from . import CURSOR


class Post:
    def __init__(self, post_id: int):
        self.id = post_id
        self.cat_name = self.get_cat_name()
        self.title = self.get_title()
        self.filename = f"{str(self.id[0])}.jpg"

    """
    Get data from the MySQL server
    """

    def get_cat_name(self) -> str:
        CURSOR.execute("SELECT cat FROM catposting.posts WHERE post_id = %s", self.id)
        return CURSOR.fetchone()[0]

    def get_title(self) -> str:
        CURSOR.execute("SELECT title FROM catposting.posts WHERE post_id = %s", self.id)
        return CURSOR.fetchone()[0]


def get_all_posts() -> list[Post]:
    CURSOR.execute("SELECT post_id FROM catposting.posts")
    result = CURSOR.fetchall()
    return [Post(x) for x in result]
