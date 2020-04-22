import psycopg2
import psycopg2.extras
import os


class Data:

    def read_db(self, query, data):
        """
        Fetch data from the db
        :param data:
        :param query:
        :return:
        """
        # Create connection and cursor
        connection = self._connect_db()
        dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # Run the query
        if data is not None:
            dict_cursor.execute(query, data)
        else:
            dict_cursor.execute(query)
        # Get all results
        entries = dict_cursor.fetchall()
        # Clean up DB connection
        dict_cursor.close()
        connection.close()

        return entries

    def write_db(self, query, data):
        """
        Perform db modifications (create, update, delete)
        :param query:
        :param data:
        :return:
        """
        # Create connection and cursor
        connection = self._connect_db()
        dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # Run the query
        if data is not None:
            dict_cursor.execute(query, data)
        else:
            dict_cursor.execute(query)
        # commit changes
        connection.commit()
        # Clean up DB connection
        dict_cursor.close()
        connection.close()

        return

    @staticmethod
    def _connect_db():
        """
        Establish db connection for read operations
        :return:
        """
        try:
            conn_string = "dbname=%s user=%s host=%s password=%s" % (os.environ['DB_NAME'],
                                                                     os.environ['DB_USER'],
                                                                     os.environ['DB_HOST'],
                                                                     os.environ['DB_PASS'])

            # Return DB connection handle
            return psycopg2.connect(conn_string)

        except psycopg2.Error as e:
            print("I am unable to connect to the database: {}".format(e.pgerror))
