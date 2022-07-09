# FROM jupyterhub/jupyterhub:0.9.3
# FROM jupyterhub/jupyterhub:2.3.0
# FROM jupyterhub/jupyterhub:1.4.1
# FROM jupyterhub/jupyterhub:2.0.0
FROM eidox/base:latest

USER root

COPY jupyterhub_config.py .

# RUN pip install --upgrade pip

# RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

# RUN pip install flask_sqlalchemy
# RUN pip3 install flask_sqlalchemy

# RUN pip install dockerspawner
RUN pip install dockerspawner==0.10.0

# RUN pip install jupyterhub-dummyauthenticator
RUN pip install jupyterhub-nativeauthenticator

RUN apt-get update
RUN yes | apt-get install nodejs npm
RUN npm install -g configurable-http-proxy

# RUN pip install jupyterhub-firstuseauthenticator
# RUN pip install statsmodels --upgrade
# RUN pip install sqlalchemy --upgrade
# RUN jupyterhub upgrade-db

# oauthenticator==0.8.0 \
# jupyterhub-firstuseauthenticator \
# jupyterhub-nativeauthenticator \
# jupyterhub-dummyauthenticator

# RUN useradd -rm -d /home/akulakov -s /bin/bash -g root -G sudo -u 1001 -p jupyter akulakov
# USER akulakov
# WORKDIR /home/akulakov

