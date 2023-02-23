import openai
import os

# 设置 API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 输入文本
prompt = "企业数字化的核心是什么"


# 生成文本
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.7,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 输出生成的文本
print(response["choices"][0]["text"].strip())