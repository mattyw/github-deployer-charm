# github-deployer-charm

The idea of this charm is to be general purpose github deployer "thing".

```bash
juju deploy github-deployer
juju set github-deployer/0 http://github.com/myname/myrepo
```

The charm will clone this repo, then look inside it for a github-deployer file.
This file will run, to do whatever installation or config you like
