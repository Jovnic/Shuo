# Assignment 1 - Bigram Model API

This FastAPI project implements a simple bigram-based text generator.

## Run Locally
# first open anaconda prompt and make sure you open docker
# use desktop or any folder 
cd Desktop  

git clone https://github.com/Jovnic/Shuo.git

# then
cd Shuo

# and use docker
docker build -t genai-api .
docker run -d -p 8000:8000 genai-api

# you can check on web
http://127.0.0.1:8000/docs