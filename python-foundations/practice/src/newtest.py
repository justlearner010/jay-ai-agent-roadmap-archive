#去重

nums =[1,2,2,3,3,4]

result = list(dict.fromkeys(nums))

print(result)
# 手动输入 【1，2，2，3，3，4】
#期望输出 [1,2,3,4]

#函数改写
def remove_duplicates(nums):
    return list(dict.fromkeys(nums))


#分组
words = ["apple","banana","avocado","blueberry"]

groups = {}

for word in words:
    first  = word[0]

    if first not in groups:
        groups[first] = []

    groups[first].append(word)

print(groups)


#两数之和
#采用dict降低查找次数

nums=[2,7,11,15]
target = 9

seen= {}

for i ,num in enumerate(nums):
    need = target - num
    if need in seen:
        print([seen[need],i])
        break
    seen[num] = i

#期望输出：[0,1]

#按照字段排序

students = [
    {"name": "Tom", "score": 90},
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 80}
]

result = sorted(
    students,
    key = lambda student : student["score"],
    reverse= False
)

print(result)

# ###期望输出
# [
#     {"name":"Bob","score":80},
#     {"name":"Tom","score":90},
#     {"name":"Alice","score":95}
# ]