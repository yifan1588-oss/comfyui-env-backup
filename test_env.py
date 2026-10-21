#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoDL 算法镜像环境自检脚本
用于通过 AutoDL「代码可在镜像环境中正常执行」的审核验证：
  1. Python 版本
  2. PyTorch / CUDA 是否可用
  3. ComfyUI 主模块能否导入
  4. 关键依赖是否齐全
用法：python test_env.py
退出码：0 = 环境合格；1 = 环境存在问题
"""
import sys
import os


def main():
    print("=" * 52)
    print("ComfyUI 镜像环境自检")
    print("=" * 52)
    print("Python:", sys.version.split()[0])

    ok = True

    # 1. PyTorch / CUDA
    try:
        import torch
        print("PyTorch:", torch.__version__)
        print("CUDA 可用:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("GPU:", torch.cuda.get_device_name(0))
    except Exception as e:
        ok = False
        print("PyTorch 导入失败:", e)

    # 2. ComfyUI 主模块（兼容常见安装路径）
    comfy_dirs = [
        "/home/ComfyUI",
        "/root/ComfyUI",
        "/root/autodl-tmp/ComfyUI",
        os.path.expanduser("~/ComfyUI"),
    ]
    found = False
    for d in comfy_dirs:
        if os.path.isdir(d):
            sys.path.insert(0, d)
            found = True
            print("ComfyUI 目录:", d)
            break
    if not found:
        sys.path.insert(0, os.getcwd())
        print("ComfyUI 目录: 未在常见路径发现，按当前目录尝试导入")
    try:
        import comfy
        print("comfy 模块导入: OK")
    except Exception as e:
        ok = False
        print("comfy 模块导入失败:", e)

    # 3. 关键依赖
    for mod in ["numpy", "PIL", "aiohttp", "yaml"]:
        try:
            __import__(mod)
        except Exception as e:
            ok = False
            print("依赖缺失 %s:" % mod, e)

    print("=" * 52)
    if ok:
        print("结果: 环境配置合格 ✓")
        return 0
    else:
        print("结果: 环境存在问题 ✗")
        return 1


if __name__ == "__main__":
    sys.exit(main())
