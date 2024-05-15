## How to setup
You will need to install [docker](https://docs.docker.com/engine/install/) on your machine

Once you have it installed and running, then you just run this command in the root of the project:
```
docker-compose up --build
```

Frontend: localhost:3000
Backend: localhost:8000

FastAPI has built in docs whic is nice: localhost:8000/docs

## Design Choices

For technologies, I opted to use FastAPI and React with Chackra UI as this is the tech stack that I am most familiar with.

I decided to build this with docker as well so its easier to spin up in another machine and not have to worry about installing dependencies

For the models, it was between BERT or GPT. I wasn't familiar with either but after doing a bit of research, BERT seemed like it was more suited for what I was looking for. 


The only part that I had difficulty with is returning a human readable text for our answers. After a bit of research, I couldn't find a quick answer to do this with BERT, so I just decided to return the unprocessed text because that was the closest I could get.




## Demo

