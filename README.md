# Ansible Role: openntpd

An Ansible Role that installs and configures `OpenNTPD`.

[![Actions Status](https://github.com/tristan-weil/ansible-role-openntpd/workflows/molecule/badge.svg?branch=master)](https://github.com/tristan-weil/ansible-role-openntpd/actions)

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

Mandatory variables:

| Variable      | Description |
| :------------ | :---------- |

Optional variables:

| Variable      | Default | Description |
| :------------ | :------ | :---------- |
| openntpd_listen | []    | a list of IP addresses to listen on |
| openntpd_sensors | []   | a list of name of sensors (`*` for all) |
| openntpd_pools | ...     | a list of <*openntpd_pool*> |
| openntpd_constraints | ... | a list of <*openntpd_constraint*>  (need libtls) |

### <*openntpd_pool*>

An *openntpd_pool* represents a NTP pool address.

Mandatory variables:

| Variable      | Description |
| :------------ | :---------- |
| type          | *server / servers*: the type of the pool (*server*: use only the first IP returned by DNS / *servers*: use all IPs) |
| address       | the IP or hostname |

Optional variables:

| Variable      | Default | Description |
| :------------ | :------ | :---------- |
| weight        | 1       | the weight of the pool |
| trusted       | False   | *True / False*: mark this pool as trusted |

### <*openntpd_constraint*>

An *openntpd_constraint* represents an OpenNTPd constraint.

Mandatory variables:

| Variable      | Description |
| :------------ | :---------- |
| type          | *constraint / constraints*: the type of the constraint (*constraint*: use only the first IP returned by DNS / *constraints*: use all IPs) |
| address       | the IP or hostname |

Optional variables:

| Variable      | Default | Description |
| :------------ | :------ | :---------- |

## Example Playbook

    - hosts: 'webservers'
      roles:
        - role: 'ansible-role-openntpd'

## Todo

None.

## Dependencies

See [requirements_galaxy.yml](https://github.com/tristan-weil/ansible-role-openntpd/blob/master/requirements_galaxy.yml)

## Supported platforms

See [meta/main.yml](https://github.com/tristan-weil/ansible-role-openntpd/blob/master/meta/main.yml)

## License

See [LICENSE.md](https://github.com/tristan-weil/ansible-role-openntpd/blob/master/LICENSE.md)