# Final_Master_Project
### Technology Requirements:
```
Anaconda-Navigator with Python 3.6
PostgreSQL
IDE, Atom
RasaX
Chatbot Widget
```


## Create a new environment in Anaconda-Navigator with the following command:
> <br> create -n rasa python=3.6 anaconda
## <br> Activate the environemt:
> conda activate rasa 
## Install Rasa through pip: 
> `pip install rasa-x --extra-index-url https://pypi.rasa.com/simple` 
## <br> Download file:
> <br> `git clone https://github.com/blueberrykary/Final_Master_Project` 
## To train model: 
> <br> rasa train
## Run the train program through the server and command line:
> rasa run actions & rasa shell 
## To run the program through the web broser, first start the rasa server and action server:
> rasa run -m models --enable-api --cors "*" --debug
## Once that is running, you can access the index.html directly. 

