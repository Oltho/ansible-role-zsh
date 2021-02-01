Ansible Role: Zsh - Oh My Zsh
=========

Role that install and configure [oh-my-zsh](https://ohmyz.sh/)

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

The following variables will change the behavior of this role (default values are shown below):

```yaml
# Default theme
oh_my_zsh_theme: robbyrussell

# Default plugins
oh_my_zsh_plugins:
  - git

# User configuration
user:
  username: example1
  oh_my_zsh:
    theme: robbyrussell
    plugins:
      - git
```

Dependencies
------------

N/A

Example Playbook
----------------

```yaml
- hosts: "servers"
  roles:
    - role: "zsh"
      user:
        username: "example1"
```

License
-------

MIT

Author Information
------------------

Thomas TRAN
