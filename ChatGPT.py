
import openai
import os
#import openai_secret_manager

# 获取 API 密钥
#secrets = openai_secret_manager.get_secret("OPENAI_API_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 调用 OpenAI API
prompt = "帮我写个IOT的技术规格说明书"
model = "text-davinci-002"
temperature = 0.5
max_tokens = 10
response = openai.Completion.create(
    engine="davinci-002",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    model=model,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0,
    response_format="json",
    turbo=True,
    use_davinci_3_5=True,
)
print(response.choices[0].text)
