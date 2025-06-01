import pytest
from sqlalchemy.orm import Session
from models import Student, SessionLocal, init_db

@pytest.fixture(scope='module')
def db():
    # Инициализация базы данных
    init_db()
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture(autouse=True)
def cleanup(db):
    # Очистка таблицы перед каждым тестом
    db.query(Student).delete()
    db.commit()

def test_add_student(db: Session):
    new_student = Student(user_id=1, level="Bachelor", education_form="Full-time", subject_id=101)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    assert new_student.user_id == 1  # Проверка, что пользователь был добавлен
    assert new_student.level == "Bachelor"
    assert new_student.education_form == "Full-time"
    assert new_student.subject_id == 101

def test_update_student(db: Session):
    student = Student(user_id=2, level="Master", education_form="Part-time", subject_id=102)
    db.add(student)
    db.commit()

    # Обновление уровня студента
    student.level = "PhD"
    db.commit()

    updated_student = db.query(Student).filter(Student.user_id == student.user_id).first()
    assert updated_student.level == "PhD"  # Проверка обновления уровня

def test_delete_student(db: Session):
    student = Student(user_id=3, level="Bachelor", education_form="Full-time", subject_id=103)
    db.add(student)
    db.commit()

    db.delete(student)
    db.commit()

    deleted_student = db.query(Student).filter(Student.user_id == student.user_id).first()
    assert deleted_student is None  # Проверка удаления студента
