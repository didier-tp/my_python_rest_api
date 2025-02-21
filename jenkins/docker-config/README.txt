sudo docker compose --profile python up -d
docker compose --profile python up -d
NB: avec le profil "python" , un seul agent est créé (en version python) et donc agent any est ok .

sudo docker compose --profile python down -v --remove-orphans
docker compose --profile python down -v --remove-orphans

-----------
NB: pour que l'on puisse déclencher une construction d'image docker depuis l'agent Jenkins python, il faut que son Dockerfile
comporte docker-ce (Inside debian) et comme en plus on se retrouve en mode "docker in docker" , il faut effectuer les réglages suivants:
* dans Dockerfile de l'agent Jenkins:

#ensures that /var/run/docker.sock exists & changes  ownership & gives jenkins user permissions to access /var/run/docker.sock
RUN touch /var/run/docker.sock &&\
	chown root:docker /var/run/docker.sock &&\
	usermod -a -G docker Jenkins

* dans le docker-compose.yaml
      volumes:
      - /var/run/docker.sock:/var/run/docker.sock

--------------
Rappel : pour debug de container :  docker container exec -ti xyz_container sh