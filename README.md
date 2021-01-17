# runSQL
 python codes for running sql files

# 运行方法
## 步骤
1.在`configuration.py`文件中配置你的数据库相关参数。  
  
2.将需要运行的的sql文件放入`sql_files`文件夹下。  
  
3.修改`run_sql.py`文件中的文件路径为你的sql文件路径。  
  
4.执行`run_sql.py`文件即可。

## 额外说明
如果你有多个sql文件需要执行，我建议你将多个sql文件内的语句按照执行的先后顺序放入一个sql文件中。
语句之间只需要使用 `;`分割即可。
然后使用本代码执行合并后的sql文件，这样可以提高执行效率。
当然，你也可以将多个sql全部放入`sql_files`文件夹下，`run_sql.py`文件会根据这些文件的默认排序顺序执行这些sql文件。
