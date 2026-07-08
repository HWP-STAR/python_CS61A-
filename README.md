# CS61A 课程学习代码

UC Berkeley [CS 61A: Structure and Interpretation of Computer Programs](https://cs61a.org/) 课程作业与练习代码。

## 目录结构

### 大项目

| 目录 | 说明 |
|------|------|
| `hog/` | **The Game of Hog** — 双人骰子策略游戏，率先达到 100 分者获胜。包含 Boar Brawl、Sus Fuss 等特殊规则，实现了游戏模拟、骰子机制和 AI 策略。 |
| `ants/` | **Ants vs. SomeBees** — 塔防游戏（仿 Plants vs. Zombies）。蚂蚁守卫蚁穴对抗入侵的蜜蜂。使用面向对象编程（`ThrowerAnt`、`FireAnt`、`WallAnt` 等），包含 Flask + Socket.IO 网页 GUI。 |
| `cats/` | **Cats: Typing Test + Autocorrect** — 打字速度测试应用，包含基于 QWERTY 键盘距离的自动纠错功能，配有网页 GUI。 |

### 作业

| 目录 | 内容 |
|------|------|
| `hw01/` | 控制流、高阶函数（`a_plus_abs_b`、`hailstone` 等） |
| `hw03/` | 递归、树递归 |
| `hw04/` | 数据结构、序列 |
| `hw05/` | 面向对象编程 |

### 实验

| 目录 | 内容 |
|------|------|
| `lab00/` | Python 基础、表达式 |
| `lab01/` | 条件语句、调试 |
| `lab02/` | 高阶函数 |
| `lab03/` | 列表、列表推导式 |
| `lab04/` | 递归 |
| `lab05/` | 列表修改、迭代器 |
| `lab06/` | 面向对象编程、类（包含卡牌游戏模拟） |

### 讨论课

- `discussion1.py` ~ `discussion7.py` — 每周讨论课练习题（质数判断、fizzbuzz、递归等）

### 其他

- `func.py`、`recursive_func.py` — 个人补充练习

## 环境要求

- Python 3.8+
- 各项目使用 `ok` 自动评分系统（已内置于各项目目录中）

## 运行

每个项目目录下包含独立的运行方式，例如：

```bash
# Hog 命令行版
python hog/hog/hog.py

# Hog GUI 版
python hog/hog/hog_gui.py

# Ants GUI 版
cd ants && python ants/gui.py

# Cats GUI 版
python cats/cats/cats_gui.py
```

运行测试：

```bash
python ok
```

## 课程信息

- 课程主页：<https://cs61a.org/>
- 课程使用 Python 3 讲解编程语言的设计与实现，涵盖函数式编程、数据抽象、面向对象编程、解释器构建和 SQL。
