import os
import sys

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.JupyterHub.services = [ 
    { 
        'name': 'idle-culler', 
        'admin': True, 
        'command': [ 
        sys.executable, 
        '-m', 'jupyterhub_idle_culler', 
        '--timeout=1000',
        ], 
    } 
] 
from firstuseauthenticator import FirstUseAuthenticator
c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
c.Authenticator.admin_users = { 'admin' } 

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {'jupyterhub-user-{username}': notebook_dir , 'jupyterhub-shared': '/home/jovyan/shared'}

c.Spawner.default_url = '/lab' 
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '2G'
c.Authenticator.min_password_length = 5

