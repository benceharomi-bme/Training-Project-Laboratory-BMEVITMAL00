# Kubernetes
## The task
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

From now on if you are using *microk8s* you should type `microk8s` before every `kubectl` command, like this:
```
microk8s kubectl some_command
```
## Starting the pods
Start 2 pods:
```
kubectl run my-box -i --image=busybox --restart=Never &
kubectl run my-box-2 -i --image=busybox --restart=Never &
```
*Explaination of the flags:*
 * *the `i` flag keeps the STDIN open even if running in detached mode*
 * *with the `--image=busybox` the wanted image can be set, in this case `busybox`*
 * *the `--restart=NEVER` means that the container will not be restarted regardless of why it exited*
 * *and lastly the `&` means that we would like to detach the container*

You can check out the pods:
```
kubectl get po
```
You can see that they are running:
```
NAME       READY   STATUS    RESTARTS   AGE
my-box     1/1     Running   0          32m
my-box-2   1/1     Running   0          10m
```
## Ping
Use the `-o wide` to see more details about them:
```
kubectl get po -o wide
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
kubectl exec -it my-box -- sh
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

## Cleaning up
For deleting a pod just execute:
```
kubectl delete pod my-box
```

## Other useful things
[kubectl cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/?fbclid=IwAR08mgxaLWgP4IMXFPvFtZ_6zKH5goSw6UE2Bzzcpm0q85Ia9AZ4x9Fh03k)
