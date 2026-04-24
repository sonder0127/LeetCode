import random
def top_k_sampling(logits, top_k):
    logits_index = list(enumerate(logits))
    print(logits_index)
    logits_index.sort(key = lambda p:-p[1])
    print(logits_index)

    top_k = min(top_k, len(logits))

    top_k_logits = []
    top_k_index = []

    for index, logits in logits_index:
        top_k_logits.append(logits)
        top_k_index.append(index)
        top_k-=1
        if top_k==0:
            break
    
    return top_k_logits, top_k_index
# def top_k_sampling(logits, top_k):
#     # 1. 构造 (值, 下标) 对
#     indexed = list(enumerate(logits))
#     print(indexed)
#     # 2. 按值从大到小排序
#     indexed.sort(key=lambda x: -x[1])
    
#     # 3. 取前 top_k 个
#     top_k = min(top_k, len(indexed))  # 防止 k 越界
#     top_items = indexed[:top_k]
    
#     # 4. 抽取出这 k 个的分数
#     scores = [s for _, s in top_items]
    
#     # 5. 归一化变成概率
#     total = sum(scores)
#     if total == 0:  # 边界：全0就随机选一个
#         return random.choice(top_items)[0]
    
#     probs = [s / total for s in scores]
    
#     # 6. 按概率采样
#     r = random.uniform(0, 1)
#     cumsum = 0
#     for idx, p in zip(top_items, probs):
#         cumsum += p
#         if r <= cumsum:
#             return idx[0]
    
#     # 兜底
#     return top_items[-1][0]

logits = [0.1, 0.5, 0.05, 0.3, 0.05]
k = 2

print(top_k_sampling(logits, k), end=' ')