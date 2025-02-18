cd ..
#-p NUM_PORT_HOST:NUM_PORT_CONTAINER
docker container run --name devise_rest_api -p8088:8088 -d didierDefrance69/my_rest_api:1

#http://localhost:8088