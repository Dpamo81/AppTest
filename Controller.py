from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test
from sqlite3 import ProgrammingError

class Controller:
    def __init__(self) -> None:
        engine = create_engine(
            'sqlite:///C:\\Users\\Daniel\\Desktop\\Cursos\\ProjectosPropios\\appExamenes\\testsdb\\test.db'
        )
        Session = sessionmaker(bind=engine)
        self.session = Session()

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
##  Para introducir los test manualmente
    def get_test_names(self):
        tests = self.session.query().with_entities(Test.test_name, Test.test_id).all()
        test_names = [test[0] for test in tests]
        return test_names
##  Para insertar en la BBDD
    def add_question(self, test_name,question_text, question_choices, correct_choice):
        test = self.session.query(Test).filter(Test.test_name == test_name).first()
        _answers = [
            Answer(
                answer_text=choice,
                is_correct=correct_choice == idx,
            )for idx, choice in enumerate(question_choices)
        ]
        question = Question(
            question_text=question_text,
            answers = _answers,
            test_id=test.test_id
        )
        self.session.add(question)
        self.session.commit()

"""f __name__ == "__main__":
    c = Controller()
    c.get_test_names()"""
