---
aliases: 
source: 
author: 
createdAt: 
updateAt: 
categories: 
high_priority: false
tags:
---
```js
import React, { useState } from 'react';
import { Tab } from '@/components/ui/tab';

// 模拟评论数据
const mockComments = [
  { id: 1, author: '用户A', content: '很棒的文章!', timestamp: new Date('2024-08-28T10:00:00'), likes: 15 },
  { id: 2, author: '用户B', content: '学到了很多,谢谢分享。', timestamp: new Date('2024-08-28T11:30:00'), likes: 8 },
  { id: 3, author: '用户C', content: '有一些地方还不太明白...', timestamp: new Date('2024-08-29T09:15:00'), likes: 3 },
  { id: 4, author: '用户D', content: '期待更多类似的内容!', timestamp: new Date('2024-08-29T14:00:00'), likes: 10 },
];

const CommentSection = () => {
  const [comments, setComments] = useState(mockComments);
  const [sortBy, setSortBy] = useState('newest');

  const sortComments = (type) => {
    let sortedComments = [...comments];
    if (type === 'newest') {
      sortedComments.sort((a, b) => b.timestamp - a.timestamp);
    } else if (type === 'hottest') {
      sortedComments.sort((a, b) => b.likes - a.likes);
    }
    setComments(sortedComments);
    setSortBy(type);
  };

  return (
    <div className="p-4">
      <div className="mb-4">
        <Tab.Group>
          <Tab.List className="flex space-x-1 rounded-xl bg-blue-900/20 p-1">
            <Tab
              className={({ selected }) =>
                `w-full rounded-lg py-2.5 text-sm font-medium leading-5 text-blue-700
                 ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2
                 ${selected ? 'bg-white shadow' : 'text-blue-100 hover:bg-white/[0.12] hover:text-white'}`
              }
              onClick={() => sortComments('newest')}
            >
              最新
            </Tab>
            <Tab
              className={({ selected }) =>
                `w-full rounded-lg py-2.5 text-sm font-medium leading-5 text-blue-700
                 ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2
                 ${selected ? 'bg-white shadow' : 'text-blue-100 hover:bg-white/[0.12] hover:text-white'}`
              }
              onClick={() => sortComments('hottest')}
            >
              最热
            </Tab>
          </Tab.List>
        </Tab.Group>
      </div>
      <div className="space-y-4">
        {comments.map((comment) => (
          <div key={comment.id} className="bg-white p-4 rounded shadow">
            <div className="font-bold">{comment.author}</div>
            <div className="text-gray-600">{comment.content}</div>
            <div className="text-sm text-gray-500 mt-2">
              {comment.timestamp.toLocaleString()} · 点赞数: {comment.likes}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CommentSection;
```

