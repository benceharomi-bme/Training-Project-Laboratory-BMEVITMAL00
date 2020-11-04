# Kubernetes

## Namespace
You can create a *namespace* by executing this command:
```
kubectl apply -f namespace/namespace.yaml
```

Check it out:
```
kubectl get namespace
```

Output:
```
NAME                STATUS   AGE
kube-system         Active   6d5h
kube-public         Active   6d5h
kube-node-lease     Active   6d5h
default             Active   6d5h
practice-session    Active   2m47s
```


## Pod
You can create a *pod* by executing this command:

```
kubectl apply -f pod/pod.yaml
```

Check it out:
```
kubectl get po --namespace practice-session
```

Output:
```
NAME        READY   STATUS    RESTARTS   AGE
nginx-pod   1/1     Running   0          2m49s
```


## Deployment
You can create a *deployment* by executing this command:
```
kubectl apply -f deployment/deployment.yaml
```

Check it out:
```
kubectl get deployment --namespace practice-session
```

Output:
```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           32s
```


## Service
You can create a *service* by executing this command:
```
kubectl apply -f service/service.yaml
```

Check it out:
```
kubectl get service --namespace practice-session
```

Output:
```
NAME                    TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
nginx-service-example   LoadBalancer   10.152.183.187   <pending>     80:32745/TCP   16s
```


## Cleanup
You can delete everything by executing this command:
```
kubectl delete namespace practice-session
```