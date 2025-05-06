---
source: https://deepwiki.com/scikit-learn/scikit-learn
update: 2025-05-07 00:31
---


scikit-learn 是一个强大的 Python 机器学习库，提供了各种监督和无监督学习算法，以及模型选择、预处理、评估等工具。

### 典型工作流程

在 scikit-learn 中进行机器学习项目的典型数据流包括以下步骤：

*   **数据预处理**：清理、缩放、规范化数据。
*   **特征工程**：创建新特征，处理分类变量。
*   **特征选择**：选择对模型最重要的特征。
*   **模型训练**：在训练数据上拟合模型。
*   **模型评估**：评估模型在未知数据上的性能。
*   **超参数调整**：寻找最优模型参数。

### 核心依赖项

Scikit-learn 的主要依赖项：

*   Python (≥3.10)
*   NumPy (≥1.22.0)
*   SciPy (≥1.8.0)
*   joblib (≥1.2.0)
*   threadpoolctl (≥3.1.0)

可选依赖项（用于特定功能）：

*   matplotlib (≥3.5.0)：可视化
*   pandas (≥1.4.0)：数据处理
*   scikit-image (≥0.19.0)：图像相关功能

### 核心模块概览

该库按功能分为不同的模块：

| 模块             | 描述                                       |
| :--------------- | :----------------------------------------- |
| `base.py`        | 核心基类 (`BaseEstimator`) 和混入类 (`ClassifierMixin` 等) |
| `utils/`         | 验证、检查和常用实用功能                     |
| `linear_model/`  | 线性回归、逻辑回归等线性模型                   |
| `ensemble/`      | 集成方法，如随机森林、梯度提升                 |
| `preprocessing/` | 数据缩放、编码等预处理工具                   |
| `metrics/`       | 各种机器学习任务的评估指标                   |
| `model_selection/`| 交叉验证和超参数调整工具                     |
| `cluster/`       | 聚类算法 (K-Means, DBSCAN 等)                 |
| `decomposition/` | 降维方法 (PCA, NMF 等)                       |
| `datasets/`      | 示例数据集和加载工具                         |

### 模型评估与选择

Scikit-learn 提供了全面的模型评估和选择工具。

#### 交叉验证

评估模型泛化能力的方法：

*   常用方法：`KFold`, `StratifiedKFold`, `TimeSeriesSplit` 等。
*   实用函数：`cross_val_score`, `cross_validate`。

#### 超参数调整

寻找最优模型参数的工具：

*   `GridSearchCV`：对指定参数网格进行详尽搜索。
*   `RandomizedSearchCV`：在参数空间中随机搜索。

#### 评估指标

用于衡量模型性能的函数：

*   **分类**：准确率 (Accuracy)、精确率 (Precision)、召回率 (Recall)、F1 分数 (F1-score)、ROC-AUC 等。
*   **回归**：均方误差 (MSE)、平均绝对误差 (MAE)、R² 分数 (R² score)、解释方差 (Explained Variance) 等。
*   **聚类**：调整兰德指数 (Adjusted Rand Index)、轮廓分数 (Silhouette Score) 等。

### 数据处理与特征工程最佳实践

*   始终在数据**拆分为训练集和测试集后**进行缩放，以避免数据泄漏。
*   **使用管道 (Pipeline)** 确保预处理步骤在训练和预测时一致。
*   在进行其他转换之前**妥善处理缺失值**。
*   在预处理之后、模型训练之前**选择特征**。
*   **评估不同预处理方法**对模型性能的影响。
*   选择预处理方法时**考虑领域知识**。
*   **记录**所做的预处理选择。

### 关键算法比较（分类）

下表比较了常见的分类算法及其特性：

