// 引入PrismaClient
const { PrismaClient } = require('@prisma/client')
// 创建PrismaClient实例
const prisma = new PrismaClient()

// 定义用户数据
const userData = [
  {
    name: 'Alice',
    email: 'alice@prisma.io',
    posts: {
      create: [
        {
          title: 'Join the Prisma Discord',
          content: 'https://pris.ly/discord',
          published: true
        },
      ]
    },
  },
  {
    name: 'Bob',
    email: 'bob@prisma.io',
    posts: {
      create: [
        {
          title: 'Follow Prisma on Twitter',
          content: 'https://twitter.com/prisma',
          published: true
        },
        {
          title: 'Follow Prisma on LinkedIn',
          content: 'https://www.linkedin.com/company/prisma/',
          published: true
        },
      ]
    },
  },
  {
    name: 'Charlie',
    email: 'charlie@prisma.io',
    posts: {
      create: [
        {
          title: 'Follow Prisma on YouTube',
          content: 'https://www.youtube.com/channel/UC6N8z7W9vYQ_ZYqb-fh_Y_A',
          pubilished: true,
          viewCount: 42,
        }
      ]
    }
  }
]

// 定义主函数
async function main() {
  console.log(`Start seeding...`)
  // 遍历用户数据
  for (const u of userData) {
    // 创建用户
    const user = await prisma.user.create({
      data: u,
    })
    console.log(`Created user with id: ${user.id}`)
  }
  console.log(`Seeding finished.`)
}

// 调用主函数
main()
  .then(async () => {
    // 断开PrismaClient连接
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    // 断开PrismaClient连接
    await prisma.$disconnect()
    // 退出程序
    process.exit(1)
  })