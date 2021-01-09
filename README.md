# What is hawkeye?
Hawkeye is an image search engine developed for the Multimedia Information Retrieval and Computer Vision course of the MSc Artificial Intelligence and Data Engineering at Università di Pisa.

It is a search engine based on the query-by-example paradigm: a user submit an image, the search engine returns the most similar ones belonging to the image collection. It uses as index a Vantage Point Tree and the MobileNetV2 for feature extraction. We extract two times the features: first, using the un-modified MobileNetV2, then with a fine-tuned version. 

The fine-tuned model is in the `\model` directory. Each file contains a description of the step performed.

Project files:
- [Vantage Point Tree](./index_creation.ipynb)
- [Model fine-tuning](./model_fine_tuning.ipynb)
- [Feature Extraction](./feature_extraction.ipynb)
- [Performance Evaluation](./performance_evaluation.ipynb)
- [Search Engine](./Retrieval.ipynb)

# Credits

@thorongil05, @matildao-pane, @ragnar1002, @nooshinnr, @seraogianluca
