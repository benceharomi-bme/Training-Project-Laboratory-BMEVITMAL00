# Lab05
## Task
Create and build a docker image, which executes the given python program (`hello-count.py`) and save it to your own DockerHub account. From this image start a Kubernetes service where the replica number is 2. 

## Solution
### Docker image
Here is the `hello-count.py` program:
```
from flask import Flask, jsonify 
from multiprocessing import Value 

counter = Value('i', 0) 

app = Flask(__name__) 

@app.route('/') 

def index(): 
  with counter.get_lock():
    counter.value += 1
    out = counter.value 

  return jsonify(count=out)

app.run(host="0.0.0.0", port=int("8080"), debug=True) 
```
You also need to add `flask` to the `requirements.txt` file:
```
flask
```
The `Dockerfile`:
```
FROM python:3-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY hello-count.py .

EXPOSE 8080

ENTRYPOINT ["python3", "hello-count.py"]
```
Please mind that the `Dockerfile` the `hello-count.py` and the `requirements.txt` should be in the `src/docker` directory.

Make sure you are in the `src` directory then build the `docker image` from the `Dockerfile` with this command:
```
docker build -t counter ./docker
```
You can try out the freshly built docker image:
```
docker run --rm -p 8080:8080 --name counter counter
```
Open another terminal and execute:
```
curl -L localhost:8080
```
You should see this output:
```
{
  "count": 1
}
```
And if you execute it several times the counter should increase:
```
{
  "count": 2
}
```
If your output matched mine then you can upload it to your `DockerHub` account.

Login with your `DockerHub` `username`:
```
docker login --username=yourhubusername
```
Check the image ID of the `counter` using:
```
docker images
```
Output:
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
counter             latest              72daeda6204b        5 days ago          55.7MB
```
In my case the image ID is `72daeda6204b`

Tag the image:
```
docker tag 72daeda6204b yourusername/yourrepo:counter
```
Push your image to the repository you created:
```
docker push yourusername/yourrepo
```
Your image is now available for everyone to use.

### Deployment

Please mind that if you are using `microk8s` then the dns should be enabled which you can do by executing this command:
```
microk8s enable dns
```
Create the namespace:
```
kubectl apply -f kubernetes/namespace/namespace.yaml
```
Start the deployment:
```
kubectl apply -f kubernetes/deployment/deployment.yaml
```
Start the service:
```
kubectl apply -f kubernetes/service/service.yaml
```

Check out the port of the  service:
```
kubectl get service --namespace counter-namespace
```
You can see in the output below that in my case the port is `30697`:
```
NAME              TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
counter-service   LoadBalancer   10.152.183.30   <pending>     8080:30697/TCP   2m57s
```
Ping the port:
```
curl -L localhost:30697
```
The output should look like similar to this:
```
{
  "count": 276
}
```
