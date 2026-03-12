from typing import Annotated, Sequence

from dotenv import load_dotenv
from google import genai
from IPython.display import Image, display
from langchain.chat_models import BaseChatModel
from langchain.tools import BaseTool, tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

SYSTEM_INSTRUCTION = """
あなたはReAct (Reason+Act) パターンに従うAIアシスタントです。
各ステップで必ず以下の形式で応答してください：

Thought: [現在の状況についての思考と分析]
Action: [実行するアクションの名前]
Action Input: [アクションの入力パラメータ（JSON形式）]

利用可能なアクション:
{tool_descriptions}

観察結果を受け取った後、最終的な答えが出るまでこのサイクルを繰り返してください。
"""


class ReActAgent:
    def __init__(
        self,
        model: BaseChatModel,
        tools: Sequence[BaseTool]
    ):
        self.model = model
        self.tools = tools
        self.workflow = StateGraph(MessagesState)
        self.workflow.add_node("llm_node", self._call_model)
        self.workflow.add_node("tool_node", ToolNode(tools=self.tools))
        self.workflow.add_edge(START, "llm_node")
        self.workflow.add_conditional_edges(
            "llm_node",
            tools_condition,
            {"tools": "tool_node", END: END}
        )
        self.workflow.add_edge("tool_node", "llm_node")

    def _call_model(self, state: MessagesState) -> MessagesState:
        model_with_tools = self.model.bind_tools(tools=self.tools)
        full_prompt = [
            SystemMessage(content=SYSTEM_INSTRUCTION.format(tool_descriptions="\n".join([f"{tool.name}: {tool.description}" for tool in self.tools]))),
            *state["messages"]
        ]
        llm_response = model_with_tools.invoke(full_prompt)
        return {"messages": [llm_response]}
