## Ansible commands and modules

1.- For file and directory Management:

    - file: Maange file and riectory attributes (permissions, ownerships, etc.)
    - copy: Copy files from the control machine to the target system.
    - fetch: Fetch files from the target system to the control machine.
    - template: Deploy files with dynamic content (Jinja2 templating).
    - unarchive: Extract archives like .tar or .zip
    - lineinfile: Manage single lines in a file (e.g., add, replace).
    - blockinfile: Manage blocks of text in files

2.- Command execution:

    - command: Execute simple command without a shell.
    - shell: Execute commands requiring shell features (e.g., pipes, redirects).
    - script: Upload and execute  local script on the target system.
    - raw: Execute raw commands (bypassin Ansible modules, useful for devices with no Python)


3.- Package Management:

    - apt: Manage packages on Debian-based systems (e.g, Ubuntu)
    - yum: Manage packages on Red Hat-based systems (e.g., Centos, Fedora)
    - dnf: Newer package manager for Red Hat-based systems.
    - pip: Manage Pythonpackages.
    - gem: Manage Ruby gembs.
    - snap: Manage Snap packages

4.- Service Management:

    - service: Manage services (start, stop, restart).
    - systemctl: Directly manage systemd services
    - supervisord: Manage process via Supervisor


5.- User and Group Management:

    - user: Manage user accounts
    - group: Manage by groups


6.- Networking:

    - uri: Interact with HTTP Apis.
    - get_url: Download files from URL
    - slurp: Retrieve the content of remote files (binary-safe)


7.- Cloud and Virtualization:

    - docker_container: Manage Docker containers.
    - docker_image: Manage Docker images
    - ec2: Manage Amazon EC2 instances.
    - azure_rm_¨: Manage Azre resources 
    - gcp_*: Manage Google Cloud reources: 

8.- Cokntrol Flow:

    - include_tasks: Include tasks from another file.
    - import_tasks: import tasks (statically).
    - set_fact: Set variables dynamically during playbook execution.
    - debug: Print debug messages.


9.- Database Management:

    - mysql_user: Manage MySQL users.
    - postgresql_db: Manage PostgreSQL databases.
    - mongodb_user: Manage MongoDB users.

10.- System Information:
    
    - setup: Gather facts about the target system.
    - ansible.builtin.stat: Retrieve information about a file.
    - ping: Test conectivity between Ansible and the target system.


Ansible structure path

```yml
---
- name: Execute a script on localhost
  hosts: localhost
  become: true
  tasks:
  - name: Ensure the script has execute permissions
    file:
      path: <path location file>
      mode: u+x
      state: file
  - name: Testing this file  
    shell: <set a bash command>


  - name: Execute the script
    command: <file to execute>
```
