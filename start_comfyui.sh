#!/bin/bash
# 一键启动 ComfyUI（AutoDL 实例 / 本地环境通用）
# 用法：bash start_comfyui.sh
set -e

COMFY_DIR="${COMFY_DIR:-}"
if [ -z "$COMFY_DIR" ]; then
    for d in /home/ComfyUI /root/ComfyUI /root/autodl-tmp/ComfyUI "$HOME/ComfyUI"; do
        if [ -d "$d" ]; then
            COMFY_DIR="$d"
            break
        fi
    done
fi

if [ -z "$COMFY_DIR" ]; then
    echo "未找到 ComfyUI 目录，请设置 COMFY_DIR 环境变量后重试"
    exit 1
fi

echo "启动 ComfyUI: $COMFY_DIR"
cd "$COMFY_DIR"
exec python main.py --listen 0.0.0.0 --port 7860
