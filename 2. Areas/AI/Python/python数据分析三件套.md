Seaborn 是基于 Matplotlib 的高级绘图库，专为统计数据可视化设计。它提供了更美观的默认样式和更高级的图表类型，如热力图、箱型图、小提琴图等。
- **统计图表**：专注于统计数据的可视化，如分布、回归、分类等。
- **美观的默认样式**：Seaborn 提供了一套美观的默认颜色和样式，使得图表更加吸引人。
- **集成**：与 Pandas 和 Matplotlib 紧密集成，可以直接使用 Pandas 的 DataFrame 和 Series 对象进行绘图。
### Seaborn 示例

```python
import seaborn as sns

# 使用 Seaborn 创建一个箱型图
tips = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
```
