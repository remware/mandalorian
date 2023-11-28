# The Mandalorian (Bug Hunter)

This is a test for python + flask + mongo stack in web development

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install pymongo
```

## Run

```
flask run
```

Open browser and Go to localhost:5000
or 
* http://localhost:5000/test/2

## Test your app
in this sample we assume:
* a "mandalorian" db
* a "bug_hunter" collection
* a document format json as below <int32>,<string>,<string>
```
{
  "_id": 653,
  "content": "Hello",
  "template": "default"
}
```