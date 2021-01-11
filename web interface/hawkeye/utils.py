import shutil, os 
from hawkeye.index_creation import VP_Tree  
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras import layers as L
import PIL
from sklearn import preprocessing as sp
from IPython.display import display
from tensorflow.python.ops import image_ops
from tensorflow.python.ops import io_ops
from tensorflow.python.keras.preprocessing import dataset_utils

INDEX_PATH = './deployment/index_fine_tuned/index_fine_tuned.json'
QUERY_PATH = './media'   #guarda dove si salva la query
MODEL_PATH = "./deployment/food_classifier.h5"
K = 15

# Extract features
def feature_extractor(model,image):
  features = model.predict(image)
  return features

def preprocess(images, labels):
  images = tf.keras.applications.mobilenet_v2.preprocess_input(images)
  return images, labels

# Retrieve User Query Image

def load_image(path):
  print("Query: ")
  img_disp = PIL.Image.open(path)
  img_disp.thumbnail((224,224))

  image = io_ops.read_file(path)
  image = image_ops.decode_image(image, channels=3, expand_animations=False)
  image = image_ops.resize_images_v2(image, (224,224), method='bilinear')
  image.set_shape((224, 224, 3))
  image=image.numpy()
  image= tf.keras.applications.mobilenet_v2.preprocess_input(image)
  image=np.array([image])
  return image


def get_results(filename):
  #load index
  vp_tree_ft = VP_Tree.load_vptree(INDEX_PATH)

  #Loading Model
  food_classifier = tf.keras.models.load_model(MODEL_PATH)
  food_classifier = tf.keras.Model(inputs=food_classifier.input, outputs=food_classifier.get_layer('dense_hidden').output)

  #Find Results using OUR MODEL
  query_ft = load_image(QUERY_PATH+'/'+filename)
 
  query_f_ft = feature_extractor(food_classifier,query_ft)

  ids2,distances2 = vp_tree_ft.knn_search(K,query_f_ft)


  files = [id[0] for id in ids2]
  
  clean(filename)

  print('files: ',files)

  return  files

def clean(filename):
  #svuota la media directory
  for file in os.listdir(QUERY_PATH):
    if (file.endswith('.jpg') or file.endswith('.png') or file.endswith('.PNG') ) and file != filename :
      if os.path.exists(QUERY_PATH+'/'+file): 
        print(QUERY_PATH+'/'+file)
        os.remove(QUERY_PATH+'/'+ file)
  print('dir emptied')
  return
