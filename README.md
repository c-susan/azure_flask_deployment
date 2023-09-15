# azure_flask_deployment
This repo is an introduction to Flask deployment using Microsoft Azure. Includes a step-by-step guide of how I set up the application and deployed it using Azure.

Azure Deployment URL: susan-504-flask.azurewebsites.net

# Setting Up the Application
**1.** Created a Github repository called ```azure_flask_deployment``` that contained a ```README.md file```. Cloned the repo in the Google Shell environement using the command ```git clone```. 

**2.** In the Shell start page, clicked **"Open Folder..."** to open up the cloned repo. 

**3.** Created a file and named it ```requirements.txt```. In the ```requirements.txt``` file, typed in ```pandas``` and ```flask```, each on different lines. 

**4.** Created a new folder called **data** and uploaded my dataset. 

**5.** Created a new file called ```app.py``` that contains the following code: 

```
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def aboutpage(): 
    return render_template('about.html')

df = pd.read_csv('https://raw.githubusercontent.com/c-susan/azure_flask_deployment/main/data/OPIOID_TREATMENT_PROGRAM_PROVIDERS_08282023.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
```


**6.** Created a new folder called **templates** that contains the following files: ```about.html```, ```base.html```, and ```data.html```.

**7.** The code in the ```about.html```, ```base.html```, and ```data.html``` files were taken from Professor Hants Williams ```WK2``` ```flaskapp_0``` file and edited according my the contents from my dataset. 

**8.** Pushed the repo back into Github using the following commands: ```git add .```, ```git commit -m'<message>'```, and ```git push```. 


# Deploying the Application Using Azure
**1.** In the Shell environment terminal at the bottom of the page, install the Azure CLI using the command ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```. 

**2.** To test that it is correctly installed, type ```az```. 

**3.** Next, type ```az login --use-device-code``` and following the directions from the output. 

**4.** To ensure the correct Azure subscription is enabled, type ```az account list --output table```. After the output is displayed, type ```az account set --subscription``` plus the subscription ID for the **Azure for Students** account. 

**5.** In the terminal, type ```az webapp up --name <app-name> --runtime PYTHON:3.9 --sku B1```. Replace the ```<app-name>``` with your app name and click enter. 

**6.** The terminal will show that the webapp does not exist and will create it for you. 

**7.** Go into into your Azure account, search for the resource **App Services**. Click into the webapp name that appears and click the link under **Default domain** to access your application. 




