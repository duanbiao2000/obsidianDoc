---
view-count: 5
tags:
  - typescript
  - tailwind-css
  - react
  - next-js
  - Type/Reference
  - Domain/Technology
  - typescript
  - tailwind-css
  - react
  - next-js
---
### **Next.js 核心能力20题实战 (App Router 版)**

> **核心目标**: **在 20 个实战练习中，掌握构建现代、高性能 Next.js 应用所需的最核心工程能力。** 本指南以构建一个迷你博客为例，贯穿所有练习。

---

#### **第一部分：项目基础与核心概念 (1-5)**

<details>
<summary>1. **项目初始化与结构**: 初始化一个包含 TypeScript 和 Tailwind CSS 的 Next.js App Router 项目。</summary>

**要求**: 创建一个新项目，并理解 `app/layout.tsx` 和 `app/page.tsx` 的作用。
**答案**:
```bash
npx create-next-app@latest my-blog --ts --tailwind --eslint
```
*   `app/layout.tsx`: **根布局**，所有页面共享的 HTML 骨架。
*   `app/page.tsx`: **首页**，对应于 `/` 路由。

</details>

<details>
<summary>2. **服务端组件 (RSC) vs. 客户端组件**: 创建一个显示服务器时间的 RSC 和一个带点击事件的客户端组件。</summary>

**要求**: 理解两者的区别和 `'use client';` 指令的用途。
**答案**:
*   **服务端组件 (默认)**: `app/components/ServerTime.tsx`
    ```tsx
    export default function ServerTime() {
      // 可以在服务端执行，如 new Date() 获取的是服务器时间
      return <p>Server Time: {new Date().toLocaleTimeString()}</p>;
    }
    ```
*   **客户端组件**: `app/components/AlertButton.tsx`
    ```tsx
    'use client'; // 必须在文件顶部声明

    export default function AlertButton() {
      // 可以使用 hooks 和浏览器事件
      return <button onClick={() => alert('Clicked!')}>Click Me</button>;
    }
    ```
**核心区别**: RSC 在服务器上渲染，无交互能力，减小客户端包体积；客户端组件在浏览器中渲染，支持 Hooks 和事件。

</details>

<details>
<summary>3. **文件系统路由**: 创建博客文章列表页 (`/posts`) 和动态详情页 (`/posts/[id]`)。</summary>

**要求**: 掌握静态路由和动态路由的文件夹结构。
**答案**:
*   **列表页**: 创建 `app/posts/page.tsx`。
*   **详情页**: 创建 `app/posts/[id]/page.tsx`。
    ```tsx
    // app/posts/[id]/page.tsx
    // props.params.id 会自动接收 URL 中的动态部分
    export default function PostPage({ params }: { params: { id: string } }) {
      return <h1>Post ID: {params.id}</h1>;
    }
    ```

</details>

<details>
<summary>4. **布局 (Layout)**: 为所有博客相关的页面创建一个共享布局。</summary>

**要求**: 在 `/posts` 和 `/posts/[id]` 页面顶部显示一个 “Blog” 标题。
**答案**: 创建 `app/posts/layout.tsx`。
```tsx
export default function BlogLayout({ children }: { children: React.ReactNode }) {
  return (
    <section>
      <h1 className="text-2xl font-bold">My Blog</h1>
      {/* 子页面 (page.tsx) 或嵌套布局会渲染在这里 */}
      {children}
    </section>
  );
}
```

</details>

<details>
<summary>5. **API 路由**: 创建一个 `/api/posts` 的 GET 接口，返回模拟的博客文章列表。</summary>

**要求**: 掌握 App Router 中 API 路由的创建方式。
**答案**: 创建 `app/api/posts/route.ts`。
```ts
import { NextResponse } from 'next/server';

export async function GET() {
  const posts = [{ id: '1', title: 'First Post' }, { id: '2', title: 'Second Post' }];
  return NextResponse.json(posts);
}
```

</details>

---

#### **第二部分：数据获取与渲染 (6-10)**

