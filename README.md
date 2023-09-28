# build your image
1. cd to this dir
2. build with docker
`sudo docker build --tag NERRE .`

# start this service
1. run with docker
`sudo docker run -it --rm -p 5000:5000 -e OPENAI_API_KEY="xxxxx" --name my-nerre NERRE`

## misc
+ http://{nv5}:5000