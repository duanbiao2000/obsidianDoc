// 引入fastify和PrismaClient
const fastify = require('fastify')
const { PrismaClient } = require('@prisma/client')

// 创建PrismaClient实例
const prisma = new PrismaClient()
// 创建fastify实例
const app = fastify({ logger: true })

// 创建用户
app.post(`/signup`, async (req, res) => {
  const { name, email, posts } = req.body

  // 如果有posts，则将posts转换为数组
  const postData = posts
    ? posts.map((post) => {
      return { title: post.title, content: post.content || undefined }
    })
    : []

  // 创建用户
  const result = await prisma.user.create({
    data: {
      name,
      email,
      posts: {
        create: postData,
      },
    },
  })
  return result
})

// 创建帖子
app.post(`/post`, async (req, res) => {
  const { title, content, authorEmail } = req.body
  const result = await prisma.post.create({
    data: {
      title,
      content,
      author: { connect: { email: authorEmail } },
    },
  })
  return result
})

// 更新帖子浏览量
app.put('/post/:id/views', async (req, res) => {
  const { id } = req.params

  try {
    const post = await prisma.post.update({
      where: { id: Number(id) },
      data: {
        viewCount: {
          increment: 1,
        },
      },
    })

    return post
  } catch (error) {
    return { error: `Post with ID ${id} does not exist in the database` }
  }
})

// 发布或取消发布帖子
app.put('/publish/:id', async (req, res) => {
  const { id } = req.params

  try {
    const postData = await prisma.post.findUnique({
      where: { id: Number(id) },
      select: {
        published: true,
      },
    })

    const updatedPost = await prisma.post.update({
      where: { id: Number(id) || undefined },
      data: { published: !postData.published || undefined },
    })
    return updatedPost
  } catch (error) {
    return { error: `Post with ID ${id} does not exist in the database` }
  }
})

// 删除帖子
app.delete(`/post/:id`, async (req, res) => {
  const { id } = req.params

  const post = await prisma.post.delete({
    where: {
      id: Number(id),
    },
  })
  return post
})

// 获取所有用户
app.get('/users', async (req, res) => {
  const users = await prisma.user.findMany()
  return users
})

// 获取用户的草稿
app.get('/user/:id/drafts', async (req, res) => {
  const { id } = req.params

  const drafts = await prisma.user
    .findUnique({
      where: {
        id: Number(id),
      },
    })
    .posts({
      where: { published: false },
    })

  return drafts
})

// 获取帖子
app.get(`/post/:id`, async (req, res) => {
  const { id } = req.params

  const post = await prisma.post.findUnique({
    where: { id: Number(id) },
  })
  return post
})

// 获取帖子列表
app.get('/feed', async (req, res) => {
  const { searchString, skip, take, orderBy } = req.query

  const or = searchString
    ? {
      OR: [
        { title: { contains: searchString } },
        { content: { contains: searchString } },
      ],
    }
    : {}

  const posts = await prisma.post.findMany({
    where: {
      published: true,
      ...or,
    },
    include: { author: true },
    take: Number(take) || undefined,
    skip: Number(skip) || undefined,
    orderBy: {
      updatedAt: orderBy || undefined,
    },
  })

  return posts
})

// 启动服务器
app.listen({ port: 3000 }, () =>
  console.log(`
🚀 Server ready at: http://localhost:3000
⭐️ See sample requests: https://github.com/prisma/prisma-examples/tree/latest/javascript/rest-fastify#using-the-rest-api`),
)