<details>
<summary>6. **服务端数据获取**: 在 `/posts` 页面，通过 `fetch` 调用 `/api/posts` 并渲染文章列表。</summary>

**要求**: 掌握在 RSC 中进行数据获取的模式。
**答案**:
```tsx
// app/posts/page.tsx
async function getPosts() {
  // 注意：在服务端组件中，可以使用绝对 URL 或配置 HOST 环境变量
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/posts`);
  return res.json();
}

export default async function PostsPage() {
  const posts = await getPosts();
  return (
    <ul>
      {posts.map((post: any) => (
        <li key={post.id}><a href={`/posts/${post.id}`}>{post.title}</a></li>
      ))}
    </ul>
  );
}
```

</details>

<details>
<summary>7. **加载 UI (`loading.tsx`)**: 为 `/posts` 页面添加加载状态。</summary>

**要求**: 在数据加载时，自动显示一个 loading 界面。
**答案**: 创建 `app/posts/loading.tsx`。
```tsx
export default function Loading() {
  return <p>Loading posts...</p>;
}
```
Next.js 会自动在 `PostsPage` 数据加载期间，用这个组件作为 `Suspense` 的 `fallback`。

</details>

<details>
<summary>8. **错误 UI (`error.tsx`)**: 为 `/posts/[id]` 页面添加错误处理。</summary>

**要求**: 当文章获取失败时，显示一个友好的错误信息和重试按钮。
**答案**: 创建 `app/posts/[id]/error.tsx`。
```tsx
'use client'; // 错误组件必须是客户端组件

