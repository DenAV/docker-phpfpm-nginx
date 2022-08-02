import os
import pytest
import testinfra

def test_os_release(host):
    assert host.file("/etc/os-release").contains("Alpine Linux")

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.16.1")


#def test_nginx_running_and_enabled(host):
#    nginx = host.service("nginx")
#    assert nginx.is_running
#    assert nginx.is_enabled
