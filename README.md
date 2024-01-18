### Setup
If you have not already setup your environment, please follow the steps [here](docs/dbt-and-cookiecutter-setup.md)
### Usage


1. The following command will scafold a skiliton to a typical dbt project after getting some input from you.

2. On terminal, run the following command 
    ```
    cookiecutter https://github.com/sylndr/dbt-template.git 
    ```

3. A directory will be created as a result of the above step containing all scafolding files and folders. you can now open an editor and see what is there.

4. You can open a terminal and inside the created folder run the following:
    ```
    dbt debug
    ```
    This command should return Sucessfull output after checking the project structure and connectivity with the database you choosed.

5. Running project :
    ```
    dbt run
    ```
6. for specific model only, run :
    ```
    dbt run --select <model-name-or-pattern>
    ```

7. To check how the model data look like :

    ```
    dbt show --select "<model_name>.sql"
    ```

8. for inline queries :

    ```
    dbt show --inline "select * from {{ ref('model_name') }}"
    ```

9. Running tests :
    ```
        dbt test
    ```
10. Check for help
    ```
    dbt--help
    ```
11. Install dependencies, like helper macros or tests :
    ```
    - add the packages to a file named packages.yml
    - run `dbt deps``
    ```
12. See how your queries will be rendered before running against your database : 
    ```
    - run `dbt compile`
        
    - check the `target` directory to see the generated sql files
    ```

... Have fun
