# Sentimental NLP

This repository contains a trained fastText model which preforms sentimental analysis on a product review, location review, etc. Specifically, given a review, the model labels the review as `positive` or `negative`.

### Some Examples

given `the food smells bad` the model returns `negative`
given `broke after 2 days` the model returns `negative`
given `best seller A++++++` the model returns `positive`

### Training data

The training data consisted of:

* 200,000 Amazon product review
* 200,000 eBay seller reviews
* 30,000 Google Maps place reviews

The source training data is not released as part of this repository.

## Install

Run the included `./install.sh` script which will download the model and install all dependencies. You can optionally install the deps in a virtualenv.

## Running

The included script, `./sentimental_nlp.py`, can read input from standard in or be ran as a webserver. Some examples:

* `echo "the product is bad" | ./sentimental_nlp.py` to read line delimited input from standard in.
* Run `./sentimental_nlp.py "server"` to start the webserver and then run `curl http://localhost:3000?review=bad` to use the server