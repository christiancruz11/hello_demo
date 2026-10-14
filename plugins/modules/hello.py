#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v2.0+

from __future__ import absolute_import, division, print_function
__metaclass__ = type


# ---------------------------------------------------------------
# DOCUMENTATION block — this is what shows up when someone runs:
#   ansible-doc redhat_demo.hello_demo.hello
# ---------------------------------------------------------------
DOCUMENTATION = r'''
---
module: hello
short_description: Returns a greeting message
version_added: "1.0.0"
description:
    - A simple demo module that returns a greeting message.
    - Useful for verifying the collection is installed and working.
options:
    name:
        description:
            - The name to include in the greeting.
        required: false
        type: str
        default: World
author:
    - Chris Cruz (@chcruz)
'''

# ---------------------------------------------------------------
# EXAMPLES block — shows users how to call the module in a playbook
# ---------------------------------------------------------------
EXAMPLES = r'''
- name: Say hello with default
  redhat_demo.hello_demo.hello:

- name: Say hello to AAP
  redhat_demo.hello_demo.hello:
    name: "Ansible Automation Platform"
  register: result

- name: Show the greeting
  ansible.builtin.debug:
    msg: "{{ result.message }}"
'''

# ---------------------------------------------------------------
# RETURN block — documents what the module gives back
# ---------------------------------------------------------------
RETURN = r'''
message:
    description: The greeting message.
    type: str
    returned: always
    sample: "Hello, World! Greetings from redhat_demo.hello_demo."
'''


# ---------------------------------------------------------------
# The actual module logic starts here
# ---------------------------------------------------------------
from ansible.module_utils.basic import AnsibleModule  # Ansible's helper library


def run_module():
    # Define what parameters this module accepts
    module_args = dict(
        name=dict(type='str', required=False, default='World'),
    )

    # Create the module object — this handles arg parsing, check mode, etc.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    # Build the result
    name = module.params['name']
    message = f"Hello, {name}! Greetings from redhat_demo.hello_demo."

    # Return success with our message
    # changed=False because this module doesn't modify anything
    module.exit_json(changed=False, message=message)


def main():
    run_module()


if __name__ == '__main__':
    main()
