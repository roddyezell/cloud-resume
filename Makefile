.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec my-user --no-session -- sam deploy

deploy-site:
	aws-vault exec my-user --no-session -- aws s3 sync ./resume-site s3://www.roddyezell.com
	aws-vault exec my-user --no-session -- aws cloudfront create-invalidation --distribution-id E2Z5GMY6KXIHFU --paths "/*"