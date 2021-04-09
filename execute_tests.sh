#!/usr/bin/env bash
source venv/bin/activate
echo "-> Installing dependencies"
python -m pip install --upgrade pip
pip3 install -r requirements.txt --quiet

echo "-> Removing old Allure results"
rm -r allure-results/* || echo "No results"
cp environment.properties allure-results/

echo "-> Start testcases"
pytest -n auto testcases --alluredir allure-results --env test
echo "-> Test finished"

echo "-> Generating report"
allure generate allure-results --clean -o allure-report
echo "-> Execute 'allure serve' in the command line"

echo "-> Open report"
allure open allure-report/