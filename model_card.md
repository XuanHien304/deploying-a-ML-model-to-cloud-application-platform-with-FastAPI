# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

- **Model Name**: Random Forest Classifier
- **Version**: 1.0
- **Author**: Vu Xuan Hien


## Intended Use

**Primary Use Case**:

The primary use case for this model is to assist in predicting individuals' income levels based on census features.

**Potential Users**:

- Data Analysts
- Data Scientists
- Charitable Organizations
- Marketing Teams
- Researchers

## Training Data

**Data Source**:

The model was trained on a dataset obtained from the UCI Machine Learning Repository. The dataset contains various demographic features such as age, education, marital status, etc., as well as the target variable indicating salary class (<=50k or >50k).

**Data Preprocessing**:

The training data underwent preprocessing steps that included handling missing values, encoding categorical features, and splitting the data into training and validation sets.
## Evaluation Data

The evaluation data is a subset of the same dataset used for training. It was reserved for model evaluation to assess its generalization performance.

## Metrics

The model was evaluated on the following metrics: Precision: 0.73. Recall: 0.64. Fbeta: 0.68.


## Ethical Considerations
- The dataset used for training and evaluation is anonymized and does not contain personally identifiable information (PII).

- Fairness considerations were made to ensure the model does not discriminate against any demographic group.
## Caveats and Recommendations
Consider incorporating additional features or external data sources to improve predictive accuracy