
<html>
	    <body>
          	<h1> Cen的日记  </h1>
        	<form action="/diary" method="post">
            输入: <input name="content" type="text" />
            <input value="确认" type="submit" />


        	<p> 历史内容 ：</p>
          %   for line in content: 
                <br> {{line}} </br>
          %   end
       
        

        </body>
</html>
