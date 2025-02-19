cd ..
docker build -t my_rest_api:1 .
docker tag my_rest_api:1 didierdefrance69/my_rest_api:1

#docker login -u didierdefrance69 (with password D.....F!)
#docker push didierdefrance69/my_rest_api:1



#docker image rm didierdefrance69/my_rest_api:1
#docker image rm my_rest_api:1
#docker pull didierdefrance69/my_rest_api:1