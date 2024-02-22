
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

exit 0

kubectl describe services/kubernetes-bootcamp

eval $(minikube docker-env)


export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

# curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME


# kubernetes-bootcamp-f95c5b745-44jfn



