from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test
from sqlite3 import ProgrammingError

class Controller:
  def __init__(self) -> None:
        engine = create_engine(
            "sqlite:///C:\\Users\\Daniel\\Desktop\\Cursos\\ProjectosPropios\\appExamenes\\testsdb\\test.db"
        )
        Session = sessionmaker(bind=engine)
        session = Session()

##  Para crear un texto
  def create_empty_test(self, _test_name):
      ##      Para comprobar que no hay ningun test con el mismo nombre
      test = self.session.query(Test).filter(Test.test_name == _test_name).first()
      if test == None:
          new_test = Test(test_name=_test_name)
          self.session.add(new_test)
          self.session.commit()
      else:
          raise ProgrammingError("Test already exists")
