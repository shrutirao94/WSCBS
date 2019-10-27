# Assignment 1.2

1. Make sure you have python 3.7 and [pipenv](https://pipenv.readthedocs.io/en/latest/) installed
2. `cd` into the *url_shortner* directory and run pipenv install
3. export the `FLASK_APP` and `FLASK_ENVIRONMENT` env variables (this will depend on your os and shell). For example, on Linux/OSX and using bash/zsh you can run:

```
export FLASK_APP=url_shortner
export FLASK_ENVIRONMENT=development
```

You can consult [this page](http://flask.pocoo.org/docs/1.0/tutorial/factory/) for more information.

4. run `flask init-db` to initialize the database
5. run `sh seed.sh` to seed the database with sample data
6. `cd` to *assignment-1* directory (one level up) and run `flask run` to start the server
7. You can now interact with the server from a browser or a client of your choice (such as [postman](https://www.getpostman.com/) or good ol [curl](https://curl.haxx.se/docs/manual.html)). Consult the `client.sh` file for a few example scenarios.
