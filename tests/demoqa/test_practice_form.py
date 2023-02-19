import datetime
import allure
from qa_guru_python_3_10.model.pages.practice_form import practice_form
from qa_guru_python_3_10.model.data.user import User
from qa_guru_python_3_10.utils import attach


def test_successful_submit_student_registration_form():
    with allure.step("Open registration form"):
        practice_form.given_opened()

    with allure.step("Fill form"):
        practice_form.fill_student(Vlad).submit_form()

    with allure.step("Check form results"):
        practice_form.assert_submitted(Vlad)

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)


Vlad = User(
    name="Vladislav",
    last_name="Kamenskiy",
    email="dje.fry@mail.ru",
    gender="Male",
    mobile_number="9162754427",
    date_of_birth=datetime.date(1994, 9, 19),
    subjects="English",
    hobbies=("Sports", "Music"),
    picture="test_pictures.webp",
    current_address="Novotushinskiy proezd 8",
    state="Haryana",
    city="Panipat",
)

