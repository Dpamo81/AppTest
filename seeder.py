from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test

##
if __name__ == "__main__":
    engine = create_engine('sqlite:///C:\\Users\\Daniel\\Desktop\\Cursos\\ProjectosPropios\\appExamenes\\testsdb\\test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    questions = [
        Question(
            question_text = "Los buceadores pueden ayudar a proteger el medio ambiente marino si:",
            answers = [
                Answer(
                    answer_text="Todas las respuestas son correctas",
                    is_correct=True
                ),
                Answer(
                    answer_text="Siendo siempre un buceador responsable",
                    is_correct=False
                ),
                Answer(
                    answer_text="Mantiene el equipo asegurado y sin piezas colgando",
                    is_correct=False
                ),
                Answer(
                    answer_text="Mantiene flotabilidad neutra en todo momento",
                    is_correct=False
                )
            ]
        ),
        Question(
            question_text = "El océano es una fuente importante de vida gracias a que:",
            answers = [
                Answer(
                    answer_text="Abarca gran parte de la superficie de la Tierra",
                    is_correct=False
                ),
                Answer(
                    answer_text="Es el hogar de muchos de los primeros eslabones de la cadena alimentaria de la Tierra",
                    is_correct=True
                ),
                Answer(
                    answer_text="Proporciona un suministro inteminable de alimento",
                    is_correct=False
                ),
                Answer(
                    answer_text="Proporciona a los seres humanos el agua de lluvia para beber",
                    is_correct=False
                )
            ]
        ),
    ]
    test = Test(test_name="OWD", questions=questions)
    session.add(test)
    session.commit()
