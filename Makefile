TAMPLATENAME = template.yaml
STACKNAME = todo-app
BUCKETNAME = todo-template
CAPABILITYS = \
			CAPABILITY_IAM \
			CAPABILITY_NAMED_IAM \
			CAPABILITY_AUTO_EXPAND 


			
all:validate
all:build			
all:deploy

.PHONY: build validate deploy  
validate:
	sam validate --template-file $(TAMPLATENAME)
build:
	sam package --s3-bucket $(BUCKETNAME) 
	sam build --use-container

deploy:
	sam deploy --stack-name $(STACKNAME) --s3-bucket $(BUCKETNAME) --capabilities $(CAPABILITYS) --region eu-central-1 


	
	
	