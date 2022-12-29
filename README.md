# Project_rtk

Python UI testing framework.

Prerequisites:
install python ^3.10
install poetry

Installation:
1. Install dependencies $poetry install

Usage:
1. Run all tests $poetry run pytest
2. Run only specific test $poetry run pytest tests/<test_filename>
3. Run only specific function from the test $poetry run pytest -k '<part_of_test_fn_name>'
4. Run only positive tests $poetry run pytest -m positive
5. Run only negative tests $poetry run pytest -m negative

Links:
target: https://b2c.passport.rt.ru
