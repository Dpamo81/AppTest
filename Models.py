from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean

Base = declarative_base()

## Definimos la tabla Answer
class Answer(Base):    
    __tablename__ = "answer"
    answer_id   = Column(Integer, primary_key=True)
    answer_text = Column(String(200))
    is_correct  = Column(Boolean, nullable=True)
    question_id = Column(Integer, ForeignKey("question.question_id", ondelete="CASCADE"))
##  Permite imprimir el objeto
    def __repr__(self) -> str:
        return f"Answer object: Answer id: {self.answer_id}. Answer text: {self.answer_text}"
## Definimos la tabla Questions
class Question(Base):
    __tablename__   = "question"
    question_id     = Column(Integer, primary_key = True)
    question_text   = Column(String(200))
    answers         = relationship("Answer", cascade="all,delete", backref=backref("question"))
    test_id         = Column(Integer, ForeignKey("test.test_id", ondelete="CASCADE"))

    def __repr__(self) -> str:
        return f"Question object: Question id: {self.question_id}. Answer text: {self.question_text}"
## Definimos la tabla de Test
class Test(Base):
    __tablename__   = "test"
    test_id         = Column(Integer, primary_key = True)
    test_name       = Column(String(100))
    questions       = relationship("Question", cascade="all,delete", backref=backref("test"))

    def __repr__(self) -> str:
        return f"Test object: Test id: {self.test_id}. Answer text: {self.test_name}"
## Para crear la BBDD
if __name__== "__main__":
    engine = create_engine('sqlite:///C:\\Users\\Daniel\\Desktop\\Cursos\\ProjectosPropios\\appExamenes\\testsdb\\test.db', echo=True)
    Base.metadata.create_all(engine)
