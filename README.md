
# AI Research Ambassador <img src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gifs/Hi.gif" width="30px">

Here's the link for the Flask + Javascript AI chatbot [https://virtualourambassador.herokuapp.com] 

![Alt text](images/virtualourambassador_demo.png?raw=true "Title")

## Theory

https://machinelearningmastery.com/gentle-introduction-bag-words-model

https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/mitkotak/virtualambassador.git
$ cd virtualourambassador
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Feel free to add more resposes to intents.jso

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```


## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs

This repo was used for the base version
https://github.com/python-engineer/chatbot-deployment
