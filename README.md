# URLPathAppender

**一个用于批量为当前路径下的 `url.txt` 文件中的 URL 添加路径的Python脚本。**

## 描述
这个脚本可以批量为存储在当前目录下的 `url.txt` 文件中的 URL 添加指定路径。它简单易用，无需复杂配置，直接运行脚本即可完成操作。运行脚本后，用户将被提示输入要添加的路径，脚本会自动将修改后的 URL 保存到当前目录下的 `final_url.txt` 文件中。

## 功能特点
- **自动读取**：直接从当前目录下的 `url.txt` 文件读取 URL 列表。
- **用户输入**：运行脚本时，用户可以手动输入要添加的路径。
- **自动保存**：修改后的 URL 将被保存到当前目录下的 `final_url.txt` 文件中。
- **简单易用**：无需任何额外配置，直接运行即可。

## 使用方法
1. **准备 `url.txt` 文件**：将需要处理的 URL 列表保存到当前目录下的 `url.txt` 文件中，每个 URL 占一行。
2. **运行脚本**：直接运行脚本，脚本会提示用户输入要添加的路径。
   ```bash
   python url_path_appender.py
   根据提示输入路径
   假设url.txt内容是
   http://example.com
   https://testsite.org
   运行脚本并输入路径 /new/path 后，final_url.txt 文件内容将变为：
   http://example.com/new/path
   https://testsite.org/new/path
