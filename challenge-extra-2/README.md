# Extra Challenge 2: Terraform

1. Bootstrap terraform
```shell
terraform init
```

2. Plan changes
```shell
terraform plan -out tfplan
```

3. Review changes (!)

4. Apply changes
```shell
terraform apply tfplan
```

5. For collaboration, before committing
```shell
terraform fmt -recursive .
```