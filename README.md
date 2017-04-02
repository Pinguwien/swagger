Swagger Example
=================

This is an example of how to use the connexion package from Zalando.
Connexion is a framework integrating Swagger (UI) and Flask.

This is mainly for internal / evaluation purposes, but you should feel free
to play around.

Necessary to get started:

0) Prerequisites / Virtualenv

  ```bash
  python3 -m venv v
  ```

  ```bash
  source env/bin/activate
  ```

1) Installation of requirements

The obligatory
```bash
pip install -r requirements.txt
```

2) Start the app

`python app.py` to start the app.

In the browser: `localhost:8000/participants` lists example data.

The Path for Swagger is `localhost:8000/ui`.

For a better experience install `swagger`via node.

```bash
npm install -g swagger
```

You have then two helpful commands at hand:
* `swagger docs` which opens the docs in your browser

* `swagger project edit` which opens an interactive editing session in your browser
