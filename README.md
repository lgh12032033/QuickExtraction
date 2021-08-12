# QuickExtraction
- 这是一个可以快速将world文档中数据通过一定规则提取到我们制定excel中的一个批量处理工具。
- This is a bulk processing tool that can quickly extract data from world documents through certain rules into our developed excel
- 现在已经更新到T4版本，现在支持使用正则表达式对文件内容进行search或者findall的匹配，所有的配置内容可以在config.ini中进行设置，包括层级等。
- Now updated to the T4 version, regular expressions are now supported for matching file contents with search or findall, all configuration content can be set in the config .ini, including hierarchy, etc.
- 具体的使用功能参见《QE instructions》
- 使用前准备环境
~~~
 pip install docx
 pip install xlwt
 pip install pywin32
~~~
