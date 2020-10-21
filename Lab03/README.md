# Kubernetes
## Ping
Using the `microk8s` start 2 pods with 1 container in each. From the inside of one of the containers ping the other pod's container (mind that you sould know the pod's
IP address what you can easily find out by executing the `ip a` command inside the pod or just by running the `kubectl describe po my-pod` where the
*my-pod* is the name of your pod).  
## Installing microk8s
Install the microk8s claster by running this command:
```
sudo snap install microk8s --classic --channel=1.19
```
Add your user to the group of microk8s to easily use the `microk8s` command:
```
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
su - $USER
```
You can find the official microk8s docs [here](https://microk8s.io/docs).
## Starting the pods
Start 2 pods:
```
microk8s kubectl run my-box -i --rm --image=busybox --restart=Never &
microk8s kubectl run my-box-2 -i --rm --image=busybox --restart=Never &
```
*Explaination of the flags:*
 * *the `i` flag keeps the STDIN open even if running in detached mode*
 * *the `--rm` means that after the container exits it should be removed*
 * *with the `--image=busybox` the wanted image can be set, in this case `busybox`*
 * *the `--restart=NEVER` means that the container will not be restarted regardless of why it exited*
 * *and lastly the `&` means that we would like to detach the container*

You can check out the pods:
```
microk8s kubectl get po
```
You can see that they are running:
```
NAME       READY   STATUS    RESTARTS   AGE
my-box     1/1     Running   0          32m
my-box-2   1/1     Running   0          10m
## Ping
```
Use the `-o widw` to see more details about them:
```
microk8s kubectl get po -o wide
```
Check out the IP address of the `my-box-2`:
```
NAME       READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
my-box     1/1     Running   0          23m   10.1.179.74   pop-os   <none>           <none>
my-box-2   1/1     Running   0          24s   10.1.179.75   pop-os   <none>           <none>
```
In my case: `10.1.179.75`


Connect in iteractive mode to `my-box`:
```
microk8s kubectl exec -it my-box -- sh
```
Ping `my-box-2` from `my-box`:
```
ping 10.1.179.75
```
You should see that ping is working from the output:
```
PING 10.1.179.75 (10.1.179.75): 56 data bytes
64 bytes from 10.1.179.75: seq=0 ttl=63 time=0.345 ms
64 bytes from 10.1.179.75: seq=1 ttl=63 time=0.184 ms
64 bytes from 10.1.179.75: seq=2 ttl=63 time=0.171 ms
64 bytes from 10.1.179.75: seq=3 ttl=63 time=0.147 ms
```

## Deleting the pods
Check out the name of the node where is your pod you want delete:
```
microk8s kubectl get nodes
```
Mark the node as unschedulable:
```
microk8s kubectl cordon my-node
```
*Where `my-node` is the name of the node.*

For deleting a pod just execute:
```
microk8s kubectl delete pod --wait=false my-box
```
*Where the `my-box` is the name of the pod you want to delete and the `--force` flag is setting to delete the pod immediately.*

Uncordon the node:
```
microk8s kubectl uncordon my-node
```
*Where `my-node` is the name of the node.*
