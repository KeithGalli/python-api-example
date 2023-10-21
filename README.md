# Building and deploying a Python API

### About

In this session we will build some API endpoints, documentation for those endpoints, and the ability to test on a live site deploying on render.com. This is a simple example to get started, but hopefully it will provide the foundation for you all to build more complex APIs in the future. If you have any questions, I recommend leaving them on the YouTube recording of the lunch & learn on Tina's channel.

### Setup

1. **Clone the repository**:
   ```bash
   git clone -b lunch-and-learn https://github.com/KeithGalli/python-api-example.git
   ```
2. **Navigate to directory**
   ```bash
   cd python-api-example
   ```
3. **Install Python libraries**
   ```bash
   pip install -r requirements.txt

4. **Run Flask Endpoint**
   ```bash
   python3 app.py
   ```

5. **Navigate to server** <br/>
   Open up URL app is running on (should say when you run above command -- http://127.0.0.1:5000 for example). Navigate to http://127.0.0.1:5000/apidocs to see Swagger endpoint specs.
