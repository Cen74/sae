
<html>
	    <body>
          	<h1> Cen的日记  </h1>
        	<form action="/newdiary" method="post">
            输入: <input name="input" type="text" />
            <input value="确认" type="submit" />


        	<p> 历史内容 ：</p>
          % if content:
          %   for line in content: 
              {{line['content']}} 
          %   end
          % else:
            <br> Empty Diary
       
        

        </body>
</html>
