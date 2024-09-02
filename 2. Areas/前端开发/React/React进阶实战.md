
### React博客实战
下面是一个简单的React博客示例代码，包括博客列表、博客详情和添加博客的功能：

```jsx
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import BlogList from './components/BlogList';
import BlogDetail from './components/BlogDetail';
import AddBlog from './components/AddBlog';
function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/add">Add Blog</Link>
            </li>
          </ul>
        </nav>
        <Route path="/" exact component={BlogList} />
        <Route path="/blog/:id" component={BlogDetail} />
        <Route path="/add" component={AddBlog} />
      </div>
    </Router>
  );
}
export default App;
```
```jsx
// components/BlogList.js
import React from 'react';
import { Link } from 'react-router-dom';
const BlogList = () => {
  const blogs = [
    { id: 1, title: 'Blog 1', content: 'This is blog 1 content.' },
    { id: 2, title: 'Blog 2', content: 'This is blog 2 content.' },
    { id: 3, title: 'Blog 3', content: 'This is blog 3 content.' },
  ];
  return (
    <div>
      <h2>Blog List</h2>
      <ul>
        {blogs.map(blog => (
          <li key={blog.id}>
            <Link to={`/blog/${blog.id}`}>{blog.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};
export default BlogList;
```
```jsx
// components/BlogDetail.js
import React from 'react';
import { useParams } from 'react-router-dom';
const BlogDetail = () => {
  const { id } = useParams();
  const blog = { id: 1, title: 'Blog 1', content: 'This is blog 1 content.' };
  return (
    <div>
      <h2>Blog Detail</h2>
      <h3>{blog.title}</h3>
      <p>{blog.content}</p>
    </div>
  );
};
export default BlogDetail;
```
```jsx
// components/AddBlog.js
import React, { useState } from 'react';
const AddBlog = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const handleSubmit = e => {
    e.preventDefault();
    // Add blog logic here
    console.log('Added blog:', { title, content });
    setTitle('');
    setContent('');
  };
  return (
    <div>
      <h2>Add Blog</h2>
      <form onSubmit={handleSubmit}>
        <label>Title:</label>
        <input type="text" value={title} onChange={e => setTitle(e.target.value)} />
        <label>Content:</label>
        <textarea value={content} onChange={e => setContent(e.target.value)} />
        <button type="submit">Add</button>
      </form>
    </div>
  );
};
export default AddBlog;
```
在这个示例中，我们使用React Router来处理路由和导航。`App.js`是应用程序的主组件，定义了导航和路由配置。`BlogList.js`显示博客列表，并使用`Link`组件创建博客详情页的链接。`BlogDetail.js`显示博客的详细信息，根据URL参数获取相应的博客。`AddBlog.js`允许用户添加博客，使用`useState`钩子来管理表单输入的状态，并在提交表单时执行相应的逻辑。
请注意，这只是一个简单的示例代码，不包含完整的后端和数据持久化逻辑。在实际开发中，您可能需要连接到后端API来获取和保存博客数据。

### React商场实战

下面是一个简单的React商城示例代码，包括商品列表、购物车和结算功能：

```jsx
// App.js
import React, { useState } from 'react';
import ProductList from './components/ProductList';
import ShoppingCart from './components/ShoppingCart';
function App() {
  const [cartItems, setCartItems] = useState([]);
  const addToCart = (product) => {
    setCartItems([...cartItems, product]);
  };
  const removeFromCart = (product) => {
    const updatedCartItems = cartItems.filter((item) => item.id !== product.id);
    setCartItems(updatedCartItems);
  };
  return (
    <div>
      <h1>React Store</h1>
      <ProductList addToCart={addToCart} />
      <ShoppingCart cartItems={cartItems} removeFromCart={removeFromCart} />
    </div>
  );
}
export default App;
```
```jsx
// components/ProductList.js
import React from 'react';
const ProductList = ({ addToCart }) => {
  const products = [
    { id: 1, name: 'Product 1', price: 10 },
    { id: 2, name: 'Product 2', price: 20 },
    { id: 3, name: 'Product 3', price: 30 },
  ];
  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - ${product.price}
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};
export default ProductList;
```
```jsx
// components/ShoppingCart.js
import React from 'react';
const ShoppingCart = ({ cartItems, removeFromCart }) => {
  return (
    <div>
      <h2>Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <p>No items in cart.</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              {item.name} - ${item.price}
              <button onClick={() => removeFromCart(item)}>Remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
export default ShoppingCart;
```


