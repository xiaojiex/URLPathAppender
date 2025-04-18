import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(script_dir, exist_ok=True)  # 新增目录创建
url_path = os.path.join(script_dir, 'url.txt')

try:
    # 使用相对路径（动态获取脚本所在目录）
    with open(url_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
        
except FileNotFoundError:
    print(f"错误：找不到文件 {url_path}，请先创建该文件")  # 显示完整路径
    exit(1)

suffix = input("请输入要追加的路径（例如admin/login.php）: ").strip()

# 生成最终路径（使用脚本所在目录）
output_path = os.path.join(script_dir, 'final_url.txt')
with open(output_path, 'w') as out:
    for url in urls:
        full_url = f"{url}{suffix}"
        out.write(full_url + '\n')

print(f"已生成 {len(urls)} 条URL到 {output_path}")