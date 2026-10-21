# ComfyUI 环境备份（LightCC 云主机）

- 导出时间：2026-10-21
- 来源主机：LightCC 云主机 `swiftlink53.lightcc.cloud`（SSH 端口 51334）
- 导出内容：`/home/ComfyUI` 目录打包（tar.gz）
- 包文件：`comfyui-env.tar.gz`（约 15 MB）

## 包含

- ComfyUI 程序源码（0.40.0，Python 3.11 + PyTorch 2.8 CUDA 环境在云主机上）
- `custom_nodes/` 自定义节点（约 11 MB，ComfyUI Manager 管理）
- `user/` 用户配置（ComfyUI 设置）
- `models/` 目录结构与占位（模型文件基本为空，未随包导出）
- 其他运行配置

## 未包含（按需排除）

- `.git`（ComfyUI 源码仓库历史）
- `output/`、`temp/`（运行时产物）
- `__pycache__`（Python 缓存）
- `user/__manager/cache`（ComfyUI Manager 缓存）

## 还原方法（在目标 ComfyUI 环境）

```bash
tar xzf comfyui-env.tar.gz -C /home
```

## 备注

该云主机为 LightCC 云主机，随主机提供 miniconda3 环境（`/root/miniconda3`，约 9 GB，未随包导出）。
