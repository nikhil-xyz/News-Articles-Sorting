# News-Articles-Sorting

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