
### Setup Environement 
These steps assume that you have a git environment up and working.

1. Install the following python libraries in the same order
```
pip install dbt-core==1.4.8
pip install dbt-bigquery==1.5.3
pip install cookiecutter==2.4.0
```
2. execute `dbt --version`, you should see some output that starts with 
```
Core :
- Installed: 1.4.8
...
```

3. execute `cookiecutter --version`, you should see some output similar to :
```
Cookiecutter 2.4.0 from ...
```
