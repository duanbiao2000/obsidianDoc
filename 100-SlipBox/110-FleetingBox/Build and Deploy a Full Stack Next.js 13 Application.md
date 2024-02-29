
![(79) Build and Deploy a Full Stack Next.js 13 Application | React, Next JS 13, TypeScript, Tailwind CSS - YouTube](https://www.youtube.com/watch?v=986hztrfaSQ)

Project-User
- How to create relations between them
- How to perform CRUD operations

Connectors
  That stitch GraphQL or OpenAPI
  APIs into a unified data layer

`Edge Resolvers`    ` Edge Caching`
to customize your GraphQL
API with edge functions

Serverless Database

Full-text search built-in

CLI for local dev with zero configuration

## Git-based workflow

## Auth
You can integrate your provider using OpenID Connect or JWT

###  These are only some of the features
That'll enable you to build complex apps
Incredibly Easily

You'll get first-hand experience on How to implement them on a real application

```bash
npx create-next-app@latest ./
```

dependencies:
```
- react
- react-dom
- next
- typescript
- @types/react
- @types/node
- @types/react-dom
- tailwindcss
- postcss
- autoprefixer
```

```bash
npm install @headlessui/react cloudinary jsonwebtoken @types/jsonwebtoken graphql-request next-auth
```

```bash
npm install @grafbase/sdk --save-dev
```

```tsx
//app/page.tsx   Home Page
const Home = () => {
  return (
    <section classname="flex-start flex-col paddings mb-16">
      <h1>Categories</h1>
      <h1>Posts</h1>
      <h1>LoadMore</h1>
    </section>
  )
}
export default Home;
```

```bash
npm run dev
```

```
//create new folder: app/api
//new file: app/globals.css (copy from src)
```

```tsx
//components

```


```tsx
//common.types.ts
import {User, Session} from 'next-auth'

export type FormState = {
  title: string;
  description: string;
  image: string
  liveSiteUrl: string;
  githubUrl: string;
  category: string;
};

export interface ProjextInterface {
  title: string;
  description: string;
  image: string;
  liveSiteUrl: string;
  githubUrl: string;
  category: string;
  id: string;
  createdBy:{
    name:string;
    email:string;
    avatarUrl: string;
    id: string;
  };
}

export interface UserProfile {
 id: string;
 ...
}

```

```tsx
//layout.tsx
import './globals.css';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

export const metadata = {
  title: 'Flexible',
  description:'Showcase and discover remarable developer projects.', 
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return(
    <html lang="en">
      <body>
        <Navbar />
        <main>
          {children}
        </main>
        <Footer />
      </body>
    </html>
  )
}
```

```jsx
//Navbar.tsx
import {NavLinks} from '@/constants'
import Link from 'next/link'
import React from 'react'
import AuthProviders from './AuthProviders';

const Navbar = () => {
  const session = {};

  return (
    <nav className="flexBetween navbar">
      <div className="flex-1 flexStart gap-10">
        <Link href="/">
          <Image
            src="/logo.svg"
            width={115}
            height={43}
            alt="Flexibble"
          />
        </Link>
        <ul className="xl:flex hidden text-small gap-7">
          {NavLinks.map((link)=>(
            <Link href={link.href} key={link.key}>
              {link.text}
            </Link>
          ))}
        </ul>
      </div>

      <div className="flexCenter gap-4">
        {seesion ? (
          <>
            UserPhoto
            
            <Link href="/create-project">
              Share Work
            </Link>
          </>
        ):(
          <AuthProviders />
        )}
      </div>
    </nav>
  )
}

export default Navbar
```

```tsx
//Footer.tsx
import {footerLinks} from '@/constants'
import Image from 'next/image'
import Link from 'next/link';

type ColumnProps ={
  title: string;
  links: Array<strings>;
}

const FooterColum = ({title, links}: ColummProps) => (
  <div className="footer_column">
    <h4 className="font-semibold">{title}</h4>
    <ul className="flex flex-col gap-2 font-normal">
      {links.map((link)=><Link href="/" key={link}>{link}</link>)}
    </ul>
  </div>
)

const Footer = ()=> {
  return (
    <footer className="flexStart footer">
      <div className="flex flex-col gap-12 w-full">
        <div className="flex items-start flex-col">
          <Image
            src="/logo-purple.svg"
            width={115}
            height={38}
            alt="Flexible"
          />
          
          <p className="text-start text-sm font-normal mt-5 max-w-xs">
          Flexibble is the world's leading community for creatives to share, grow, and get hired.</p>
        </div>
        <div className="flex flex-wrap gap-12">
          <FooterColumn title={footerLinks[0].title} links={footerLinks[0].links} />

          <div className="flex-1 flex flex-col gap-4">
            <FooterColumn title={footerLinks[1].title} links={footerLinks[1].links} />
            <FooterColumn title={footerLinks[2].title} links={footerLinks[2].links} />
          </div>
           <FooterColumn title={footerLinks[3].title} links={footerLinks[3].links} />
           <div className="flex-1 flex flex-col gap-4">
            <FooterColumn title={footerLinks[4].title} links={footerLinks[4].links} />
            <FooterColumn title={footerLinks[5].title} links={footerLinks[5].links} />
           </div>
            <FooterColumn title={footerLinks[6].title} links={footerLinks[6].links} />
        </div>
      </div>

      <div className="flexBetween footer_copyright">
        <p>@ 2023 Flexibble. All rights reserved </p>
        <p className="text-gray">
          <span className="text-black font-semibold">10,214</span> projects
          submitted
        </p>
      </div>

    </footer>
  )
}

export default Footer
```

```tsx
//AuthProviders.tsx
import React from 'react'

const AuthProviders=()=>
{
  return (
    <div>AuthProviders</div>
  )

export default AuthProviders
}
```


```ts
//index.ts
export const footerLinks = [
{
  title:'For developers',
  links:[
    'Go Pro!',
    'Explore development work',
    'Development blog',
    'Code podcast',
    'Open-source projects',
    'Refer a Friend',
    'Code of conduct',
  ],
},
{
  title:'Hire developers',
  links:[
    'Post a job opening',
    'Post a freelance project',
    'Search for developers',
  ],
}
]
```

















