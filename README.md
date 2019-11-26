# tripleo-scale

Scripts relating to large TripleO scaling.

## Requirements

- TripleO >= Queens release.
- Python 2.7 or >= 3.6

## Scripts

- instackenv_nodes_divide.py = Seperate an `instackenv.yaml` file into multiple files for every 50 nodes. This provides a more reliable way to introspect a large amount of nodes using a single Undercloud node by dividing and conquering. Alternatively, consider deploying multiple [Minion nodes](https://docs.openstack.org/project-deploy-guide/tripleo-docs/latest/features/undercloud_minion.html) to help scale Ironic horizontally.

```
$ ./instackenv_nodes_divide.py
$ for instackenv in $(ls -1 instackenv_*.yaml); do openstack overcloud node import --introspect --provide $instackenv; done
```

## License

Apache v2.0
