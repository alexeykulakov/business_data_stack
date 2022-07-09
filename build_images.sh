# docker build -t eidox/base ./base
# docker build -t aerofeev/spark ./spark
# docker build -t aerofeev/rstudio ./rstudio
# docker build -t eidox/jupyterlab ./jupyterlab
# docker build -t aerofeev/dremio ./dremio

docker build -t eidox/jupyterlab ./images/jupyterlab
docker build -t eidox/jupyterhub ./images/jupyterhub

docker build -t eidox/dagster_user_code_image -f ./images/dagster/Dockerfile_user_code ./images/dagster
docker build -t eidox/dagster -f ./images/dagster/Dockerfile_dagster ./images/dagster


