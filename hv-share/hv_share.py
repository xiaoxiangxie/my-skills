#!/usr/bin/env python3
"""
hv-share: 一图系列生成器
用法: python hv_share.py <主题词> [输出目录]
"""

import sys
import os
import json
import re
import subprocess
import tempfile
from pathlib import Path

# 城市列表（简单判断，非精确）
CITIES = {
    "北京","上海","广州","深圳","成都","杭州","重庆","武汉","西安","苏州",
    "南京","天津","长沙","郑州","东莞","青岛","沈阳","宁波","昆明","大连",
    "无锡","合肥","福州","厦门","济南","温州","哈尔滨","长春","石家庄",
    "福州","南昌","贵阳","太原","南宁","徐州","佛山","泉州","乌鲁木齐",
    "兰州","洛阳","开封","绍兴","扬州","惠州","珠海","中山","海口","三亚",
    "拉萨","银川","西宁","呼和浩特","张家界","桂林","丽江","大理","西安",
}

def is_city(topic: str) -> bool:
    return topic.strip() in CITIES

def run_skill(skill_name: str, args: str, cwd: str = None) -> dict:
    """通过 Claude Code 的 skill 工具触发子 skill"""
    # 这里实际由调用方（Claude Code）通过 Skill tool 触发
    # 本脚本仅负责数据处理和 HTML 生成
    return {}

def generate_city_cards(travel_data: dict, city: str, output_path: str) -> str:
    """生成城市主题 HTML 卡片"""
    # 见下方 HTML 模板，数据从 travel_data 注入
    pass

def generate_analysis_cards(analysis_data: dict, topic: str, output_path: str) -> str:
    """生成横纵分析主题 HTML 卡片"""
    pass

def main():
    if len(sys.argv) < 2:
        print("用法: python hv_share.py <主题词> [输出目录]")
        sys.exit(1)

    topic = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output/hv-share"

    os.makedirs(output_dir, exist_ok=True)

    if is_city(topic):
        print(f"🌆 检测为城市: {topic}")
        # 后续通过 Skill tool 调用 ljg-travel
    else:
        print(f"📊 检测为分析主题: {topic}")
        # 后续通过 Skill tool 调用 hv-analysis

    index_path = os.path.join(output_dir, "index.html")
    print(f"输出目录: {output_dir}")
    print(f"主文件: {index_path}")

if __name__ == "__main__":
    main()