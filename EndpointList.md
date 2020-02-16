# Templates

## GET /templates
Get template by template_id, but if not provided, will return all templates instead
### Request
#### Header
```
application/json
```

#### Params
```json
{
    "template_id" : SOME_OBJECT_ID
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    templates[]
}
```

## PUT /templates
Create a tempalte. If template_id is specified, it will be used on creating a new version for that template.

### Request
#### Header
```
application/x-www-form-urlencoded
```
#### Body
```json
{
    "file" : [file object],
    "name" : "Template-A",
    "description" : "This is a demo template",
    "Tags" : ["TypeA","TypeB"],
    (optional)"template_id" : SOME_OBJECT_ID
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    "message" : "success"
}
```




## POST /templates
search template by name

### Request
#### Header
```
application/json
```
#### Body
```json
{
    "key" : "Tem"
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    "result" : templates[]
}
```








# Versions

## GET /versions
Get versions of a template by template id. It has to be provided
### Request
#### Header
```
application/json
```

#### Body
```json
{
    "template_id" : SOME_OBJECT_ID
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    templates[]
}
```





## PUT /versions
Activate a specific version of a template
### Request
#### Header
```
application/json
```

#### Body
```json
{
    "template_id" : SOME_OBJECT_ID,
    "version_id" : SOME_OBJECT_ID,
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    "message" : "success"
}
```




## DELETE /versions
Delete a specific version of a template
### Request
#### Header
```
application/json
```

#### Body
```json
{
    "template_id" : SOME_OBJECT_ID,
    "version_id" : SOME_OBJECT_ID,
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    "message" : "success"
}
```




# Deployment Jobs

## PUT /jobs
Create a deployment job
### Request
#### Header
```
application/json
```

#### Body
{
    "template_id" : SOME_OBJECT_ID
    "region" : REGION_NAME
}

### Response
#### Header
```
application/json
```
#### Body
```json
{
    "message" : "success"
}
```







## GET /jobs
Get all deployment jobs. If job is specified in the params, will return a specific job detail.
### Request
#### Header
```
application/json
```

#### Param
```json
{
    "job_id" : SOME_OBJECT_ID
}
```

### Response
#### Header
```
application/json
```
#### Body
```json
{
    deployment_jobs[]
}
```






## DELETE /jobs
Revoke an ongoing deployment jobs
### Request
#### Header
```
application/json
```

#### Body
```json
{
    "job_id" : SOME_OBJECT_ID
}
```
### Response
#### Header
```
application/json
```
#### Body
```json
{
    "message" : "success"
}
```