export default function Error({ error, reset }: { error: Error; reset: () => void; }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

</details>

<details>
<summary>9. **生成静态页面 (`generateStaticParams`)**: 预构建前 10 篇博客文章的详情页。</summary>

**要求**: 提升构建速度和页面加载性能。
**答案**: 在 `app/posts/[id]/page.tsx` 中导出 `generateStaticParams`。
```ts
export async function generateStaticParams() {
  const posts = await fetch('/api/posts').then((res) => res.json());

  // 返回一个 params 数组，Next.js 会在构建时为每个 param 生成静态页面
  return posts.slice(0, 10).map((post: any) => ({
    id: post.id,
  }));
}
```

</details>

<details>
<summary>10. **缓存与数据重新验证**: 设置文章列表页每小时重新验证一次数据。</summary>

**要求**: 掌握 `fetch` 的缓存控制。
**答案**: 在 `getPosts` 函数的 `fetch` 调用中添加 `revalidate` 选项。
```ts
// in getPosts function
const res = await fetch(url, { next: { revalidate: 3600 } }); // 3600 秒 = 1 小时
```
这实现了增量静态再生 (ISR)。

</details>

---

#### **第三部分：数据变更与交互 (11-15)**

<details>
<summary>11. **Server Actions**: 创建一个表单，用于添加新文章，通过 Server Action 直接与数据库交互。</summary>

**要求**: 理解 Server Actions 如何替代传统的 API 路由进行数据变更。
**答案**:
1.  **定义 Action**: `app/actions.ts`
    ```ts
    'use server';
    import { revalidatePath } from 'next/cache';

    export async function createPost(formData: FormData) {
      const title = formData.get('title') as string;
      // ... 在这里直接调用数据库或服务来创建文章 ...
      console.log('New Post Title:', title);
      
      revalidatePath('/posts'); // 清除 /posts 页面的缓存，使其重新获取数据
    }
    ```
2.  **在组件中使用**: `app/components/NewPostForm.tsx`
    ```tsx
    import { createPost } from '@/app/actions';

    export default function NewPostForm() {
      return (
        <form action={createPost}>
          <input type="text" name="title" required />
          <button type="submit">Create Post</button>
        </form>
      );
    }
    ```
**核心优势**: 无需手动创建 API 路由，简化了数据变更逻辑，且默认支持渐进式增强。

</details>

<details>
<summary>12. **`useFormState`**: 在表单提交后，显示来自 Server Action 的成功或错误消息。</summary>

**要求**: 掌握处理 Server Action 返回状态的 Hook。
**答案**:
```tsx
'use client';
import { useFormState } from 'react-dom';
import { createPost } from '@/app/actions';

const initialState = { message: '' };

export function NewPostForm() {
  const [state, formAction] = useFormState(createPost, initialState);

  return (
    <form action={formAction}>
      {/* ... form fields ... */}
      <p>{state?.message}</p>
    </form>
  );
}

// 在 action 中返回状态
export async function createPost(prevState: any, formData: FormData) {
  // ... a lot of logic ...
  return { message: 'Post created successfully!' };
}
```

</details>

<details>
<summary>13. **乐观更新 (`useOptimistic`)**: 创建一个“点赞”按钮，点击后 UI 立即更新，再在后台发送请求。</summary>

**要求**: 提升用户体验，避免等待服务器响应。
**答案**:
```tsx
'use client';
import { useOptimistic } from 'react';

function LikeButton({ initialLikes, likeAction }) {
  const [optimisticLikes, addOptimisticLike] = useOptimistic(
    initialLikes,
    (state, amount) => state + amount
  );

  return (
    <form action={async () => {
      addOptimisticLike(1); // 立即在 UI 上 +1
      await likeAction(); // 在后台发送真实请求
    }}>
      <button type="submit">Likes ({optimisticLikes})</button>
    </form>
  );
}
```

</details>

<details>
<summary>14. **`useRouter`**: 表单提交成功后，以编程方式导航到新创建的文章页面。</summary>

**要求**: 掌握客户端的编程式导航。
**答案**: 在客户端组件中：
```tsx
'use client';
import { useRouter } from 'next/navigation';

// ...
const router = useRouter();

const handleSubmit = async (formData) => {
  const newPost = await createPostAction(formData);
  router.push(`/posts/${newPost.id}`); // 导航到新页面
};
```

</details>

<details>
<summary>15. **`redirect`**: 在 Server Action 或服务端组件中，进行服务器端重定向。</summary>

**要求**: 掌握服务端重定向。
**答案**:
```ts
// in a Server Action or RSC
import { redirect } from 'next/navigation';

export async function updateUser(formData) {
  'use server';
  // ... update logic ...
  redirect('/profile'); // 重定向到个人资料页
}
```

</details>

---

#### **第四部分：认证、元数据与优化 (16-20)**

<details>
<summary>16. **中间件 (`middleware.ts`)**: 保护所有 `/admin` 开头的页面，未登录用户重定向到 `/login`。</summary>

**要求**: 掌握在 Edge 运行时进行路由保护。
**答案**: 在项目根目录创建 `middleware.ts`。
```ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const isAuthenticated = request.cookies.has('auth-token'); // 简化认证检查

  if (request.nextUrl.pathname.startsWith('/admin') && !isAuthenticated) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}
```

</details>

<details>
<summary>18. **图片优化 (`next/image`)**: 在首页使用 `Image` 组件展示一张图片。</summary>

**要求**: 自动实现图片懒加载、格式优化 (WebP) 和尺寸调整。
**答案**:
```tsx
import Image from 'next/image';

<Image
  src="/path/to/your/image.jpg"
  alt="Description"
  width={500}
  height={300}
  priority // 如果是首屏图片，加上此属性
/>
```

</details>

<details>
<summary>19. **字体优化 (`next/font`)**: 引入一个 Google 字体并全局应用。</summary>

**要求**: 避免字体加载引起的布局偏移 (CLS) 并提升性能。
**答案**:
```tsx
// app/layout.tsx
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      {/* ... */}
    </html>
  );
}
```

</details>

<details>
<summary>20. **部署**: 将你的博客项目部署到 Vercel。</summary>

**要求**: 实现 Git 推送即部署 (CI/CD)。
**答案**:
1.  将你的项目推送到 GitHub/GitLab/Bitbucket。
2.  登录 Vercel，选择 "Add New... -> Project"。
3.  从你的 Git 提供商导入该项目仓库。
4.  Vercel 会自动识别为 Next.js 项目，点击 "Deploy"。
**完成**: 之后每次 `git push` 到主分支，Vercel 都会自动构建和部署新版本。

</details>
