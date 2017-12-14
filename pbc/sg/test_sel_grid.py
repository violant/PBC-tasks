from pbc.sg.sg import StartGrid, Grid
from selenium import webdriver
import pytest
import requests
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium_grid
def test_sg_sm(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.download_json()
    grid.start_hub()
    grid.add_node()
    res = ssh_client.execute('pgrep java')
    assert len(res) == 2
    grid.clean()


@pytest.mark.selenium_grid
def test_sg_grid_firefox_icons(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.download_json()
    grid.start_hub()
    grid.add_node()
    try:
        driver = webdriver.Firefox()
        driver.get("http://192.168.33.10:4444/grid/console")
        elem = driver.find_elements_by_xpath(
            "//div[@type='browsers' and @class='content_detail']//img[contains(@title,'firefox')]")
        assert 5, elem.count()
    except Exception as e:
        print 'Can\'t get icons count from grid: ' + e.message
        raise e
    finally:
        driver.close()
        grid.clean()


@pytest.mark.selenium_grid
def test_requests(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.download_json()
    grid.start_hub()
    grid.add_node()
    try:
        resp = requests.get('http://192.168.33.10:4444/grid/api/hub/ -d \'{"configuration":["slotCounts"]}\'')
        assert resp.status_code == 200
        json_data = json.loads(resp.text)
        assert 5, json_data['slotCounts']['total']
    except Exception as e:
        print 'Can\'t get response from API with request' + e.message
        raise e
    finally:
        grid.clean()


@pytest.mark.python_org
def test_python(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.download_json()
    grid.start_hub()
    grid.add_node()
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Remote(
            command_executor='http://192.168.33.10:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox'},
            options=options
        )
        driver.get("http://www.python.org")
        assert True, 'Python' in driver.title
        web_element = driver.find_element_by_name('q')
        web_element.clear()
        web_element.send_keys('pycon')
        web_element.send_keys(Keys.ENTER)
        driver.save_screenshot('pycon.png')
    except Exception as e:
        print 'Can\'t search on python_org' + e.message
        raise e
    finally:
        driver.close()
        grid.clean()
