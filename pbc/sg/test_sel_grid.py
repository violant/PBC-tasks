from pbc.sg.sg import StartGrid, Grid
from selenium import webdriver


def test_sg_sm(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.download_json()
    grid.start_hub()
    grid.add_node()
    res = ssh_client.execute('pgrep java')
    assert len(res) == 2
    grid.clean()


def test_sg_grid_firefox_icons(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.download_json()
    grid.start_hub()
    grid.add_node()
    driver = webdriver.Firefox()
    driver.get("http://192.168.33.10:4444/grid/console")
    elem = driver.find_elements_by_xpath(
        "//div[@type='browsers' and @class='content_detail']//img[contains(@title,'firefox')]")
    assert 5, elem.count()
    driver.close()
    grid.clean()
