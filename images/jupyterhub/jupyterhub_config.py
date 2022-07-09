# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os

# from jupyterhub.auth import DummyAuthenticator
# c.JupyterHub.authenticator_class = DummyAuthenticator
# c.DummyAuthenticator.password = "some_password"

# c.JupyterHub.hub_ip = '127.0.0.1'
# c.JupyterHub.hub_ip = '*'
## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

c.Authenticator.admin_users = {'jupadmin'}
# c.Authenticator.admin_users = { 'hardway_admin' }
c.LocalAuthenticator.create_system_users = True

# c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
# FirstUseAuthenticator.create_users = False

# c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
# c.DummyAuthenticator.password = "some_password"

# from jupyterhub.spawner import SimpleLocalProcessSpawner
# c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

# ## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']

c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']

c.DockerSpawner.debug = True

c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.Spawner.http_timeout = 180


# c.DockerSpawner.cmd = ""

# c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'

# # See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py

# # user data persistence
# # see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
# notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
# c.DockerSpawner.notebook_dir = notebook_dir
# c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# # Other stuff
# c.Spawner.cpu_limit = 1
# c.Spawner.mem_limit = '10G'

# ## Services
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]