import pymysql

class SqlProc(object):
    
    def __init__(self, host, port, username, password, db, charset):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
    
    def _getConn(self):
        conn = pymysql.connect(host=self.host, port=self.port,
                                user=self.username, password=self.password,
                                db=self.db, charset=self.charset,
                                cursorclass=pymysql.cursors.DictCursor)
        return conn

    def insertData(self, sql, data):
        '''
        执行insert sql 语句
        如果插入成功，则返回True 以及 插入id号
        如果插入失败，这返回False 以及 -1
        '''
        conn = self._getConn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, data)
            conn.commit()
        except:
            conn.rollback()
            return False, -1
        finally:
            # cursor.close()
            conn.close()

        return True, cursor.lastrowid

    def selectData(self, sql, data):
        '''
        数据库查询操作
        如果查询成功，返回所有数据
        如果查询失败，返回-1，并回滚
        '''
        conn = self._getConn()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, data)
        except:
            # conn.rollback()
            return -1
        finally:
            # cursor.close()
            conn.close()

        return cursor.fetchall()

    def updateData(self, sql, data):
        '''
        更新数据
        '''
        conn = self._getConn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, data)
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()





        