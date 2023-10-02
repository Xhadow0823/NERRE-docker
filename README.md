# Before start this service
1. clone this repo
2. cd to this dir
3. prepare your open ai api key

# Start this service
1. Method1 - run with docker
  1. build this image
    `sudo docker build --tag NERRE .`
  2. then run with docker
    `sudo docker run -it --rm -p 5000:5000 -e OPENAI_API_KEY="xxxxx" --name my-nerre NERRE`
2. Method2 - build & run with docker-compose
  `echo OPENAI_API_KEY=xxxxx > .env && sudo docker compose up`

> Please replace all xxxxx with your open ai api key.

## misc
+ http://{url_of_your_location}:5000
