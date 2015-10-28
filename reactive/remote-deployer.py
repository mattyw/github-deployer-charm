import os
import subprocess

from charmhelpers.core import hookenv
from charms.reactive import hook
from charmhelpers.fetch import install_remote


@hook('config-changed')
def config_changed():
    config = hookenv.config()
    if config.changed('repo'):
        repo = config['repo']
        if repo != "":
            hookenv.status_set('waiting', 'cloning %s' % repo)
            dest = install_remote(repo)
            hookenv.status_set('waiting', 'cloned %s' % repo)
            # Consider payloads
            subprocess.check_call(
                os.path.join(dest, "remote-deployer"),
                cwd=dest,
                )
            hookenv.status_set('active', 'Ready')
