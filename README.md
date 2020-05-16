# cosibot-germany-turkish

This is the starter for the  Cosibot Germany in Turkish


## Requirements

The chatbot is implemented using the open source machine learning framework Rasa.
You will need Rasa and spaCy. For installation instructions see:
https://rasa.com/docs/rasa/user-guide/installation/ and https://spacy.io/usage.

Cosibot Germany in turkish uses pre-trained turkish word vectors, trained on Common Crawl and Wikipedia using fastText. (see https://fasttext.cc/docs/en/crawl-vectors.html)
You will need to integrate this to your spaCy installation to be able to include it into the Rasa pipeline (see `bot/config.yml`).
For the integration execute the following commands:

Download the fasttext word vectors:

`wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.tr.300.vec.gz`

Create a spaCy language model based on turkish base model combined with fasttext vectors and a spaCy package for this model.
The spaCy package can be then installed via pip.

```
python -m spacy init-model tr tr_vectors --vectors-loc cc.tr.300.vec.gz
python -m spacy package tr_vectors .
tar zcvf tr_model-0.0.0.tar.gz tr_model-0.0.0
pip install tr_model-0.0.0.tar.gz
```

Optionally if you want to link the this model with 'tr' short name use the following:

`python -m spacy link --force tr_model tr`
