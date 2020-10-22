# python_framework
Python Pytest Framework


To have a dry run of the framework follow below steps.
1. Clone the repo 
```sh
git clone https://github.com/MohammedWaasim/python_framework.git
```
2. Have following plugin and softwares installed
```sh
   pip3 install selenium
   pip3 install pytest
   pip3 install ddt
   pip3 install allure-pytest
   pip3 install pyyaml
   pip3 install requests
   pip3 install webdriver_manager
 ```
3. Set up the env by running this command 
```sh
export PYTHONPATH=$PYTHONPATH:.
```
4. Run this line in the project folder 
```sh
pytest tests/test_suite_demo.py --browser chrome --alluredir=reports --env staging
```
5. To run api test alone exe this command 'pytest -k api --alluredir=reports'
7. To run Web test alone exe 'pytest -k web --browser chrome --alluredir=reports'
6. Finally to view the report run 'allure serve reports' <- this command will open the report in the dynamic page and
will remain there till we press ctrl+c on the terminal.
  
