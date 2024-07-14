[2.1. 数据操作 — 动手学深度学习 2.0.0 documentation (d2l.ai)](https://zh.d2l.ai/chapter_preliminaries/ndarray.html)

略去引言
#  预备知识 (暂略)
## 数据预处理

## 线性代数

## 微积分

## 自动微分

## 概率

## 查阅文档 (略)



# 3.线性神经网络

# 从线性回归到深度网络

![image](https://img2024.cnblogs.com/blog/488941/202401/488941-20240126111643202-665478434.png)

线性回归是一个单层神经网络

对于线性回归，每个输入都与每个输出（在本例中只有一个输出）相连， 称为全连接层（fully-connected layer）或称为稠密层（dense layer）。

3.1.5 小结

- 机器学习模型中的关键要素是训练数据、损失函数、优化算法，还有模型本身。
- 矢量化使数学表达上更简洁，同时运行的更快。
- **最小化目标函数和执行极大似然估计等价。** 
- 线性回归模型也是一个简单的神经网络。



打乱数据集中的样本并以小批量方式获取数据
```python
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = np.array(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]
```


```python
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        with autograd.record():
            l = loss(net(X, w, b), y)  # X和y的小批量损失
        # 计算l关于[w,b]的梯度
        l.backward()
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    train_l = loss(net(features, w, b), labels)
    print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
```
X：表示输入特征。在这个例子中，X 是一个小批量的输入样本，它包含了特征值，例如图片中的像素、文本中的单词表示等。每一行代表一个样本，每一列代表一个特征。

w 和 b：是模型的参数。在这个例子中，w 是权重（weights），b 是偏置（bias）。它们是模型通过训练学到的参数，用于将输入特征映射到输出。

y：是标签，代表模型应该预测的真实输出。在监督学习中，模型的目标是通过学习输入特征与标签之间的关系，能够对新输入做出准确的预测。


### 线性回归的简洁实现

 （1）通过张量来进行数据存储和线性代数；
 （2）通过自动微分来计算梯度。 实际上，由于数据迭代器、损失函数、优化器和神经网络层很常用， 现代深度学习库也为我们实现了这些组件。
 
## softmax回归
![image](https://img2024.cnblogs.com/blog/488941/202401/488941-20240126124258669-388970424.png)


## 信息论
交叉熵分类目标： （i）最大化观测数据的似然；（ii）最小化传达标签所需的惊异。

 通常我们使用预测概率最高的类别作为输出类别。 如果预测与实际类别（标签）一致，则预测是正确的。 在接下来的实验中，我们将使用精度（accuracy）来评估模型的性能。 精度等于正确预测数与预测总数之间的比率。


# 4.多层感知机

## 多层感知机实现

## 模型选择,欠拟合和过拟合

## 权重衰减

## 暂退法

## 前向传播,反向传播和计算图

## 数值稳定性和模型初始化

## 环境和分布偏移

## Kaggle比赛

# 深度学习计算

层和快
参数管理
延后初始化
自定义层
读写文件
GPU

# 卷积神经网络
从全连接层到卷积
图像卷积
填充和步幅
多输入多输出通道
汇聚层
卷积神经网络 LeNet

# 现代卷积神经网络
深度卷积神经网络 AlexNet
使用块的网络(VGG)
网络中的网络(NiN)
含并行连结的网络(GooLeNet)
批量规范化
残差网络(ResNet)
稠密连接网络(DenseNet)


# 循环神经网络

序列模型
文本预处理
语言模型和数据集
循环神经网络
实现
通过时间反向传播

# 现代循环神经网络
门控循环单元(GRU)
长短期记忆网络(LSTM)
深度循环神经网络
双向循环神经网络
机器翻译与数据集
编码器-解码器架构
序列导序列学习(seq2seq)
束搜索

后面另有10-16章
[[DIVE INTO DEEP LEARNING下册]]




# 现代深度学习大类模型：

1. **前馈神经网络 (Feedforward Neural Networks, FNNs)：**
   - 也称为多层感知机（Multilayer Perceptron, MLP）。
   - 由输入层、若干隐藏层和输出层组成。
   - 适用于各种任务，包括分类、回归等。

2. **卷积神经网络 (Convolutional Neural Networks, CNNs)：**
   - 主要用于图像识别和处理。
   - 包含卷积层、池化层和全连接层。
   - 卷积层可以有效地捕捉图像中的局部特征。

3. **循环神经网络 (Recurrent Neural Networks, RNNs)：**
   - 适用于处理序列数据，如文本、语音等。
   - 具有循环结构，能够捕捉数据中的时序信息。
   - 长短时记忆网络（Long Short-Term Memory, LSTM）和门控循环单元（Gated Recurrent Unit, GRU）是常见的 RNN 变体。

4. **生成对抗网络 (Generative Adversarial Networks, GANs)：**
   - 由生成器和判别器组成，通过对抗训练生成真实样本的生成器。
   - 主要用于生成新的、与训练数据类似的样本。

5. **自编码器 (Autoencoders)：**
   - 包含编码器和解码器，用于学习数据的压缩表示。
   - 用于降维、去噪、生成等任务。

6. **强化学习模型 (Reinforcement Learning Models)：**
   - 包括深度 Q 网络（Deep Q Network, DQN）、策略梯度方法等。
   - 用于处理智能体与环境交互，学习制定动作策略以获得最大的奖励。

7. **注意力机制模型（Attention Mechanism Models）：**
   - 包括 Transformer 模型等。
   - 在处理序列数据时，通过引入注意力机制，使模型能够关注输入序列中的不同部分。

这些是主要的深度学习模型类别，每个类别都有其适用的场景和任务。同时，深度学习领域仍然在不断发展，新的模型和算法不断涌现。