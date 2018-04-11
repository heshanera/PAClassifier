# PAClassifier

Online Passive Aggressive Binary Classifier

## Dataset

Wisconsin Breast Cancer Database (January 8, 1991)

O. L. Mangasarian, R. Setiono, and W.H. Wolberg: "Pattern recognition via linear programming: Theory and application to medical diagnosis", in: "Large-scale numerical optimization", Thomas F. Coleman and Yuying Li, editors, SIAM Publications, Philadelphia 1990, pp 22-30.

*2/3 of the data is used for training and 1/3 is used for testing.*

## Results

*Training Data Size: `466`*   

| Iterations  | Correct     | Incorrect   | Training    |
| :----------:|:-----------:|:-----------:|:-----------:|
| 1           | 256         | 210         | 54.94%      |
| 2           | 557         | 375         | 59.76%      |
| 10          | 3095        | 1565        | 66.42%      |



*Testing Data Size: `233`*

| Iterations    | Correct       | Incorrect | Accuracy  |
| :-----------: |:-------------:| :--------:| :--------:|
| 1             | 156           | 77        | 66.95%    |  
| 2             | 179           | 54        | 76.82%    |   
| 10            | 189           | 44        | 81.12%    |
