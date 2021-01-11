# Hawkeye: Image Search Engine - Web Interface

The web interface of Hawkeye had been developed with the use of the Django Framework, used to develop web applications with Python. In this repository the dataset and the index files were not uploaded.

To make the retrieval search engine tensorflow code run on a local machine it was necessary to install:
- Python 3.7.4
- Cuda 11.2  (https://developer.nvidia.com/cuda-downloads)
- Tensorflow 2.4 (pip install --upgrade tensorflow)
- Keras 2.4.3 (pip install --upgrade keras)

Usefull links: 
- Tensorflow setup: https://stephenjoel2k.medium.com/how-to-set-up-tensorflow-and-keras-on-your-local-system-using-pip-84b4d9f4475a
- Django tutorial by DjangoGirls : https://tutorial.djangogirls.org/it/django_start_project/

## Usage Example

The user will load a query picture in the search bar and the server will reply with a list of similar images retrieved from the food dataset (101 classes of food, 1000 images each).

![usage](./usage.gif)

