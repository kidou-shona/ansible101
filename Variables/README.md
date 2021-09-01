ansible [hostname] -m setup

ansible-playbook [playbook] -e @vars.yaml

ansible localhost -m setup -a 'gather_subset=!all'
