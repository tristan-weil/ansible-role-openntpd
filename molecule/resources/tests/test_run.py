import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_openntpd_run(host):
    c = host.run(r'ntpctl -s status | egrep -vq "O/[0-9]+ peers valid"')
    assert c.rc == 0
