import os
import subprocess

def main():
    print("请将 .lpk 文件拖入此窗口后按 Enter:")
    lpk_path = input().strip().strip('"') 
    if not os.path.isfile(lpk_path):
        print("错误：文件路径无效或文件不存在！")
        return
    target_dir = os.path.dirname(lpk_path)
    config_path = os.path.join(target_dir, "config.json")
    output_dir = os.path.join(target_dir, "output")
    if not os.path.isfile(config_path):
        print(f"错误：配置文件 config.json 不存在！请确保它位于 {target_dir} 中。")
        return
    command = [
        "python", "LpkUnpacker.py", "-v",
        "-c", config_path,
        lpk_path,
        output_dir
    ]
    
    print("执行以下命令：")
    print(" ".join(command))

    try:
        subprocess.run(command, check=True)
        print(f"解包成功！解包文件已保存至: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"解包失败！错误信息：{e}")
    except Exception as ex:
        print(f"未知错误：{ex}")

if __name__ == "__main__":
    main()
