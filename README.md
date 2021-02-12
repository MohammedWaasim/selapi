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
4. To Start Dockerized Selenium-grid run below command
```commandline
docker-compose -f docker-compose.yml up --scale chrome=2
``` 
5. Verify Selenium-Grid is up and running with 2 chrome containers and 1 firfox container in 
```html
http://localhost:4444/ui/index.html#/
```
6. Run below command which executes tests in parallel with 4 threads

```shell script
 pytest tests/skf_test.py -v -s --browser="docker-chrome" --alluredir="reports" -n 4
```
7. To View test reports run below command
```shell script
allure serve reports
```