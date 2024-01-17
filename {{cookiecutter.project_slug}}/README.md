
IMPORTANT NOTE:

```
dbt debug
```
- If you want to run your models against the database connection specified in `profiles.yml`:
```
dbt run
```
- for specific model only, run 
``` 
dbt run --select <model-name-or-pattern>
```
- To check how the model data look like :

```
dbt show --select "<model_name>.sql"
```

for inline queries :

```
dbt show --inline "select * from {{ "{{" }} ref('model_name') {{ "}}" }} "
```

- Running tests :
```
dbt test
```
- Check for help
```
dbt --help
```
- Install dependencies, like helper macros or tests
    - add the packages to a file named `packages.yml`
    - run `dbt deps`
- See how your queries will be rendered before running against your database 
    - run `dbt compile`
    - check the `target` directory to see the generated sql files
