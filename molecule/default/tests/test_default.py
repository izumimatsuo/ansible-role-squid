import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_squid_is_installed(host):
    package = host.package("squid")
    assert package.is_installed
    assert package.version.startswith("3.5")


def test_squid_running_and_enabled(host):
    service = host.service("squid")
    assert service.is_running
    assert service.is_enabled


def test_squid_listen(host):
    assert host.socket('tcp://0.0.0.0:3128').is_listening
