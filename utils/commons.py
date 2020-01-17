import uuid

from django.db import connection


class DatabaseOperation:
    @staticmethod
    def data_to_dict(cursor, data):
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in data
        ]

    @staticmethod
    def select_one(sql, values=None):
        cursor = connection.cursor()
        if values is not None:
            cursor.execute(sql, values)
            return cursor.fetchone()
        cursor.execute(sql)
        results = DatabaseOperation.data_to_dict(cursor, cursor.fetchone())
        return results

    @staticmethod
    def select_all(sql, values=None):
        cursor = connection.cursor()
        if values is not None:
            cursor.execute(sql, values)
            return cursor.fetchall()
        cursor.execute(sql)
        results = DatabaseOperation.data_to_dict(cursor, cursor.fetchall())
        return results

    @staticmethod
    def execute(sql, values=None):
        cursor = connection.cursor()
        try:
            if values is not None:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
        except Exception as e:
            print("执行单条语句时", e)
        finally:
            cursor.close()

    @staticmethod
    def executemany(sql, values=None):
        cursor = connection.cursor()
        try:
            if values is not None:
                cursor.executemany(sql, values)
            else:
                cursor.execute(sql)
        except Exception as e:
            print("执行多条语句时", e)
        finally:
            cursor.close()

    @staticmethod
    def select_column_values(sql, values=None):
        cursor = connection.cursor()
        if values:
            cursor.execute(sql, values)
        cursor.execute(sql)
        return cursor.fetchone()


class LogsOperations:

    @staticmethod
    def add_log(log_msg, current_time):
        log_id = str(uuid.uuid4()).replace("-", "")[:20]
        username = "胡先森"  # 测试专用名，用户登录之后，可以转客户昵称
        sql = """
            insert into logs_logs
            (log_id, name, somethings, runtime)
            values (%s, %s, %s, %s)
        """
        values = (log_id, username, log_msg, current_time)
        DatabaseOperation.execute(sql, values)
