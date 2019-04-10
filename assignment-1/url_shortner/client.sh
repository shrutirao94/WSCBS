#!/usr/bin/env sh

# following are a few sample requests that can be made to the url_shortner
# service, we tried to cover as many (edge) cases as we could think of. A few
# things to note:
# 1. run `sh seed.sh` before running the following commands
# 2. replace the <:placeholder> where necessary
# 3. you can copy the command that you would like to run and execute it from the
# shell, alternatively you can comment out the commands except the one you would
# like to test, and execute this file with `sh client.sh` from the shell.
# if you want to inspect only the header of the response, use the -X flag,
# consult the curl man page for more info.

#
# /
#

# / GET
# returns a json response containing all urls in the database
# curl -X "GET" "http://127.0.0.1:5000/"

# / DELETE
# deletes all rows of the database, returns a 204 status code
# curl -X "DELETE" "http://127.0.0.1:5000/"

# / POST (params: url)
# creates a new entry in the database with the given url
# returns a 400 if no url is given or if url is invalid (a url is considered
# valid if it starts with any of `https`, `http` or `ftp`, check the `valid_url`
# method definition in shortner.py for more info)
# returns a 200 status code and the shortened url otherwise

# no param url given, throws a 400
# curl -X "POST" "http://127.0.0.1:5000/"

# invalid url given, throws a 400
# curl -X "POST" --data url=ptth://www.google.ca "http://127.0.0.1:5000/"

# valid url given, returns a 200
# curl -X "POST" --data url=https://www.valid.url "http://127.0.0.1:5000/"

#
# /<:url_short>
#

# /<:url_short> GET
# redirects to the full url, returns a 301
# if <:url_short> is invalid, returns a 400
# you can get a <:url_short> by visiting the root url (`/`) in the browser
# curl -X "GET" "http://127.0.0.1:5000/<:url_short>"

# /<:url_short> DELETE
# deletes the given url from the db, returns a 204
# returns a 404 if <:url_short> is invalid
# curl -X "DELETE" "http://127.0.0.1:5000/<:url_short>"

# invalid <:url_short>, returns a 404
# curl -X "DELETE" "http://127.0.0.1:5000/random"

# /<:url_short> PUT (params: url)
# updates the given <:url_short> with the provided url
# returns a 400 if no url is given or if url is invalid
# returns a 404 if <:url_short> is invalid
# returns a 200 status code otherwise

# no url given, throws a 400
# curl -X "PUT" "http://127.0.0.1:5000/<:url_short>"

# invalid url given, throws a 400
# curl -X "PUT" --data url=www.invalid.nl "http://127.0.0.1:5000/<:url_short>"

# <:url_short> does not exist, throws a 404
# curl -I -X "PUT" --data url=http://www.new-url.nl "http://127.0.0.1:5000/random"

# everything okay, returns 200
# curl -X "PUT" --data url=http://www.valid.com "http://127.0.0.1:5000/<:url_short>"
