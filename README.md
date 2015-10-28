# remote-deployer-charm

This charm copies remote file trees to the unit, then runs any remote-deployer
file found within this directory to perform any desired setup.

remote paths can be copied using charm config:
```bash
juju deploy remote-deployer
juju set remote-deployer/0 http://github.com/myname/myrepo
```

or actions:
```bash
juju deploy remote-deployer
juju action do remote-deployer/0 deploy source=http://github.com/myname/myrepo
```

In both cases the charm will clone the github repo, then look inside it for a remote-deployer file.
This file will run, to do whatever installation or config is defined by that file
