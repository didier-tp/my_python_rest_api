cd ..

#create virtualenv:
python -m venv .venv

#activate virtualenv:
. .venv/bin/activate

#pip in venv (sudo not advised , only if necessary):
#python -m pip install -r requirements.txt
sudo python -m pip install -r requirements.txt

#run test
pytest --junit-xml test-reports/results.xml test_devise_api.py
