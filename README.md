Role Name
=========

This role is meant for doing Keystone Fernet key rotations in a TripleO overcloud.

Requirements
------------

This requires an already running overcloud.


Example Playbook
----------------

    - hosts: keystone
      become: true
      roles:
        - tripleo-fernet-keys-rotation

License
-------

GPLv3
