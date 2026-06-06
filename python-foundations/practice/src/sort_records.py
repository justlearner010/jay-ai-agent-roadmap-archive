#按照字段排序

def sort_students(students, field, reverse=False):
    """
    按指定字段对学生列表排序。

    students: list[dict]
    field: 要排序的字段名，比如 "score" 或 "name"
    reverse: 是否降序，默认升序
    """
    return sorted(
        students,
        key=lambda student: student[field],
        reverse=reverse
    )

# ###期望输出
# [
#     {"name":"Bob","score":80},
#     {"name":"Tom","score":90},
#     {"name":"Alice","score":95}
# ]