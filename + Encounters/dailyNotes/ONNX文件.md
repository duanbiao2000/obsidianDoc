## ONNX文件
在提供的代码仓中，有两个与ONNX文件相关的文件：

1. **model.onnx** - 这个文件位于`onnx`目录下，是一个ONNX模型文件。ONNX（Open Neural Network Exchange）是一个开放的格式，用于表示深度学习模型。这个文件可能包含了预训练的模型，可以用于推理或进一步训练。

2. **model_quantized.onnx** - 这个文件也位于`onnx`目录下，是一个量化后的ONNX模型文件。量化是一种优化技术，可以将模型的大小减小，同时保持或提高模型的性能。这个文件可能包含了预训练的量化模型，可以用于推理或进一步训练。

这两个文件都是ONNX模型文件，可以用于深度学习模型的推理或进一步训练。ONNX是一个开放的格式，可以用于不同的深度学习框架和平台，如TensorFlow、PyTorch、Caffe等。

在`.gitattributes`文件中，这些ONNX文件被配置为使用Git Large File Storage（LFS）进行版本控制。LFS是一种Git扩展，用于处理大文件，如模型文件。使用LFS可以避免Git仓库的体积过大，同时还可以保持文件的完整性和可访问性。

总的来说，`model.onnx`和`model_quantized.onnx`是两个ONNX模型文件，可以用于深度学习模型的推理或进一步训练。这些文件被配置为使用Git LFS进行版本控制，以避免Git仓库的体积过大。