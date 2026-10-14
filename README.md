# redhat_demo.hello_demo

A demo collection for Ansible Automation Platform (AAP).

## Modules

- **hello** — Returns a greeting message.

## Roles

- **greeting** — Calls the hello module and displays the result.

## Example

```yaml
- hosts: localhost
  tasks:
    - name: Say hello
      redhat_demo.hello_demo.hello:
        name: "AAP Demo"
      register: result

    - debug:
        msg: "{{ result.message }}"
```
