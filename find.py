import re

# 定义要解析的日志文件路径
log_file_path = '/home/coral/coding/BSARec/src/output/BSARec_SA_S_Yelp.log'

# 正则表达式模式用于匹配日志行中的指标
pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - {'Epoch': (\d+), 'HR@5': '([\d.]+)', 'NDCG@5': '([\d.]+)', 'HR@10': '([\d.]+)', 'NDCG@10': '([\d.]+)', 'HR@20': '([\d.]+)', 'NDCG@20': '([\d.]+)'}")

max_sum = 0
best_line = ""

with open(log_file_path, 'r') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            # 解析出每个值并转换为浮点数
            timestamp = match.group(1)
            epoch = int(match.group(2))
            hr5 = float(match.group(3))
            ndcg5 = float(match.group(4))
            hr10 = float(match.group(5))
            ndcg10 = float(match.group(6))
            hr20 = float(match.group(7))
            ndcg20 = float(match.group(8))

            # 计算总和
            total = sum([hr5, ndcg5, hr10, ndcg10, hr20, ndcg20])

            # 如果当前行的总和大于已知的最大值，则更新最大值和最佳行
            if total > max_sum:
                max_sum = total
                best_line = f"{timestamp} - {{'Epoch': {epoch}, 'HR@5': '{hr5:.4f}', 'NDCG@5': '{ndcg5:.4f}', 'HR@10': '{hr10:.4f}', 'NDCG@10': '{ndcg10:.4f}', 'HR@20': '{hr20:.4f}', 'NDCG@20': '{ndcg20:.4f}'}}"

print("最高总和的行是：")
print(best_line)