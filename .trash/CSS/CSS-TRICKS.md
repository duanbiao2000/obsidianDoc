---
aliases:

---
20230717 1126
links: https://css-tricks.com
title:
origin:
tags: #flashcards #todo 



- [CSS Flexible Box Layout Module Level 1](https://www.w3.org/TR/css-flexbox-1/) (W3C)
- [A CSS Flexbox Cheatsheet](https://www.digitalocean.com/community/cheatsheets/css-flexbox?utm_medium=content_acq&utm_source=css-tricks&utm_campaign=&utm_content=awareness_bestsellers) (DigitalOcean)
- [Centering Things in CSS With Flexbox](https://www.digitalocean.com/community/tutorials/css-centering-using-flexbox?utm_medium=content_acq&utm_source=css-tricks&utm_campaign=&utm_content=awareness_bestsellers) (DigitalOcean)


#### the differences between Flexbox and Grid
Flexbox is "one dimensional" and allows elements to wrap, but it can't control where elements end up.    

```css
.parent { display: flex; flex-flow: row wrap; /* OK elements, go as far as you can on one line, then wrap as you see fit */ }
```

Grid is "two dimensional" and allows for explicit sizing of rows and columns and placement of elements within those rows and columns. Grid is better at overlapping, sturdier, and more flexible in terms of layout structure. Flexbox is supported in more browsers than Grid.
```css
.parent { 
display: grid; grid-template-columns: 1fr 3fr 1fr; /* Three columns, one three times as wide as the others */ 
grid-template-rows: 200px auto 100px; /* Three rows, two with explicit widths */ 
grid-template-areas: "header header header" ". main sidebar" "footer . ."; } /* Now, we can explicitly place items in the defined rows and columns. */ 

.child-1 { grid-area: header; } 
.child-2 { grid-area: main; } 
.child-3 { grid-area: sidebar; } 
.child-4 { grid-area: footer; }
```

Grid is mostly defined **on the parent element**. In flexbox, most of the layout (beyond the very basics) happen **on the children**.
```scss
/* The flex children do most of the work */ 
.flexbox { display: flex; 
  > div { 
  &:nth-child(1) { // logo 
    flex: 0 0 100px; 
  } 
  &:nth-child(2) { // search 
    flex: 1;
    max-width: 500px; } 
  &:nth-child(3) { // avatar 
  flex: 0 0 50px; 
  margin-left: auto; } 
  } } 
  /* The grid parent does most of the work */ 
  .grid { 
  display: grid; 
  grid-template-columns: 1fr auto minmax(100px, 1fr) 1fr; 
  grid-template-rows: 100px repeat(3, auto) 100px; 
  grid-gap: 10px; 
  }
```



**Flexbox can _optionally_ **wrap**.** If we allow a flex container to wrap, they will wrap down onto another row when the flex items fill a row. Where they line up on the next row is independent of what happenned on the first row, allowing for a masonry-like look.

>Use grid when you already have the layout structure in mind, and flex when you just want everything to fit. Layout first vs content first.
  — Beverly (@aszenitha) [January 25, 2019](https://twitter.com/aszenitha/status/1088838733086973953?ref_src=twsrc%5Etfw)

>flexbox looks like it does what you want but grid is usually what you want.

>Grid makes actual columns and rows. Content will line up from one to the other, as you ask it to. Flexbox doesn’t. Not only in the second dimension (which is easiest to talk about), but also in the first dimension. Flexbox isn’t for most of the things we’ve been using it for.

>Grid makes actual columns and rows. Content will line up from one to the other, as you ask it to. Flexbox doesn’t. Not only in the second dimension (which is easiest to talk about), but also in the first dimension. Flexbox isn’t for most of the things we’ve been using it for.

>Use grid when you already have the layout structure in mind, and flex when you just want everything to fit. Layout first vs content first.
  — Beverly (@aszenitha) [January 25, 2019](https://twitter.com/aszenitha/status/1088838733086973953?ref_src=twsrc%5Etfw)

