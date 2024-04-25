from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from datetime import datetime
import os

def main():
    # The main routine.
    session = getDBSession()
    generateInsertData(123, 345, "comment 1", session)


def getDBSession():
    # Create and get a Cassandra session
    cloud_config= {
            #'secure_connect_bundle': os.environ.get('ASTRA_PATH_TO_SECURE_BUNDLE')
            'secure_connect_bundle': '/Users/sasukoboy/Documents/GitHub/MiniStackOverflow/CommentService/secure-connect-ministackdb.zip'
            #'use_default_tempdir' : True
    }
    auth_provider = PlainTextAuthProvider(os.environ.get('ASTRA_CLIENT_ID'), os.environ.get('ASTRA_CLIENT_SECRET'))
    print(auth_provider)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    return session


# def getDBSession2():
#     # Create and get a Cassandra session
#     cloud_config= {
#             #'secure_connect_bundle': os.environ.get('ASTRA_PATH_TO_SECURE_BUNDLE')
#             'secure_connect_bundle': '/Users/sasukoboy/Documents/GitHub/MiniStackOverflow/CommentService/secure-connect-ministackdb.zip'
#             #'use_default_tempdir' : True
#     }
#     auth_provider = PlainTextAuthProvider(os.environ.get('ASTRA_CLIENT_ID'), os.environ.get('ASTRA_CLIENT_SECRET'))
#     print(auth_provider)
#     cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
#     session = cluster.connect()
#     return session


def generateInsertData(answer_id, user_id, body, session):
    """A function which completes generation of data and insertion of data to Cassandra"""
    insert_query = session.prepare("""
                INSERT INTO comments_keyspace.comments (answer_id, user_id, publication_ts, body)
                VALUES (?, ?, ?, ?)
                IF NOT EXISTS;
                """)
    
    try:
        publication_ts = datetime.now()
        publication_ts = publication_ts.strftime("%Y-%m-%d %H:%M:%S")
        session.execute(insert_query, [answer_id, user_id, publication_ts, body])
        print("Success")
    except Exception as e: 
        print(e)


if __name__ == "__main__":
    main()
