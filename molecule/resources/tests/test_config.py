import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_openntpd_file(host):
    host_os = host.system_info.distribution

    if host_os == "debian":
        file = host.file("/etc/openntpd/ntpd.conf")
        assert file.exists
        assert file.contains("1.debian.pool.ntp.org")

    elif host_os == "openbsd":
        file = host.file("/etc/ntpd.conf")
        assert file.exists
        assert file.contains("1.debian.pool.ntp.org")

    return
