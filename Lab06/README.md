# Lab06
## Task
Create a voting-app
## Solution
### Docker images
Build the *result*, *vote* and *worker* images and upload them to your DockerHub account.
Make sure you are in the src directory
```
docker build -t ./docker/result .
```
```
docker build -t ./docker/vote .
```
```
docker build -t ./docker/worker .
```
Login with your DockerHub username:
```
docker login --username=your-hub-username
```
```
docker images
```
Output:
```
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
worker                    latest              e58182c1d5ee        7 days ago          1.72GB
vote                      latest              8b22d3b27103        7 days ago          84.2MB
result                    latest              0ce18fe6db28        7 days ago          146MB
```
Tag the images:
```
docker tag e58182c1d5ee your-username/your-repo:worker
docker tag 8b22d3b27103 your-username/your-repo:vote
docker tag 0ce18fe6db28 your-username/your-repo:result
```
Push your images to the repository you created:
```
docker push your-username/your-repo
```
### Deployment
There are 2 possible solutions, a five-pod and a three-pod solution. Firstly I'm gonna show the five-pod solution.
#### Five-pod solution
In this solution every container placed in a pod on it's own.

First of all create the *namespace*:
```
kubectl apply -f src/kubernetes/five-pod-solution/namespace/namespace.yaml
```
Deploy the *services*:
```
kubectl apply -f src/kubernetes/five-pod-solution/service/
```
Deploy the *deployments*:
```
kubectl apply -f src/kubernetes/five-pod-solution/deployment/
```
List the pods:
```
kubectl get po -o wide -n voting-app
```
Output:
```
NAME                      READY   STATUS    RESTARTS   AGE
db-77464d4957-vv982       1/1     Running   0          24s
redis-fd7cc6786-k5nd6     1/1     Running   0          24s
result-75b8bd76b7-rwdfm   1/1     Running   0          24s
vote-79cc99d9d6-4rnq2     1/1     Running   0          24s
worker-9fc48559c-vp4bj    1/1     Running   0          24s
```
Everything up and running.
List the services:
```
kubectl get svc -n voting-app
```
Output:
```
NAME     TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
db       ClusterIP      10.108.189.193   <none>        5432/TCP       69s
redis    ClusterIP      10.103.187.97    <none>        6379/TCP       69s
result   LoadBalancer   10.100.249.233   <pending>     80:32050/TCP   69s
vote     LoadBalancer   10.110.111.254   <pending>     80:31907/TCP   69s
```
Find the port of the *vote*. In my case it's `31907` check out `localhost:31907` in your browser and vote.
I'm using lynx because I'm accessing the server through a jump server and cannot access the server's IP address remotely.
```
lynx localhost:31907
```
Output:
```
Cats vs Dogs!

   (a) Cats (b) Dogs
   (Tip: you can change your vote)
   Processed by container ID vote-79cc99d9d6-4rnq2

```
You can also check out the results if you use the port of the `result` pod which is `32050`
```
lynx localhost:3250
```
Output:
```
   Cats
   {{aPercent | number:1}}%
   Dogs
   {{bPercent | number:1}}%

   No votes yet {{total}} vote {{total}} votes
```
Unfortunately with *lynx* the results cannot be checked so I have to see the database if the records are stored.
The database's IP address is `10.108.189.193` and the port is `5432` and I am using psql to connect to it.
```
psql postgres://postgres:postgres@10.108.189.193:5432/postgres
```
List relations with the `\d` command to find out what is the name of the table where the votes stored.
```
postgres=# \d
```
Output:
```
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | votes | table | postgres
(1 row)
```
Surprisingly the votes are stored in the `votes` table. :)

List the records of the *votes* table:
```
postgres=# select * from votes;
```
Output:
```
        id        | vote 
------------------+------
 a1b06a7af5a8093a | a
(1 row)
```
And there is a record which means that the vote succesfully stored in the database.

#### Five-pod solution

