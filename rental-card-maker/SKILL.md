# rental-card-maker

> **一句话**：将话题内容转换为信息图风格的多卡系列 PNG

**用途**：把任意「利他型」话题（比如租房指南、买房避坑）做成小红书风格的多卡片内容

**输入**：话题标题 + 内容素材（文本/文件/URL）
**输出**：N 张 1080×1440 PNG（3:4竖版），自动根据内容量和类型决定页数（4-8页）

**触发**：发话题+素材，说"帮我生成卡片"

## 内容输入

用户发送：
- 话题标题（如「租房看房时必查的隐蔽问题」）
- 内容素材（粘贴文本 / 文件路径 / URL）

## 输出规格

- **格式**：N张 1080×1440 PNG，3:4竖版（页数由内容决定）
- **风格**：信息图风格（锐利色调，噪点纹理，衬线标题+无衬线正文，深色数据卡）
- **视觉语言**：
  - 背景：#EDEDF0（灰白）
  - 强调色：#D93025（红）
  - 深色：#2D2926
  - 字体：DM Serif Display + DM Sans + KingHwa_OldSong
  - 每页有 grain 纹理（SVG filter）
- **无Footer/无Logo**：内容干净，末页结尾用 end mark ∎

## 输出文件

- `/tmp/ljg_rental_card_1.html` ~ `/tmp/ljg_rental_card_N.html`
- `~/Downloads/rental_check_1.png` ~ `rental_check_N.png`

## 截图工具

```bash
cd ~/.claude/skills/ljg-card && node assets/capture.js <html> <png> 1080 1440
```

## 页面结构（动态规划）

根据内容自然切分，参考规则：

| 内容类型 | 建议页数 | 分布 |
|---------|---------|------|
| 清单式（8-15项） | 4-6页 | 1封面 + N内容 + 1清单 |
| 对比式（A vs B） | 4-5页 | 1封面 + A面 + B面 + 总结 |
| 流程式（步骤） | 5-7页 | 1封面 + 每步骤1页 + 总结 |
| 混合式（多分类） | 5-8页 | 1封面 + 每类1页 + 快速检查 |

**切分原则**：
- 封面页（Page 1）：标题 + hook + 核心数据锚点
- 内容页（Page 2~N-1）：每页一个主题块，4-8个条目，条目含：名称 + 验证方法 + 严重程度标签
- 末页（最后一页）：快速检查清单（3-8项可操作步骤）+ 核心提示框 + end mark ∎
- 单页内容不过挤也不过散：总条目数 ÷ (页数-2) ≈ 4-8 项/页

**末页清单建议结构**：
- 3-8项快速可执行检查项（带emoji图标）
- 一个核心提示框（深色背景，白字，强调最关键的行动）
- end mark `∎` 在右下角

## 视觉模板（每页通用）

```css
/* 固定变量 */
--bg: #EDEDF0
--pink: #D93025
--ink: #2D2926
--ink-light: #5C5350
--white: #FFFFFF
--serif: 'DM Serif Display', 'KingHwa_OldSong', Georgia, 'Noto Serif SC', serif
--sans: 'DM Sans', 'KingHwa_OldSong', -apple-system, 'PingFang SC', system-ui, sans-serif

/* 标签 */
.hero-tag：背景 --ink，白字，字号18px，圆角4px

/* 标题 */
.hero-title：字号80px，行高1.08，letter-spacing -0.03em，--serif

/* 数据卡 */
.hero-right：背景 --ink，圆角14px，内有 stat-number（96px，--pink）

/* 严重程度 */
.severity-high：文字 --pink，背景 rgba(217,48,37,0.08)
.severity-mid：文字 #e07b2a，背景 rgba(224,123,42,0.08)
.severity-low：文字 #5a9c6e，背景 rgba(90,156,110,0.08)

/* 提示框 */
.highlight-box：背景 --ink，白字，圆角14px
.highlight-box.featured：背景 --pink
```

## 执行流程

1. **分析素材**：提取话题核心、分支主题、关键数据点，判断总条目数和主题数
2. **规划页数**：总条目数 ÷ 6（基准）= 初步页数，调整至4-8页范围内
3. **分配内容**：封面占1页，末页占1页，中间页按主题/分类均匀分配
4. **生成HTML**：每个HTML写完整样式，直接写入 `/tmp/ljg_rental_card_N.html`
5. **并行截图**：N个 capture 命令，输出到 `~/Downloads/rental_check_N.png`
6. **更新选题库**：`docs/content-topics/房产利他内容选题库.md` 标记完成

## 触发条件

当用户发送话题要求"生成卡片"时，自动执行本skill。
只需发话题和素材，无需指定页数。