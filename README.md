# DEX-aggregator-service

Docker   \
build:    \
docker build -t dexaggregator:latest .   \
run local:\
docker run -p 9000:8080 dexaggregator:latest    \

Push to ECR    \
export AWS_DEFAULT_PROFILE=personal \
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 579907623869.dkr.ecr.us-east-1.amazonaws.com  \
docker tag dexaggregator:latest 579907623869.dkr.ecr.us-east-1.amazonaws.com/dexaggregator:latest  \
docker push 579907623869.dkr.ecr.us-east-1.amazonaws.com/dexaggregator:latest

testing:
pytest test.py



