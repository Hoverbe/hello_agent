import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from autogen_core.models import ModelInfo, ModelFamily


# 加载 .env 文件中的环境变量
load_dotenv()
def create_openai_model_client():
    """创建并配置 OpenAI 模型客户端"""
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL_ID"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        model_info=ModelInfo(
            vision=False,
            function_calling=True,  # 如果你的模型支持工具调用
            json_output=True,  # 如果你的模型支持 JSON 模式
            family=ModelFamily.UNKNOWN,  # 或 ModelFamily.QWEN
        ),
    )
