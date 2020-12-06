# pyconf
This repo is for the pyconf influx demo

# Create civo k3s cluster 
 - Join the kube100 program from [here](https://www.civo.com/?ref=53e176)
 - Create a cluster via UI or cli
 - Download the cli from [here](https://github.com/civo/cli)
 ```
civo k3s create --wait --save --switch        

 ```
 
 - Clone the repository 
 - Deploy the manifests from deploy folder
 
 
 # Create the secret and config map used in the deployment(Can be automated as well)
```
kubectl create configmap host --from-literal=host="influxdb.{clusterID}.k8s.civo.com"
kubectl create secret generic influx --from-literal=token="{token from the UI}"

```
