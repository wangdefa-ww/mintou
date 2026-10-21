# -*- coding: utf-8 -*-
"""
广告投放成本计算小工具
用于快速估算广告投放的消耗、CPM/CPC 等基础指标。
"""

def calc_cost(clicks, cpc):
    """按点击量与 CPC 计算总消耗"""
    return clicks * cpc


def calc_cpm(cost, impressions):
    """按消耗与展示量计算 CPM（千次展示成本）"""
    if impressions == 0:
        return 0.0
    return cost / impressions * 1000


if __name__ == "__main__":
    # 示例：千川投放场景
    clicks = 1200
    cpc = 1.5
    impressions = 85000

    total_cost = calc_cost(clicks, cpc)
    cpm = calc_cpm(total_cost, impressions)

    print(f"总消耗: {total_cost:.2f} 元")
    print(f"CPM: {cpm:.2f} 元/千次展示")
    print(f"平均点击成本 CPC: {cpc:.2f} 元/次")
