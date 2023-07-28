# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S"
# )

def hello_world(app):
    print("Hello, World!")

def setup(app):
    app.connect("builder-inited", hello_world)