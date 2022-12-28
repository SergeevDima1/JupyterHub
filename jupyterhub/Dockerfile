FROM jupyterhub/jupyterhub

RUN pip install \
 dockerspawner \
 jupyterhub-firstuseauthenticator \
 jupyterhub-idle-culler 

COPY jupyterhub_config.py .
