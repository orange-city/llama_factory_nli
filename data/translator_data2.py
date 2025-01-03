import pandas as pd
import json
import os


def csv_to_json(csv_file_path, json_file_path):
    """
    将包含 'sentence1'、'sentence2' 和 'label' 列的 CSV 文件转换为指定格式的 JSON 文件。

    JSON格式示例：
    {
        "instruction": "Consider the following two sentences:

        Sentence1: Hence, tasks can be related through the paths on the graph that links their nodes even when they share few output classes.

        Sentence2: we use linear transformation for g(·) and h(·).

        What is the semantic relation between Sentence1 and Sentence2? Choose from the following options: 1. Entailment, 2. Reasoning, 3. Contrasting, 4. Neutral.",

        "input": "",

        "output": "neutral"
    },

    参数:
    - csv_file_path: 输入的 CSV 文件路径。
    - json_file_path: 输出的 JSON 文件路径。
    """

    # 检查CSV文件是否存在
    if not os.path.isfile(csv_file_path):
        print(f"错误: 找不到文件 {csv_file_path}")
        return

    try:
        # 读取CSV文件
        df = pd.read_csv(csv_file_path)
    except pd.errors.EmptyDataError:
        print(f"错误: 文件 {csv_file_path} 是空的")
        return
    except pd.errors.ParserError:
        print(f"错误: 文件 {csv_file_path} 解析失败")
        return

    # 检查必要的列是否存在
    required_columns = {'sentence1', 'sentence2', 'label'}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        print(f"错误: CSV文件缺少以下列: {', '.join(missing)}")
        return

    # 标签映射（如果标签是数字）
    label_mapping = {
        '1': 'entailment',
        '2': 'reasoning',
        '3': 'contrasting',
        '4': 'neutral'
    }

    # 初始化一个列表来存储JSON对象
    json_list = []

    # 定义静态的instruction字符串模板
    instruction_template = (
        "Consider the following two sentences:\n\n"
        "Sentence1: {sentence1}\n\n"
        "Sentence2: {sentence2}\n\n"
        "What is the semantic relation between Sentence1 and Sentence2? Choose from the following options: 1. Entailment, 2. Reasoning, 3. Contrasting, 4. Neutral."
    )

    # 遍历每一行并构建JSON对象
    for index, row in df.iterrows():
        sentence1 = str(row['sentence1']).strip()
        sentence2 = str(row['sentence2']).strip()
        label = str(row['label']).strip().lower()  # 转换为小写

        # 如果标签是数字，进行映射
        if label in label_mapping:
            label = label_mapping[label]

        # 构建instruction字符串
        instruction = instruction_template.format(sentence1=sentence1, sentence2=sentence2)

        # 构建JSON对象
        json_obj = {
            "instruction": instruction,
            "input": "",
            "output": label
        }

        json_list.append(json_obj)

    # 将JSON对象列表写入JSON文件
    try:
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_list, json_file, ensure_ascii=False, indent=4)
        print(f"成功: 已将 CSV 数据转换并保存到 {json_file_path}")
    except IOError as e:
        print(f"错误: 无法写入文件 {json_file_path}。错误信息: {e}")


if __name__ == "__main__":
    # 定义输入和输出文件路径
    input_csv = './MSciNLI/train.csv'
    output_json = './MSciNLI/train2.json'
    # 调用转换函数
    csv_to_json(input_csv, output_json)

    input_csv = './MSciNLI/dev.csv'
    output_json = './MSciNLI/dev2.json'
    csv_to_json(input_csv, output_json)

    input_csv = './MSciNLI/test.csv'
    output_json = './MSciNLI/test2.json'
    csv_to_json(input_csv, output_json)
