# Istio Minikube Install 

## Start Minikube server 

```
minikube start --cpus 6 --memory 8192
```

## Install Istio in cluster 

```
istioctl install 
```

pods will be installed in istio-system namespace 
```
% kubectl get po -n istio-system
NAME                                    READY   STATUS    RESTARTS   AGE
istio-ingressgateway-74cb44d567-xxfvv   1/1     Running   0          7m43s
istiod-6685b8cbfc-ss592                 1/1     Running   0          8m43s
```

## Deploy Demo application 

- get demo application from https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/release/kubernetes-manifests.yaml
- download this file 
- apply it to the cluster 

```
% kubectl apply -f kubernetes-manifest.yaml
deployment.apps/emailservice created
service/emailservice created
deployment.apps/checkoutservice created
service/checkoutservice created
deployment.apps/recommendationservice created
service/recommendationservice created
deployment.apps/frontend created
service/frontend created
service/frontend-external created
deployment.apps/paymentservice created
service/paymentservice created
deployment.apps/productcatalogservice created
service/productcatalogservice created
deployment.apps/cartservice created
service/cartservice created
deployment.apps/loadgenerator created
deployment.apps/currencyservice created
service/currencyservice created
deployment.apps/shippingservice created
service/shippingservice created
deployment.apps/redis-cart created
service/redis-cart created
deployment.apps/adservice created
service/adservice created

```
