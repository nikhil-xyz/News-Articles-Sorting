# News-Articles-Sorting
## Overview
With News companies having terabytes of data stored in
servers, everyone is in the quest to discover insights that add value to the organization.
With various examples to quote in which analytics is being used to drive actions, one that
stands out is news article classification. Nowadays on the Internet there are a lot of sources that generate immense amounts of
daily news. In addition, the demand for information by users has been growing
continuously, so it is crucial that the news is classified to allow users to access the
information of interest quickly and effectively. This way, the machine learning model for
automated news classification could be used to identify topics of untracked news and/or
make individual suggestions based on the user’s prior interests.

## Git Commands
```
git add .
git commit -m "message"
git push origin main
```

## Virtual Environmant Commands (Anaconda)
```
conda create -n <environament_name> python=<version> -y
conda activate <environament_name>
conda deactivate
```
## Evaluation
These bars represent the proportion of correctly classified instances for each target category.

![Image](https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/flowcharts/accuracy_bar_plot.png)

**Confusion Matrix :** A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known. It visualizes the performance of a classification model by showing the counts of True Positives, True Negatives, False Positives, and False Negatives.

![Image](https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/flowcharts/confusion_matrix.png)

## Performance Matrix
- **Accuracy:** Overall correctness of the model (total correct predictions / total predictions).
- **Precision:** Out of the positive predictions, how many were actually positive (true positives / (true positives + false positives)). Focuses on minimizing false positives.
- **Recall:** Out of the actual positives, how many were correctly predicted (true positives / (true positives + false negatives)). Focuses on minimizing false negatives.
- **F1-score:** Harmonic mean of precision and recall. Provides a balance between the two metrics.

![Image](https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/flowcharts/model_performance_bar_plot.png)