# greeting

Displays a greeting using the `hello` module from `redhat_demo.hello_demo`.

## Role Variables

- `greeting_name` — The name to greet (default: `"World"`)

## Example

```yaml
- hosts: localhost
  roles:
    - role: redhat_demo.hello_demo.greeting
      vars:
        greeting_name: "AAP Audience"
```
