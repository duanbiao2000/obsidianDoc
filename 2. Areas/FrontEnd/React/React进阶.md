
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

