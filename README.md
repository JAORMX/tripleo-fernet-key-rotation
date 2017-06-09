Role Name
=========

This role is meant for doing Keystone Fernet key rotations in a TripleO
overcloud.

Requirements
------------

This requires an already running overcloud and preferably Ansible 2.0 or
higher.


Examples
--------

With an inventory that points to the keystone nodes you could run the following
playbook in order to do a rotation.

    - hosts: keystone
      become: true
      roles:
        - tripleo-fernet-keys-rotation

In the Pike release of TripleO, it's possible to get such an inventory
dynamically by using the /usr/bin/tripleo-ansible-inventory script. Once could
use it directly on the playbook by adding the following parameter to the
ansible-playbook call:

```
ansible-playbook \
    ...
    -i /usr/bin/tripleo-ansible-inventory \
    ...
```

Or you could generate a static inventory from that script by doing the
following:

```
/usr/bin/tripleo-ansible-inventory --static-inventory inventory.txt
```

License
-------

GPLv3
