import pandas as pd
import json

def csv_to_json(csv_file_path, json_file_path):
    """
    将包含'sentence1'、'sentence2'和'label'列的CSV文件转换为指定格式的JSON文件。

    参数:
    - csv_file_path: 输入的CSV文件路径。
    - json_file_path: 输出的JSON文件路径。
    """

    try:
        # 读取CSV文件
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"错误: 找不到文件 {csv_file_path}")
        return
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

    # 初始化一个列表来存储JSON对象
    json_list = []

    # 定义静态的instruction字符串
    instruction = (
        "Consider the following two sentences. What is the semantic relation between Sentence1 and Sentence2? "
        "Choose from the following options: 1. Entailment, 2. Reasoning, 3. Contrasting, 4. Neutral."
    )

    # 遍历每一行并构建JSON对象
    for index, row in df.iterrows():
        sentence1 = str(row['sentence1']).strip()
        sentence2 = str(row['sentence2']).strip()
        label = str(row['label']).strip().lower()  # 转换为小写

        # 构建input字符串
        input_str = f"Sentence1: {sentence1} Sentence2: {sentence2}."

        # 构建JSON对象
        json_obj = {
            "instruction": instruction,
            "input": input_str,
            "output": label
        }

        json_list.append(json_obj)

    # 将JSON对象列表写入JSON文件
    try:
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_list, json_file, ensure_ascii=False, indent=4)
        print(f"成功: 已将CSV数据转换并保存到 {json_file_path}")
    except IOError as e:
        print(f"错误: 无法写入文件 {json_file_path}。错误信息: {e}")

if __name__ == "__main__":
    # 定义输入和输出文件路径
    input_csv = './MSciNLI/train.csv'
    output_json = './MSciNLI/train.json'

    # 调用转换函数
    csv_to_json(input_csv, output_json)

    input_csv = './MSciNLI/dev.csv'
    output_json = './MSciNLI/dev.json'
    csv_to_json(input_csv, output_json)

    input_csv = './MSciNLI/test.csv'
    output_json = './MSciNLI/test.json'
    csv_to_json(input_csv, output_json)