| Algorithm                      | 训练时间复杂度                               | 预测时间复杂度                     | 内存占用 | 处理缺失值 | 处理分类特征 | 可解释性 |
| :----------------------------- | :------------------------------------------- | :--------------------------------- | :------- | :--------- | :----------- | :------- |
| LogisticRegression             | O(n\_samples × n\_features²)                 | O(n\_features)                     | 低       | 否         | 否           | 高       |
| RandomForestClassifier         | O(n\_estimators × n\_samples × log(n\_samples) × n\_features) | O(n\_estimators × log(n\_samples))  | 中等     | 否         | 否           | 中等     |
| GradientBoostingClassifier     | O(n\_estimators × n\_samples × log(n\_samples) × n\_features) | O(n\_estimators × log(n\_samples))  | 中等     | 否         | 否           | 中等     |
| HistGradientBoostingClassifier | O(n\_estimators × n\_samples × n\_features)  | O(n\_estimators × log(n\_bins))     | 中等     | 是         | 是           | 中等     |
| SVC                            | O(n\_samples² × n\_features)                 | O(n\_support\_vectors × n\_features) | 高       | 否         | 否           | 低       |
| GaussianNB                     | O(n\_samples × n\_features)                  | O(n\_classes × n\_features)         | 低       | 否         | 否           | 高       |



## 评估指标详情

这些指标用于量化模型在特定任务上的表现。

*   **分类指标**：适用于评估分类模型的性能。
    *   **准确率 (Accuracy)**：模型正确预测的样本占总样本的比例。它是最直观的指标，但对于类别不平衡的数据集可能具有误导性。
        *   计算公式：$(TP + TN) / (TP + TN + FP + FN)$
    *   **精确率 (Precision)**：在所有被模型预测为正类的样本中，实际为正类的比例。衡量模型避免误报（将负类错预测为正类）的能力。
        *   计算公式：$TP / (TP + FP)$
    *   **召回率 (Recall)**：在所有实际为正类的样本中，被模型正确预测为正类的比例。衡量模型找到所有正样本的能力。
        *   计算公式：$TP / (TP + FN)$
    *   **F1 分数 (F1-score)**：精确率和召回率的调和平均值。综合考虑了精确率和召回率，在两者都很重要时使用。
        *   计算公式：$2 \times (Precision \times Recall) / (Precision + Recall)$
    *   **ROC-AUC (Receiver Operating Characteristic - Area Under Curve)**：接收者操作特征曲线下面积。ROC 曲线描绘了在不同分类阈值下，真阳性率 (True Positive Rate, 召回率) 与假阳性率 (False Positive Rate, FP / (TN + FP)) 的关系。AUC 值越高，表示模型的区分能力越强。

*   **回归指标**：适用于评估回归模型的性能。
    *   **均方误差 (MSE)**：预测值与真实值之间差值的平方的平均值。对较大的误差惩罚更重。
        *   计算公式：$\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
    *   **平均绝对误差 (MAE)**：预测值与真实值之间差值的绝对值的平均值。它对异常值不如 MSE 敏感。
        *   计算公式：$\frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$
    *   **R² 分数 (R² score)**：也称为决定系数。衡量模型解释的方差比例。$R^2$ 分数接近 1 表示模型能很好地解释数据，接近 0 表示模型效果与简单平均值模型相当，小于 0 表示模型效果甚至不如简单平均值模型。
        *   计算公式：$1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$
    *   **解释方差 (Explained Variance)**：衡量模型预测值与真实值之间的差异是否能被模型解释。与 R² 相似，但计算方式略有不同，在某些情况下可能更有用。
        *   计算公式：$1 - \frac{Var(y - \hat{y})}{Var(y)}$

*   **聚类指标**：适用于评估聚类算法的性能。
    *   **调整兰德指数 (Adjusted Rand Index)**：衡量两个聚类划分之间相似度的指标，考虑了随机聚类的可能性。值域在 -1 到 1 之间，1 表示聚类结果完全一致，0 表示聚类结果与随机划分相似。需要已知真实标签才能计算。
    *   **轮廓分数 (Silhouette Score)**：评估聚类结果的紧密度和分离度。对于每个样本，计算其到同簇其他样本的平均距离 (a) 和到最近不同簇样本的平均距离 (b)。轮廓系数为 $(b - a) / \max(a, b)$。分数的平均值在 -1 到 1 之间，值越高表示聚类效果越好（簇内紧密，簇间分离）。不需要已知真实标签。

这些指标的选择取决于具体的机器学习任务和数据的特点。