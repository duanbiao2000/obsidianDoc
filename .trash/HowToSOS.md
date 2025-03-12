曾经也做过一些装扮的事情，只是很多内容还停留在表面，以至于主页看起来比较简单，最近对主页进行了整体的改造，过程中也遇到不少好的经验，这篇文章就是对这些内容的总结整理，看完之后，你也可以快速构建一个美观简洁的个人主页，这是一张重要的个人名片，快装扮起来吧。

```
![二丫讲梵's github stats](https://github-readme-stats.vercel.app/api?username=eryajf&amp;hide_title=false&amp;hide_border=true&amp;show_icons=true&amp;include_all_commits=true&amp;line_height=20&amp;bg_color=0,EC6C6C,FFD479,FFFC79,73FA79&amp;theme=graywhite&amp;locale=cn)![主要使用语言](https://github-readme-stats.vercel.app/api/top-langs/?username=eryajf&amp;hide_title=false&amp;hide_border=true&amp;layout=compact&amp;bg_color=0,73FA79,73FDFF,D783FF&amp;theme=graywhite&amp;locale=cn)

![profile](https://github-profile-trophy.vercel.app/?username=eryajf&amp;theme=algolia&amp;column=8)
```

```
![snake](./assets/github-contribution-grid-snake.svg)
```

```
<span>name</span><span>:</span> Generate Snake
<span>on</span><span>:</span>
  <span>schedule</span><span>:</span>
    <span>-</span> <span>cron</span><span>:</span> <span>"0 0 * * *"</span>
  <span>workflow_dispatch</span><span>:</span>
<span>jobs</span><span>:</span>
  <span>build</span><span>:</span>
    <span>runs-on</span><span>:</span> ubuntu<span>-</span>latest
    <span>steps</span><span>:</span>
      <span>-</span> <span>name</span><span>:</span> Checkout
        <span>uses</span><span>:</span> actions/checkout@v2.3.4
      <span>-</span> <span>name</span><span>:</span> Generate Snake
        <span>uses</span><span>:</span> Platane/snk@master
        <span>id</span><span>:</span> snake<span>-</span>gif
        <span>with</span><span>:</span>
          <span>github_user_name</span><span>:</span> $<span>{</span><span>{</span> github.repository_owner <span>}</span><span>}</span>
          <span>gif_out_path</span><span>:</span> ./assets/github<span>-</span>contribution<span>-</span>grid<span>-</span>snake.gif
          <span>svg_out_path</span><span>:</span> ./assets/github<span>-</span>contribution<span>-</span>grid<span>-</span>snake.svg
      <span>-</span> <span>name</span><span>:</span> Push to GitHub
        <span>uses</span><span>:</span> EndBug/add<span>-</span>and<span>-</span>commit@v7.2.1
        <span>with</span><span>:</span>
          <span>branch</span><span>:</span> master
          <span>message</span><span>:</span> <span>"Generate Contribution Snake"</span>
```

```
![](https://activity-graph.herokuapp.com/graph?username=eryajf&amp;theme=github)
```

```
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=eryajf&amp;repo=ldapctl&amp;show_owner=true&amp;&amp;theme=cobalt)](https://github.com/eryajf/ldapctl)
```

```
<span>name</span><span>:</span> Latest blog post workflow
<span>on</span><span>:</span>
  <span>schedule</span><span>:</span> <span># Run workflow automatically</span>
    <span>-</span> <span>cron</span><span>:</span> <span>"0 * * * *"</span>
  <span>workflow_dispatch</span><span>:</span>
<span>jobs</span><span>:</span>
  <span>update-readme-with-blog</span><span>:</span>
    <span>name</span><span>:</span> Update this repo's README with latest blog posts
    <span>runs-on</span><span>:</span> ubuntu<span>-</span>latest
    <span>steps</span><span>:</span>
      <span>-</span> <span>name</span><span>:</span> Checkout
        <span>uses</span><span>:</span> actions/checkout@v2
      <span>-</span> <span>name</span><span>:</span> Pull in eryajf posts
        <span>uses</span><span>:</span> gautamkrishnar/blog<span>-</span>post<span>-</span>workflow@v1
        <span>with</span><span>:</span>
          <span>max_post_count</span><span>:</span> <span>6</span>
          <span>committer_username</span><span>:</span> <span>"eryajf"</span>
          <span>committer_email</span><span>:</span> <span>"eryajf@163.com"</span>
          <span>feed_list</span><span>:</span> <span>"https://wiki.eryajf.net/rss.xml"</span>
          <span>template</span><span>:</span> <span>"$newline- $randomEmoji(💯,🔥,💫,🚀,🌮,📝,🥳,💻,🧰,🏊,🥰,🧐,🤓,😎,🥸,🤩,🤗,🤔,🫣,🤭,🤠,👹,👺,🤡,🤖,🎃,😺,🫶,👍,💪,💄,👀,🧠,🧑🏫,👨🏫,💂,🧑💻,🥷,💃,🕴,💼,🎓,🐻,🐵,🙉,🦄,🦆,🦅,🦍,🦣,🐘,🦒,🦏,🐎,🦩,🐲,🌝,🌜,🌏,🌈,🌊,🎬,🎭,🚀,🚦,⛽️,🗽,🎡,🌋,🌁,💡,🕯,🪜,🧰,⚗️,🔭,🪄,🎊,🎉,) [$title]($url) $newline"</span>
```