# docker build
docker build -t test-api .

docker run -p 8000:8000 --name mycontname test-api