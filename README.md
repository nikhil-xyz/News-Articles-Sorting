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

## Tools
- Data Link : https://www.kaggle.com/datasets/jacopoferretti/bbc-articles-dataset

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

## MongoDB for Data Storage and Retrieval

MongoDB is a NoSQL, document-oriented database. It stores data in flexible, JSON-like documents called BSON, making it suitable for handling data that doesn't fit well into traditional rows and columns.

### Connection Syntax

```
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```
### Data Storage Syntax

```
data_base = client[DB_NAME]
collection = data_base[COLLECTION_NAME]

rec = collection.insert_many(data)
```

### Data Retrieval Syntax

```
records = collection.find()
```

## Evaluation
These bars represent the proportion of correctly classified instances for each target category from testing data.

![Image](https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/flowcharts/accuracy_bar_plot.png)

**Confusion Matrix :** A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known. It visualizes the performance of a classification model by showing the counts of True Positives, True Negatives, False Positives, and False Negatives. Following confusion matrix contains predictions from the testing data.

![Image](https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/flowcharts/confusion_matrix.png)

## Performance Matrix
- **Accuracy:** Overall correctness of the model (total correct predictions / total predictions).
- **Precision:** Out of the positive predictions, how many were actually positive (true positives / (true positives + false positives)). Focuses on minimizing false positives.
- **Recall:** Out of the actual positives, how many were correctly predicted (true positives / (true positives + false negatives)). Focuses on minimizing false negatives.
- **F1-score:** Harmonic mean of precision and recall. Provides a balance between the two metrics.
Following bar chart shows the evaluation of testing data on different matrices. 

![Image](https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/flowcharts/model_performance_bar_plot.png)