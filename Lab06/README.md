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
Create the *namespace*:
```
kubectl apply -f src/kubernetes/namespace/namespace.yaml
```
Deploy the *services*:
```
kubectl apply -f src/kubernetes/services/
```
Deploy the *deployments*:
```
kubectl apply -f src/kubernetes/deployment/
```
```
kubectl get po -o wide -n voting-app-namespace
```
Output:
```
NAME                                 READY   STATUS             RESTARTS   AGE    IP             NODE     NOMINATED NODE   READINESS GATES
db-deployment-7d44bb9987-64h25       1/1     Running            0          150m   10.1.179.104   pop-os   <none>           <none>
result-deployment-5f4b86484f-htrng   1/1     Running            0          150m   10.1.179.117   pop-os   <none>           <none>
redis-deployment-67f9dd6bc6-2zb79    1/1     Running            0          150m   10.1.179.110   pop-os   <none>           <none>
vote-deployment-7ddb576d64-x75vb     1/1     Running            0          150m   10.1.179.115   pop-os   <none>           <none>
worker-deployment-65b859946c-t6d8r   0/1     CrashLoopBackOff   27         127m   10.1.179.125   pop-os   <none>           <none>
```
```
kubectl get service -n voting-app-namespace
```
```
NAME             TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
db-service       ClusterIP      10.152.183.113   <none>        5432/TCP       5h43m
redis-service    ClusterIP      10.152.183.36    <none>        6379/TCP       5h43m
result-service   LoadBalancer   10.152.183.98    <pending>     80:30560/TCP   5h43m
vote-service     LoadBalancer   10.152.183.147   <pending>     80:31699/TCP   5h43m
```
```
kubectl logs worker-deployment-65b859946c-t6d8r -n voting-app-namespace
```
Output:
```
System.AggregateException: One or more errors occurred. (Resource temporarily unavailable) ---> System.Net.Internals.SocketExceptionFactory+ExtendedSocketException: Resource temporarily unavailable
   at System.Net.Dns.InternalGetHostByName(String hostName, Boolean includeIPv6)
   at System.Net.Dns.ResolveCallback(Object context)
--- End of stack trace from previous location where exception was thrown ---
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Net.Dns.HostResolutionEndHelper(IAsyncResult asyncResult)
   at System.Net.Dns.EndGetHostAddresses(IAsyncResult asyncResult)
   at System.Net.Dns.<>c.<GetHostAddressesAsync>b__25_1(IAsyncResult asyncResult)
   at System.Threading.Tasks.TaskFactory`1.FromAsyncCoreLogic(IAsyncResult iar, Func`2 endFunction, Action`1 endAction, Task`1 promise, Boolean requiresSynchronization)
   --- End of inner exception stack trace ---
   at System.Threading.Tasks.Task`1.GetResultCore(Boolean waitCompletionNotification)
   at Npgsql.NpgsqlConnector.Connect(NpgsqlTimeout timeout)
   at Npgsql.NpgsqlConnector.RawOpen(NpgsqlTimeout timeout)
   at Npgsql.NpgsqlConnector.Open(NpgsqlTimeout timeout)
   at Npgsql.ConnectorPool.Allocate(NpgsqlConnection conn, NpgsqlTimeout timeout)
   at Npgsql.NpgsqlConnection.OpenInternal()
   at Worker.Program.OpenDbConnection(String connectionString) in /code/src/Worker/Program.cs:line 78
   at Worker.Program.Main(String[] args) in /code/src/Worker/Program.cs:line 19
---> (Inner Exception #0) System.Net.Internals.SocketExceptionFactory+ExtendedSocketException (0x00000001): Resource temporarily unavailable
   at System.Net.Dns.InternalGetHostByName(String hostName, Boolean includeIPv6)
   at System.Net.Dns.ResolveCallback(Object context)
--- End of stack trace from previous location where exception was thrown ---
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Net.Dns.HostResolutionEndHelper(IAsyncResult asyncResult)
   at System.Net.Dns.EndGetHostAddresses(IAsyncResult asyncResult)
   at System.Net.Dns.<>c.<GetHostAddressesAsync>b__25_1(IAsyncResult asyncResult)
   at System.Threading.Tasks.TaskFactory`1.FromAsyncCoreLogic(IAsyncResult iar, Func`2 endFunction, Action`1 endAction, Task`1 promise, Boolean requiresSynchronization)<---
```
