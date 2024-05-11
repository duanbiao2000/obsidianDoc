<div style='font-family: Consolas,"Courier New",Courier,FreeMono,monospace;text-align:center;line-height: 12px;font-size:12px;'>
<%*
  const number = await tp.system.prompt("输入内容，仅限 0~9:-_/ 和空格：")
  if(number){
    tR += tp.user.get_big_number(number).replace(/\n/g, '<br>').replace(/ /g, '&nbsp;')
  }
%>
</div>


<% tp.user.Get_Sentence(tp) %><div style='font-family: Consolas,"Courier New",Courier,FreeMono,monospace;text-align:center;line-height: 12px;font-size:12px;'>


<% tp.user.Get_Today_Date() %>

<% tp.user.Get_Sentence(tp) %>


<% tp.user.Get_Today_History() %>