# Second Deployment Modeling
This project is intended to demonstrate a full ML Ops pipeline, though needing some manual intervention to change model versions.  
It is intended to enhance monitoring of a model to include not only a primary 'active' model but additional 'candidate' models that are run silently in the background.  Further, metrics will be created that take into account this active/background nature and assume that the active model is affecting outcomes that may be included in the retraining population.

## Approach
### Data
The [cifar100](https://huggingface.co/datasets/cifar100) data is being utilized, and will be incrementally exposed to models being evaluated and trained.  
Further the two-layer labeling will be used to simulate drift and side-effects of a primary model by a forced remapping of subgroups to coarse groups.

### Models
The data will be used as a classification problem, starting with a full multilabel problem, but eventually collapsing 1vsRest into a binary classifier scenario.  
The feature extractor and classifier 'google/vit-base-patch16-224-in21k' available from [huggingface](https://huggingface.co/google/vit-base-patch16-224-in21k) will be used as a starting point for the models. 

## Contents
### docs/
Documents for class deliverables - includes slides for homework wk 5

### eda/
Exploratory notebooks  
train_cifar_basic.ipynb - Run on google colab; first fine-tuning of model  
prediction_v0 - Testing script to load and predict with model trained elsewhere 

### models/
NOT COMMITED TO GITHUB - EXCEEDS LIMIT  
model0 - initial model, full multiclass image classifier 