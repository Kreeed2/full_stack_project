# JobApplicationTask

## Folder Structure

```txt
 |-- server: Python server backend  
 |-- ui: Angular frontend
 |-- tests: Unit tests for the python server
 | setup.py: Python dependencies
```

## Prerequisites

1.  Make sure **Python 3.8.x** is installed and added to your PATH environment variable
2.  Make sure **NodeJS Version 14.x.x LTS** with **npm** is installed
3.  Install tox (globally into your Python distribution) using pip

## Setup environments

### Python enviromnent

To setup the python dev environment run the following command:

```shell
tox -e dev
```

### Angular enviromnent

To setup the angular environment run the following command:

```shell
npm i
```

## Development

### Server

Start the python server by running the `npm run start:server` command.

### UI

Run `npm run start:ui` for a dev server. Navigate to `http://localhost:3333/`. The app will automatically reload if you change any of the source files.

## Additional commands

```sh
npm run test:server
npm run test:ui
npm run lint:server
npm run lint:ui
```
