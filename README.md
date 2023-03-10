<img href="https://img.shields.io/github/issues-pr-raw/cedricouellet/torn-stock-helper">
<img href="https://img.shields.io/github/issues-raw/cedricouellet/torn-stock-helper">
<img href="https://img.shields.io/github/last-commit/cedricouellet/torn-stock-helper/main?label=last%20commit%20%28branch%3Dmain%29">
<img href="https://img.shields.io/github/last-commit/cedricouellet/torn-stock-helper/dev?label=last%20commit%20%28branch%3Ddev%29">
<img href="https://img.shields.io/github/v/tag/cedricouellet/torn-stock-helper?include_prereleases&sort=semver">
<img href="https://img.shields.io/github/v/release/cedricouellet/torn-stock-helper?display_name=tag&include_prereleases">

# torn-stock-helper

A Torn stock market helper application

## Built With

- [Docker](https://www.docker.com/) (Container management system)
- [Flask](https://flask.palletsprojects.com/) (REST API framework)
- [SQLAlchemy](https://www.sqlalchemy.org/) (Database ORM)
- [MySQL](https://www.mysql.com/) (Database system)
- [phpMyAdmin](https://www.phpmyadmin.net/) (Database admin web interface)
- [React.js](https://reactjs.org/) (Web client)


## Installation

### Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose V1](https://docs.docker.com/compose/)

### Procedure

1. Copy `.example.env` and to `.env`, and fill out sensitive entries.

    **Important:** do not add `.env` file to Git. It is in `.gitignore` by default so this shouldn't happen normally.

2. Run the following command within the project root directory

    Attach output to console:
    ```bash
    docker-compose up
    ```
    Detach output from console:
    ```bash
    docker-compose up -d
    ```

The following services will be accessible by the following URLs:
    
- REST API: `http://localhost:{FLASK_RUN_PORT}` (see `.env` for `FLASK_RUN_PORT`)
- phpMyAdmin: `http://localhost:{PMA_PORT}` (see `.env` for `PMA_PORT`)
    - username: `DB_USER` entry in `.env`
    - password: `DB_PASS` entry in `.env`

**To shut down container instances**

Run the following command within the project root directory

```bash
docker-compose down
```

## Contributing

Pull requests are welcome. 
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to follow preceding code and naming conventions.

## README TODO
- Add installation procedure for web client