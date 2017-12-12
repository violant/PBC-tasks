from pbc.sg.sg import StartGrid, Grid


def test_sg_sm(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()
    res = ssh_client.execute('pgrep java')
    assert len(res) == 2
