# Templates

## GET /templates
Get template by template_id, but if not provided, will return all templates instead. However, if key word is provieded as a string, it will return all templates that contains that string. Also, if both template_id and deployed_regions_required is specified in the request, the deployed regions should be returned as well.
### Request
#### Header
```
application/json
```

#### Params
```json
{
    (optional)"template_id" : SOME_OBJECT_ID,
    (optional)"key_word" : SOME_KEY_WORD,
    (optional)"deployed_regions_required" : True,
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

## POST /templates
Create a template. If template_id is specified, it will be used on creating a new version for that template.

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
    "origin_id" : "SOME_OBJECT_ID"
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

## POST /versions
Create a new version given origin_id
### Request
#### Header
```
application/json
```

#### Body
```json
{
    "origin_id" : "SOME_OBJECT_ID",
    "name": "name of version",
    "file": "file for this version",
    
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
    "origin_id" : SOME_OBJECT_ID,
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
```json
{
    "template_id" : SOME_OBJECT_ID,
    "region" : REGION_NAME
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






