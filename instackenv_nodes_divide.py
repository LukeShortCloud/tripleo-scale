#!/usr/bin/python3

from yaml import dump as yaml_dump, load as yaml_load

instackenv = None

with open('instackenv.yaml', 'r') as instackenv_file:
    instackenv = yaml_load(instackenv_file)

node_count = len(instackenv['nodes'])
print("Node count: {}".format(node_count))
instackenv_seperate = {'nodes': []}

for index, node in enumerate(instackenv['nodes'], start=1):
    instackenv_seperate['nodes'].append(node)

    # Every 50 nodes (or end of the loop), write to a new file.
    if ((index % 50) == 0) or (index == node_count):

        with open('instackenv_{}.yaml'.format(index), 'w') as instackenv_new:
            instackenv_new.write(yaml_dump(instackenv_seperate))

        instackenv_seperate = {'nodes': []}

    if index == node_count:
        continue
