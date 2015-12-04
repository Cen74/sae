<!DOCTYPE html>
<html>
  <head>
    <title>Alan's Diary</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
     margin: 10px 20%;}
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Alan's Diary</h1>
    <form method="post" action="/newdiary">
      <div><textarea id="input" name="input"></textarea></div>
      <div><button id="go" type="submit">保存</button></div>
    </form>
    %import time
    %for row in content:
        <div class=post>
          <em class=date>{{row['time']}}</em><br>
          {{!row['content'].replace('\n','<br/>')}}
        </div>
    %end
  </body>
</html>