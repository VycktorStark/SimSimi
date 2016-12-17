 Artificial Intelegincia simsimi request via webapp for API.AI

## Instructions:
Open the `app.py` file and add your key and language, set the messages for errors and enter the number for the type of the ia in the parameters, here is an example below:

>> * Key = "jksd978ww787w878w4654w"

>> * lang = "pt"

>> * error_msg = ["SEU ARROMBADO FDP","POLICIA AQUI E SimSimi TEM UM CARA ME SAKEANDO SOCORU",'q foi', 'kié', 'oque vc q Comigo me deixa em paz poha!!!']

>> * typeIA = "2.3"

Then create an account at https://api.ai/ and follow the steps below

* Step 1

Sign up to Heroku (or sign in if you already have an account).

* Step 2
 
click 'Deploy to Heroku' button.

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


* Step 3

The Heroku site will open and you will be asked to fill in the name of the application. Enter the name of the application (choose any name) and click the 'Deploy for Free' button.

* Step 4

Create an API.AI agent and enable webhook:

>> * Click on Fulfillment in the left side menu

>> * Turn Webhook on

>> * Insert the link `https://[App Name].herokuapp.com/webhook` into the URL field

>> * Click ‘Save’.

For your own service, you may want to secure it with basic auth and/or headers (if you don’t want other people using your web hooks).

* Step 5

Create a fallback intent that matches the requests for artificial intelligence. The action should be set to `ApiSimsimi` . Make sure the 'Enable webhook for this intent' option in the 'Voice response' section is checked. In the 'Voice Response' field, define the response that will be displayed in the case of Web service errors.

* Step 6

Now you can test simsimi artificial intelligence requests on the test console API.AI

## In the returned JSON, the “fulfillment” object will look like this:

>>
`"fulfillment": {
"speech": "POLICIA AQUI E SimSimi TEM UM CARA ME SAKEANDO SOCORU",
"source": "ApiSimsimi",
"displayText": "POLICIA AQUI E SimSimi TEM UM CARA ME SAKEANDO SOCORU"
}`
