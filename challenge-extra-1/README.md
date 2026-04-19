# Extra Challenge 1: Kubernetes

## Get all namespaces
```shell
kubectl get ns
# NAME                 STATUS   AGE
# collector            Active   68s
# default              Active   88s
# integration          Active   68s
# kube-node-lease      Active   88s
# kube-public          Active   88s
# kube-system          Active   88s
# local-path-storage   Active   84s
# monitoring           Active   68s
# orcrist              Active   68s
# tools                Active   68s
```

## Get all pods from all namespaces
```shell
kubectl get pods --all-namespaces
# NAMESPACE            NAME                                         READY   STATUS    RESTARTS   AGE
# integration          pod-example-integration                      1/1     Running   0          116s
# kube-system          coredns-7d764666f9-dwzxm                     1/1     Running   0          2m6s
# kube-system          coredns-7d764666f9-snff6                     1/1     Running   0          2m6s
# kube-system          etcd-kind-control-plane                      1/1     Running   0          2m15s
# kube-system          kindnet-hl4tp                                1/1     Running   0          2m6s
# kube-system          kube-apiserver-kind-control-plane            1/1     Running   0          2m15s
# kube-system          kube-controller-manager-kind-control-plane   1/1     Running   0          2m15s
# kube-system          kube-proxy-gwbq6                             1/1     Running   0          2m6s
# kube-system          kube-scheduler-kind-control-plane            1/1     Running   0          2m15s
# local-path-storage   local-path-provisioner-67b8995b4b-2f4mz      1/1     Running   0          2m6s
# monitoring           pod-example-monitoring                       1/1     Running   0          116s
# orcrist              nginx-deployment-59f86b59ff-7z87q            1/1     Running   0          116s
# orcrist              nginx-deployment-59f86b59ff-kqj5g            1/1     Running   0          116s
# orcrist              nginx-deployment-59f86b59ff-zpp5q            1/1     Running   0          116s
# orcrist              pod-example-orcrist                          1/1     Running   0          116s
# tools                pod-nginx-tools                              1/1     Running   0          116s
```

## Get all resources from all namespaces
```shell
kubectl get all --all-namespaces
# NAMESPACE            NAME                                             READY   STATUS    RESTARTS   AGE
# integration          pod/pod-example-integration                      1/1     Running   0          3m24s
# kube-system          pod/coredns-7d764666f9-dwzxm                     1/1     Running   0          3m34s
# kube-system          pod/coredns-7d764666f9-snff6                     1/1     Running   0          3m34s
# kube-system          pod/etcd-kind-control-plane                      1/1     Running   0          3m43s
# kube-system          pod/kindnet-hl4tp                                1/1     Running   0          3m34s
# kube-system          pod/kube-apiserver-kind-control-plane            1/1     Running   0          3m43s
# kube-system          pod/kube-controller-manager-kind-control-plane   1/1     Running   0          3m43s
# kube-system          pod/kube-proxy-gwbq6                             1/1     Running   0          3m34s
# kube-system          pod/kube-scheduler-kind-control-plane            1/1     Running   0          3m43s
# local-path-storage   pod/local-path-provisioner-67b8995b4b-2f4mz      1/1     Running   0          3m34s
# monitoring           pod/pod-example-monitoring                       1/1     Running   0          3m24s
# orcrist              pod/nginx-deployment-59f86b59ff-7z87q            1/1     Running   0          3m24s
# orcrist              pod/nginx-deployment-59f86b59ff-kqj5g            1/1     Running   0          3m24s
# orcrist              pod/nginx-deployment-59f86b59ff-zpp5q            1/1     Running   0          3m24s
# orcrist              pod/pod-example-orcrist                          1/1     Running   0          3m24s
# tools                pod/pod-nginx-tools                              1/1     Running   0          3m24s
# 
# NAMESPACE     NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
# default       service/kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP                  3m43s
# kube-system   service/kube-dns        ClusterIP   10.96.0.10     <none>        53/UDP,53/TCP,9153/TCP   3m42s
# orcrist       service/nginx-service   ClusterIP   10.96.247.73   <none>        80/TCP                   3m24s
# 
# NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
# kube-system   daemonset.apps/kindnet      1         1         1       1            1           kubernetes.io/os=linux   3m40s
# kube-system   daemonset.apps/kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   3m42s
# 
# NAMESPACE            NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
# kube-system          deployment.apps/coredns                  2/2     2            2           3m42s
# local-path-storage   deployment.apps/local-path-provisioner   1/1     1            1           3m40s
# orcrist              deployment.apps/nginx-deployment         3/3     3            3           3m24s
# 
# NAMESPACE            NAME                                                DESIRED   CURRENT   READY   AGE
# kube-system          replicaset.apps/coredns-7d764666f9                  2         2         2       3m34s
# local-path-storage   replicaset.apps/local-path-provisioner-67b8995b4b   1         1         1       3m34s
# orcrist              replicaset.apps/nginx-deployment-59f86b59ff         3         3         3       3m24s
```

## Get all services from namespace `orcrist`
```shell
kubectl -n orcrist get svc
# NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
# nginx-service   ClusterIP   10.96.247.73   <none>        80/TCP    4m43s
```

## Get all deployments from `tools`
```shell
kubectl -n tools get deploy
# No resources found in tools namespace.
```

## Get image from `nginx` deployment on `orcrist` namespace
```shell
kubectl -n orcrist get deployment/nginx-deployment -o jsonpath --template '{.spec.template.spec.containers[0].image}'
# nginx:latest
```

## Create a `port-forward` to access `nginx` pod on `orcrist` namespace
```shell
kubectl -n orcrist port-forward svc/nginx-service 8080:80
```