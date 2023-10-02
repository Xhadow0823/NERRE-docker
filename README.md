# build your image
1. cd to this dir
2. build with docker
`sudo docker build --tag NERRE .`

# start this service
1. Method1 - run with docker
`sudo docker run -it --rm -p 5000:5000 -e OPENAI_API_KEY="xxxxx" --name my-nerre NERRE`
2. Method2 - run with docker-compose
`echo OPENAI_API_KEY=xxxxx > .env && sudo docker compose up`

## misc
+ http://{url_of_your_location}:5000