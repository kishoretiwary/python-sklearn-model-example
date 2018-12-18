#!/bin/bash
kubectl expose deployment wine-predict-demo-deployment --type=NodePort --name=wine-predict-demo-service
