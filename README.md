# pokemons

# Installation
I use docker for run this project, but if don't want to use docker, i could recommend you to use virtualenv.

## Docker installation guide
If you choose run this project with docker, you have to do the steps below:

- Run `docker-compose run --rm --service-ports worker sh` in your terminal. Install gcc package often take a couple of minutes.
- Now, you are into woker container. Run `python manage.py migrate`
- Run `python manage.py loaddata stats.json`

## How to use it.
All below commands have to be run into docker container:

For example, create a pokemon: `python manage.py evolution-chain 6`.

If you can see the new pokemon created, you can go to: http://localhost:8000/pokemon/search-pokemon/charizard

### Warning
If you run this project on Windows, you have to check the correct port.