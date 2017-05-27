# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# hive util with hive server2

"""
@author:miles
@create:2017-05-25 16:55
"""

from pyhive import hive


class HiveClient:
    def __init__(self, db_host):
        """
        create connection to hive server2
        """
        self.conn = hive.connect(db_host)

    def query(self, sql):
        """
        query
        """

        # with self.conn.cursor() as cursor:
        #     cursor.execute(sql)
        #     return cursor.fetchall()
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def close(self):
        """
        close connection
        """
        self.conn.close()


def main():
    """
    main process
    @rtype:
    @return:
    @note:

    """
    hive_client = HiveClient(db_host='10.255.128.1')
    result = hive_client.query('select * from metadata.app_id_info')
    print result
    hive_client.close()


if __name__ == '__main__':
    main()
