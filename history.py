"""
История ввода интерпретатора
"""


class History:
    def __init__(self):
        self.data = []
        self.current_pos = 0

    @staticmethod
    def write_history(self, text):
        sql = """
            INSERT INTO history VALUES ($1, $2, $3)
        """
        return True

    @staticmethod
    def load_history(self):
        sql = """
            SELECT * FROM history WHERE user = $1 ORDER BY time DESC
        """
        return True

    def get_history(self):
        return self.data[self.current_pos] #???
