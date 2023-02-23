# Countries Informer Service

Service to get up-to-date information about countries and cities.

## Requirements:

- docker
- git

## Installation

```shell
git clone https://github.com/Samoed/python-course-countries-informer
```
1. To configure the application copy `.env.sample` into `.env` file:
    ```shell
    cp .env.sample .env
    ```
   
    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values. 
    So it can be configured depending on the environment.

2. Build the container using Docker Compose:
    ```shell
    docker compose build
    ```
    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.
   
3. Now it is possible to run the project inside the Docker container:
    ```shell
    docker compose up
    ```
   When containers are up server starts at [http://0.0.0.0:8020](http://0.0.0.0:8020). You can open it in your browser.

## Usage
1. Run application:
    ```shell
    make run
    ```
2. Migrate database:
    ```shell
    make migrate
    ```
3. Create superuser:
    ```shell
    make create_super_user
    ```

## Automation commands
1. To run tests:
    ```shell
    make test
    ```


## Documentation
1. Swagger documentation
   When app running swagger will be at [http://0.0.0.0:8020/swagger](http://0.0.0.0:8020/swagger)
2. Documentation generation
    ```shell
    make docs-html
    ``` 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
