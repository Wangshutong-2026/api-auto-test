# 基于 Pytest + Requests 的接口自动化测试框架

## 📌 项目简介
本项目是一个从零搭建的接口自动化测试框架。针对真实业务场景（如：论坛登录、多接口关联），实现了数据驱动、接口统一封装、Token 动态提取与传递，并集成了 Allure 可视化测试报告，旨在提升接口回归测试的效率。

## 🛠️ 技术栈
*   **开发语言**：Python 3.14
*   **测试框架**：Pytest
*   **网络请求**：Requests (Session 鉴权保持)
*   **数据驱动**：YAML
*   **测试报告**：Allure-pytest
*   **其他**：正则表达式 (Token提取)、Logging日志记录

## 📂 项目结构
```text
api-auto-test/
├── basics/                 # 基础语法练习代码（略）
├── commons/                # 公共方法
├── data/                   # 测试数据文件
├── docs/                   # 学习笔记与文档
├── logs/                   # 运行日志存放
├── public/                 # 核心封装层
│   ├── request_util.py     # Requests 二次封装（支持 Session 保持）
│   └── yaml_util.py        # YAML 文件读写工具
├── report/                 # Allure 报告生成目录
├── tests/                  # 测试用例层
│   ├── conftest.py         # Pytest 共享夹具（Fixture）
│   ├── login_data.yaml     # 登录业务测试数据（正向/逆向）
│   └── test_business_flow.py # 核心业务流测试用例
├── allure_report.png       # 测试报告截图展示
├── pytest.ini              # Pytest 全局配置文件
├── requirements.txt        # 项目依赖包列表
└── run.py                  # 测试运行入口