---
name: yes-but-comic
description: 生成「YES vs BUT」对比漫画的创意构思和图片提示词。适用场景：(1) 用户输入一个主题，要求生成对比漫画创意；(2) 用户想做对比图/反差图，需要左 YES 右 BUT 的视觉表达；(3) 用户说「帮我生成对比漫画」「Yes But 漫画」「反差图提示词」「生成创意图」或类似表达。触发条件：用户提供主题 + 要求生成对比漫画创意和出图提示词。
---

# Yes / But 对比漫画提示词生成器

输入一个主题，自动生成：对比创意（YES vs BUT）、场景设计、可直接用的提示词（中文 + 英文）。

## 风格规范（固定不变）

| 元素 | 规范 |
|------|------|
| 画风 | 简笔画风格，寥寥几笔，手绘草图感 |
| 场景 | 极简日常生活，一看就懂 |
| 人物 | 简笔小人，靠表情动作传达意思 |
| 用色 | 黑白线稿，可加一两处清淡点缀色 |
| 画面文字 | 尽可能不要，优先用视觉符号 |
| 标签 | YES / BUT 标注在画面上方 |

## 对比结构

- 画面上方标注 **YES** / **BUT**
- 左侧 vs 右侧，同一场景，左边正常，右边反转

## 创意生成原则（重点）

**反转角度要新，不要套路化。**

常见套路要避免：
- ❌ "以为是好的，实际变坏了"
- ❌ "效率反转"（AI快了/慢了）
- ❌ "成功反转成失败"

正确方向：**期望落空型反转**
- YES 描述的是对方的**口头承诺或表面现象**
- BUT 揭示的是**现实没有兑现或曲解了意思**
- 核心是"说 vs 做"或"以为 vs 实际"的落差

**BUTR 的反转应该是荒诞或黑色幽默，不是单纯"变差"**

## 场景设计原则

- 场景贴合真实生活，不过度设计
- 对比要**一眼可辨**
- 优先用视觉表达，实在必要才加少量中文
- AI 一笔能画出来的简单元素组合

## 输出模板

```
🧠 创意构思
主题：{主题}

YES：
（对方说的话 / 表面的现象，简短一句）

BUT：
（现实没兑现 / 意思被曲解，简短一句）

🎨 英文提示词
simple hand-drawn doodle comic, split panel, left panel labeled "YES" right panel labeled "BUT", {极度简单的单句场景英文}, black and white line drawing, minimalist sketch, minimal text, casual napkin-drawing vibe, clear readable contrast

🎨 中文提示词
简笔画漫画，左右分割构图，左侧标注 YES，右侧标注 BUT，{极度简单的单句场景中文}，黑白线稿，寥寥几笔，画面中无文字，靠简笔人物的动作表情差异表达对比，手绘草图感，简洁清晰
```

## 示例

**输入：**
```
主题：相亲
```

**输出：**
```
🧠 创意构思
主题：相亲

YES：
对方说"我这个人比较直接"

BUT：
然后全程没再说过第二句

🎨 英文提示词
simple hand-drawn doodle comic, split panel, left panel labeled "YES" right panel labeled "BUT", two stick figures at cafe table, left shows one figure speaking with speech bubble "I'm very direct", right shows the same two figures sitting in complete silence with tumbleweed rolling across floor, black and white line drawing, minimalist sketch, minimal text, clear contrast

🎨 中文提示词
简笔画漫画，左右分割构图，左侧标注 YES，右侧标注 BUT，两个简笔小人在咖啡桌前，左侧一人说话，泡泡里写着"我比较直接"，右侧两人全程沉默无语，地上有落叶滚过，黑白线稿，寥寥几笔，画面中无文字，靠沉默的场景对比表达反差，手绘草图感，简洁清晰
```

**输入：**
```
主题：租房
```

**输出：**
```
🧠 创意构思
主题：租房

YES：
房东说"押一付一，随时可退"

BUT：
合同上写的是"押金不退"

🎨 英文提示词
simple hand-drawn doodle comic, split panel, left panel labeled "YES" right panel labeled "BUT", two stick figures shaking hands, left shows landlord pointing at paper while renter looks happy with coin stack visible, right shows the same renter staring at contract with small text clearly stating deposit non-refundable while landlord waves goodbye, black and white line drawing, minimalist sketch, minimal text, clear contrast

🎨 中文提示词
简笔画漫画，左右分割构图，左侧标注 YES，右侧标注 BUT，两个简笔小人在握手，左侧房东指着合同，租房人看着手里钱币表情很开心，右侧同一租房人盯着合同看小字"押金不退"，房东在挥手告别，黑白线稿，寥寥几笔，画面中无文字，靠两人的动作表情和钱币细节对比表达反差，手绘草图感，简洁清晰
```
