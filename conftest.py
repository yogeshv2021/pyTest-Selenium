from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
import pytest,json,os,difflib,threading,openai,codecs
import pytest_check as check


@pytest.fixture(scope="session")
def driver(request):
    options=Options()
    options.add_argument("--no-sandbox")          # Needed in Linux environments
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")         # safe fallback
    options.add_argument("--remote-debugging-port=9515")  # prevent DevTools port crash
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--headless=new")


    service = Service("/home/yoge1542/Automation/RagAsTesting/selenium/resources/chromedriver")     # adjust path if needed

    driver = webdriver.Chrome(service=service,options=options)	

    driver.maximize_window()

    yield driver

    driver.quit()

def pytest_collection_modifyitems(session,config,items):

    ordered=[]

#    class_order=["TestLogin","TestVoice","TestFlowBuiler","TestLogout"]

    class_order=["TestLogin","TestFlowBuiler","TestLogout"]

    print(session,config,items)

    for cls in class_order:
        for item in items:
            if cls in item.nodeid:
                ordered.append(item)
    items[:] = ordered
