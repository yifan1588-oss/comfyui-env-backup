# ComfyUI 环境备份（LightCC 云主机）

AutoDL 算法镜像配套代码仓库 · 导出时间：2026-10-21

- 来源主机：LightCC 云主机 `swiftlink53.lightcc.cloud`（Docker 容器，ComfyUI 0.40.0）
- 用途：配合 AutoDL Art 发布的 ComfyUI 算法镜像使用，镜像环境中安装的 ComfyUI 目录由镜像本体提供，本仓库提供环境自检脚本与启动脚本

## 仓库结构

```
comfyui-env-backup/
├── test_env.py         # 环境自检脚本（AutoDL 审核用：验证 PyTorch/CUDA/ComfyUI 可运行）
├── start_comfyui.sh    # 一键启动 ComfyUI（--listen 0.0.0.0 --port 7860）
├── README.md           # 本说明
└── comfyui-env.tar.gz  # ComfyUI 程序/自定义节点/配置的备份包（约 15 MB，可选资产）
```

## 环境自检

在镜像环境中执行（AutoDL 审核会运行简单代码验证环境）：

```bash
python test_env.py
```

通过标准：退出码 0，输出「结果: 环境配置合格 ✓」。

## 启动 ComfyUI

```bash
bash start_comfyui.sh
```

启动后访问 `http://<实例公网地址>:7860`。

## 备份包内容（comfyui-env.tar.gz）

- ComfyUI 程序源码（0.40.0）
- `custom_nodes/` 自定义节点（约 11 MB）
- `user/` 用户配置
- `models/` 目录结构与占位（模型文件基本为空，未随包导出）

排除项：`.git`、`output/`、`temp/`、`__pycache__`、`user/__manager/cache`。

还原到目标环境：

```bash
tar xzf comfyui-env.tar.gz -C /home
```

## 备注

- 云主机随附 miniconda3 环境（`/root/miniconda3`，约 9 GB，未随包导出）
- 模型文件未包含在本仓库（如需发布带模型的完整环境，镜像本体应自带模型目录）
