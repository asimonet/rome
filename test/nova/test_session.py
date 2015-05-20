__author__ = 'jonathan'

import unittest
from lib.rome.core.session.session import Session as Session
from lib.rome.core.orm.query import Query as Query
from test.test_dogs import *
import _fixtures as models

class TestSession(unittest.TestCase):

    def test_session_instances(self):
        logging.getLogger().setLevel(logging.DEBUG)
        session = Session()
        # with session.begin():
        # query = Query(models.Instance).filter(models.Instance.id==1)
        query = Query(models.Network)
        instance = query.first()
        # instance.display_name += "a"
        instance.save(force=True)
            # session.add(instance)
            # print(instance)
        pass

    def test_session_execution(self):
        logging.getLogger().setLevel(logging.DEBUG)
        session = Session()
        with session.begin():
            dogs = session.query(Dog).all()
            print("dogs: %s" % (dogs))
            print("session_id: %s" % (session.session_id))
            dogs[0].name += "aa"
            # dogs[0].update({"name": dogs[0].name + "bb"})
            # dogs[0].save(session=session)
            # dogs[0].save(session=session)
            # raise Exception("toto")

    def test_concurrent_update(self):
        import threading
        import time

        def work():
            logging.getLogger().setLevel(logging.DEBUG)
            session = Session()
            with session.begin():
                dogs = Query(Dog).all()
                time.sleep(1)
                print("dogs: %s" % (dogs))
                print("session_id: %s" % (session.session_id))
                dogs[0].name += "bb"
                # dogs[0].update({"name": dogs[0].name + "bb"})
                # dogs[0].save(session=session)

        a = threading.Thread(None, work(), None)
        b = threading.Thread(None, work(), None)
        a.start()
        b.start()


if __name__ == '__main__':
    unittest.main()