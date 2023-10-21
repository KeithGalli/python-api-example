# Building and deploying a Python API

## About

In this session we will build some API endpoints, documentation for those endpoints, and the ability to test on a live site deploying on render.com. This is a simple example to get started, but hopefully it will provide the foundation for you all to build more complex APIs in the future. If you have any questions, I recommend leaving them on the YouTube recording of the lunch & learn on Tina's channel.

## Setup
1. **Fork the repository**:  
   Click on the 'Fork' button at the top right corner of the repository's GitHub page. This will create a copy of the repository in your own GitHub account.

2. **Clone your forked repository**:
   Make sure to replace YOUR_GITHUB_USERNAME with your username in this command
   ```bash
   git clone -b lunch-and-learn https://github.com/YOUR_GITHUB_USERNAME/python-api-example.git

3. **Navigate to directory**
   ```bash
   cd python-api-example
   ```
4. **Install Python libraries**
   ```bash
   pip install -r requirements.txt

5. **Run Flask Endpoint**
   ```bash
   python3 app.py
   ```

6. **Navigate to server** <br/>
   Open up URL app is running on (should say when you run above command -- http://127.0.0.1:5000 for example). Navigate to http://127.0.0.1:5000/apidocs to see Swagger endpoint specs.

7. **Making changes and pushing to your fork** <br/>
   After making your changes, you can push them to your forked GitHub repository.
   ```bash
   git add -u
   git commit -m "Your commit message"
   git push origin lunch-and-learn
   ```


## Render.com

We will be using [render.com](https://render.com) to deploy our app. Create an account there and connect your Github using the [following instructions](https://render.com/docs/github)

## Airtable

As a very simple and easy to set-up DB, we will be using airtable. I'll show in the live stream how to create an API token to use in Python API requests.
