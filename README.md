## Instructions:
Open the `config.py` file and to configure it, you will add your keys and add the other information as requested - follow the example below:

------------
<table><thead>
<tr><td><strong>Parameters</strong></td><td><strong>Type</strong></td><td><strong>Required</strong></td></tr>
</thead><tbody>
    <tr><td>timeout</td><td>Integer</td><td>Yes</td></tr>
    <tr><td>debug</td><td>True or False</td><td>Yes</td></tr>
    <tr><td>source</td><td>String</td><td>Optional</td></tr>
    <tr><td>key</td><td>String and Integer</td><td>Yes</td>
    <tr><td>lang</td><td>String</td><td>Yes</td></tr>
    <tr><td>typeIA</td><td>Integer</td><td>Yes</td></tr></tr>
</table>
------------

Then create an account at https://api.ai/ and follow the steps below

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


* Step 3

The Heroku site will open and you will be asked to fill in the name of the application. Enter the name of the application (choose any name) and click the 'Deploy for Free' button.


* Step 4

Create an API.AI agent and enable webhook:

 - Click on Fulfillment in the left side menu

 - Turn Webhook on

 - Insert the link `https://[App Name].herokuapp.com/webhook` into the URL field

 - Click ‘Save’.

 ------------

![Print-exemplo01](http://i.imgur.com/fTL2RgE.png)

------------

For your own service, you may want to secure it with basic auth and/or headers (if you don’t want other people using your web hooks).

* Step 5

Create a return intent that matches your artificial intelligence requests. The action should be set to `ApiSimsimi`, make sure the 'Enable webhook for this intent' option in the 'Fulfillment' section is checked. And the 'Text response' field, define the response that will be displayed in case of web service errors, do the same for the other function, but define the action of each as defined in the 'app.py' file

* Step 6

Now you can test simsimi artificial intelligence requests on the test console API.AI

## In the returned JSON, the “fulfillment” object will look like this:
```bash
{
  "id": "2j3nb2obh3ob2o3bo2-b3olkn2lk3n2",
  "timestamp": "2017-01-05T22:52:17.269Z",
  "result": {
    "source": "agent",
    "resolvedQuery": "simsimi",
    "action": "ApiSimsimi",
    "actionIncomplete": false,
    "parameters": {
      "any": "simsimi"
    },
    "contexts": [],
    "metadata": {
      "intentId": "j2bn3oj-kb2j3blj2bn3ljb2ljk3bjkl",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "true",
      "intentName": "IA"
    },
    "fulfillment": {
      "speech": "oi vagabundo\n\n",
      "source": "SimSimi",
      "messages": [
        {
          "type": 0,
          "speech": "oi vagabundo?\n\n"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "21hkj12bh3kjb1k3bb23bk-jb2jk3b"
}
```
