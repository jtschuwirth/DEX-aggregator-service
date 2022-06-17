# DEX-aggregator-service

Docker\
build:\
docker build -t dexaggregator:latest .\
run local:\
docker run -p 9000:8080 dexaggregator:latest\

Push to ECR\
docker tag dexaggregator:latest 579907623869.dkr.ecr.us-east-1.amazonaws.com/dexaggregator:latest\
docker push 579907623869.dkr.ecr.us-east-1.amazonaws.com/dexaggregator:latest



