import pytest as _pytest


@_pytest.mark.parametrize('username, theme, plugins', [
    ('test_usr1', 'robbyrussell', 'git'),
    ('test_usr2', 'custom_usr2_theme', 'git usr2_plugin_1 usr2_plugin_2'),
])
def test_zsh_config_file(host, username, theme, plugins):
    zshrc = host.file(f'/home/{username}/.zshrc')

    assert zshrc.exists
    assert zshrc.is_file
    assert zshrc.mode == 0o644
    assert zshrc.contains(theme)
    assert zshrc.contains(plugins)


@_pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_zsh_alias_config_file(host, username):
    zsh_aliases = host.file(f'/home/{username}/.zsh_aliases')

    assert zsh_aliases.exists
    assert zsh_aliases.is_file
    assert zsh_aliases.mode == 0o644


@_pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_oh_my_zsh_install(host, username):
    oh_my_zsh = host.file(f'/home/{username}/.oh-my-zsh')

    assert oh_my_zsh.exists
    assert oh_my_zsh.is_directory
    assert oh_my_zsh.user == username
    assert oh_my_zsh.group in [username, 'users']
