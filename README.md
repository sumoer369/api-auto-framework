# 接口自动化测试框架

## 📖 项目简介
基于 Python + Pytest + Requests + YAML 搭建的接口自动化测试框架，采用分层设计，实现数据驱动与持续集成。

## 🛠️ 技术栈
- 测试框架：Python、Pytest、Requests
- 数据驱动：YAML
- 持续集成：GitHub Actions

## 📂 项目结构
- `config/`：多环境配置
- `api/`：接口封装层
- `testcases/`：测试用例层
- `data/`：YAML测试数据
- `utils/`：请求与断言工具
- `reports/`：测试报告

## 🚀 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 执行测试：`pytest`

## 💡 项目亮点
- 分层设计：配置、接口、数据、用例分离，易维护
- 数据驱动：YAML管理测试数据，新增用例不改代码
- CI集成：GitHub Actions自动触发测试