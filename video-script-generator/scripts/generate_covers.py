#!/usr/bin/env python3
import re
import os

CSS_TEMPLATE = """
:root {
  --bg-color: #0f1f38;
  --accent-cyan: #5BA8A8;
  --text-color: #E8F0F0;
  --highlight-color: var(--accent-cyan);
  --muted-color: #2a4a5a;
  --bg-gradient-start: #0f1f38;
  --bg-gradient-mid: #0d1a2e;
  --bg-gradient-end: #08101f;
  --bg-glow: rgba(91, 168, 168, 0.06);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Noto Serif SC', 'SimSun', serif;
  background: #1a1a2e;
  color: var(--text-color);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

h1 { font-size: 16px; color: #666; margin-bottom: 20px; font-weight: 400; letter-spacing: .1em; }

.preview-container { position: relative; overflow: hidden; }

.preview-4x3 { width: 540px; height: 405px; position: relative; background: var(--bg-color); overflow: hidden; display: none; }
.preview-3x4 { width: 360px; height: 480px; position: relative; background: var(--bg-color); overflow: hidden; }
.preview-1x1 { width: 480px; height: 480px; position: relative; background: var(--bg-color); overflow: hidden; display: none; }
.preview-16x9 { width: 640px; height: 360px; position: relative; background: var(--bg-color); overflow: hidden; display: none; }

.size-tabs { display: flex; gap: 10px; margin-bottom: 20px; }
.size-tab { padding: 8px 16px; border: 1px solid #333; background: transparent; color: #666; cursor: pointer; font-size: 12px; letter-spacing: .1em; border-radius: 4px; transition: all 0.2s; }
.size-tab:hover { border-color: var(--accent-cyan); color: var(--accent-cyan); }
.size-tab.active { background: var(--accent-cyan); color: var(--bg-color); border-color: var(--accent-cyan); }

.slide { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0; opacity: 0; pointer-events: none; transition: opacity 0.4s ease; overflow: hidden; }
.slide.active { opacity: 1; pointer-events: auto; }

.slide::before { content: ""; position: absolute; inset: 0; background: radial-gradient(ellipse 70% 50% at 50% 0%, rgba(var(--bg-glow), 1) 0%, transparent 60%), radial-gradient(ellipse 50% 40% at 100% 100%, rgba(91, 168, 168, 0.04) 0%, transparent 50%), linear-gradient(180deg, var(--bg-gradient-start) 0%, var(--bg-gradient-mid) 50%, var(--bg-gradient-end) 100%); z-index: 0; }

.accent-line { position: absolute; top: 0; left: 40px; right: 40px; height: 2px; background: linear-gradient(90deg, transparent 0%, rgba(91, 168, 168, 0.15) 10%, rgba(91, 168, 168, 0.5) 35%, rgba(91, 168, 168, 0.8) 50%, rgba(91, 168, 168, 0.5) 65%, rgba(91, 168, 168, 0.15) 90%, transparent 100%); z-index: 2; }
.accent-line::before { content: ""; position: absolute; left: 0; top: -3px; width: 8px; height: 8px; border-radius: 50%; background: var(--accent-cyan); opacity: 0.7; }
.accent-line::after { content: ""; position: absolute; right: 0; top: -3px; width: 8px; height: 8px; border-radius: 50%; background: var(--accent-cyan); opacity: 0.7; }

.bottom-line { position: absolute; bottom: 0; left: 40px; right: 40px; height: 2px; background: linear-gradient(90deg, transparent 0%, rgba(91, 168, 168, 0.15) 10%, rgba(91, 168, 168, 0.5) 35%, rgba(91, 168, 168, 0.8) 50%, rgba(91, 168, 168, 0.5) 65%, rgba(91, 168, 168, 0.15) 90%, transparent 100%); z-index: 2; }
.bottom-line::before { content: ""; position: absolute; left: 0; top: -3px; width: 8px; height: 8px; border-radius: 50%; background: var(--accent-cyan); opacity: 0.5; }
.bottom-line::after { content: ""; position: absolute; right: 0; top: -3px; width: 8px; height: 8px; border-radius: 50%; background: var(--accent-cyan); opacity: 0.5; }

.slide::after { content: ""; position: absolute; bottom: 0; left: 0; right: 0; height: 20%; background: linear-gradient(0deg, rgba(8, 16, 31, 0.6) 0%, transparent 100%); z-index: 1; pointer-events: none; }

/* 横屏（4x3、16x9）不加装饰线，避免被抖音误判为截屏 */
.preview-4x3 .accent-line,
.preview-4x3 .bottom-line,
.preview-16x9 .accent-line,
.preview-16x9 .bottom-line {
  display: none;
}

.main-title { font-family: 'Noto Serif SC', 'SimSun', serif; font-size: 38px; font-weight: 700; text-align: center; line-height: 1.15; letter-spacing: 0.5px; position: relative; z-index: 5; }
.main-title .line { display: block; }
.main-title .line:first-child { font-size: 1.05em; }
.main-title .line:nth-child(2) { font-size: 0.95em; }
.main-title .line:last-child { font-size: 0.92em; opacity: 0.85; }
.main-title .hl { color: var(--highlight-color); }

.title-divider { width: 80px; height: 2px; background: linear-gradient(90deg, transparent 0%, rgba(91, 168, 168, 0.6) 30%, var(--accent-cyan) 50%, rgba(91, 168, 168, 0.6) 70%, transparent 100%); margin: 14px auto; opacity: 0.6; }

.course-info { position: absolute; bottom: 28px; display: flex; flex-direction: column; align-items: center; gap: 8px; z-index: 10; }
.course-num { display: inline-flex; align-items: center; justify-content: center; padding: 6px 18px; border-radius: 4px; font-size: 18px; font-weight: 700; font-family: 'Noto Serif SC', serif; color: var(--accent-cyan); letter-spacing: 2px; opacity: 0.75; }
.course-type { display: inline-flex; align-items: center; justify-content: center; padding: 6px 18px; border: 1px solid rgba(91, 168, 168, 0.25); border-radius: 50px; font-size: 12px; font-weight: 500; color: var(--text-color); letter-spacing: 2px; opacity: 0.55; }

.controls { display: flex; align-items: center; gap: 20px; margin-top: 20px; }
.nav-btn { width: 40px; height: 40px; border: 1px solid #333; background: transparent; color: #666; cursor: pointer; border-radius: 50%; font-size: 16px; display: flex; align-items: center; justify-content: center; transition: all 0.2s; }
.nav-btn:hover { border-color: var(--accent-cyan); color: var(--accent-cyan); }
.dots { display: flex; gap: 8px; }
.dot { width: 8px; height: 8px; border-radius: 50%; background: #333; cursor: pointer; transition: all 0.2s; }
.dot:hover { background: #555; }
.dot.active { background: var(--accent-cyan); }
.export-btn { padding: 10px 24px; background: var(--accent-cyan); color: var(--bg-color); border: none; cursor: pointer; font-size: 14px; font-weight: 700; font-family: 'Noto Serif SC', serif; border-radius: 4px; margin-left: 20px; transition: all 0.2s; }
.export-btn:hover { opacity: 0.85; }

.preview-16x9 .slide { flex-direction: row; padding: 0 50px 0 60px; gap: 50px; }
.preview-16x9 .slide-content { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 16px; }
.preview-16x9 .main-title { font-size: 44px; text-align: left; }
.preview-16x9 .title-divider { margin: 10px 0; }
.preview-16x9 .course-info { position: relative; bottom: auto; flex-direction: row; gap: 12px; }

.preview-1x1 .slide { padding: 40px 35px; }
.preview-1x1 .main-title { font-size: 34px; }
.preview-1x1 .course-info { bottom: 35px; }

.preview-4x3 .slide { flex-direction: row; padding: 0 45px 0 55px; gap: 35px; }
.preview-4x3 .slide-content { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 14px; }
.preview-4x3 .main-title { font-size: 38px; text-align: left; }
.preview-4x3 .title-divider { margin: 10px 0; }
.preview-4x3 .course-info { position: relative; bottom: auto; }

.preview-3x4 .slide { padding: 0 30px; }
"""

JS_TEMPLATE = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
let currentIndex = 0;
const TOTAL_SLIDES = 3;
const dots = document.querySelectorAll('.dot');

function getActiveContainer() {
  const size = document.querySelector('.size-tab.active').dataset.size;
  return document.getElementById('preview-' + size);
}
function getSlides() {
  return getActiveContainer().querySelectorAll('.slide');
}
function showSlide(index) {
  const slides = getSlides();
  slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
  dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
  currentIndex = index;
}

document.getElementById('prevBtn').addEventListener('click', () => showSlide((currentIndex - 1 + TOTAL_SLIDES) % TOTAL_SLIDES));
document.getElementById('nextBtn').addEventListener('click', () => showSlide((currentIndex + 1) % TOTAL_SLIDES));
dots.forEach(dot => dot.addEventListener('click', () => showSlide(parseInt(dot.dataset.index))));
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') showSlide((currentIndex - 1 + TOTAL_SLIDES) % TOTAL_SLIDES);
  else if (e.key === 'ArrowRight') showSlide((currentIndex + 1) % TOTAL_SLIDES);
});

document.querySelectorAll('.size-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.size-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const size = tab.dataset.size;
    ['4x3', '3x4', '1x1', '16x9'].forEach(s => document.getElementById('preview-' + s).style.display = s === size ? 'block' : 'none');
    showSlide(currentIndex);
  });
});

document.getElementById('exportBtn').addEventListener('click', async () => {
  const size = document.querySelector('.size-tab.active').dataset.size;
  const sizeNames = { '4x3': '4-3', '3x4': '3-4', '1x1': '1-1', '16x9': '16-9' };
  try {
    const canvas = await html2canvas(document.getElementById('preview-' + size), { scale: 4, backgroundColor: '#0f1f38', logging: false });
    const link = document.createElement('a');
    link.download = '{DOWNLOAD_PREFIX}-' + sizeNames[size] + '-推荐' + (currentIndex + 1) + '.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  } catch (err) { alert('导出失败: ' + err.message); }
});
</script>
"""

def make_line_span(text):
    """Wrap each line in <span class="line"> and handle hl markup."""
    parts = re.split(r'(<span class="hl">.*?</span>)', text)
    result = []
    for part in parts:
        if part.startswith('<span class="hl">'):
            result.append(part)
        else:
            lines = part.strip().split('\n')
            for line in lines:
                if line:
                    result.append(f'<span class="line">{line}</span>')
    return ''.join(result)

def build_slides(slides_data, is_horizontal=False):
    """Build slide HTML for all 4 sizes."""
    slides_html = {}
    for size in ['4x3', '3x4', '1x1', '16x9']:
        container = [f'  <!-- ========== {size} ========== -->', f'  <div id="preview-{size}" class="preview-{size}">', '    <div class="accent-line"></div>', '    <div class="bottom-line"></div>']
        for i, (title_text, course_num, course_type) in enumerate(slides_data):
            line_html = make_line_span(title_text)
            active = ' active' if i == 0 else ''
            if is_horizontal or size in ['4x3', '16x9']:
                container.append(f'    <div class="slide{active}" data-index="{i}">')
                container.append(f'      <div class="slide-content"><div class="main-title">{line_html}</div><div class="title-divider"></div></div>')
                container.append(f'      <div class="course-info"><div class="course-num">{course_num}</div><div class="course-type">{course_type}</div></div>')
                container.append('    </div>')
            else:
                container.append(f'    <div class="slide{active}" data-index="{i}">')
                container.append(f'      <div class="main-title">{line_html}</div>')
                container.append('      <div class="title-divider"></div>')
                container.append(f'      <div class="course-info"><div class="course-num">{course_num}</div><div class="course-type">{course_type}</div></div>')
                container.append('    </div>')
        container.append('  </div>')
        slides_html[size] = '\n'.join(container)
    return slides_html

def generate_cover(course_dir, course_name, slides_data, download_prefix, course_num_display):
    """Generate a cover.html file."""
    is_horizontal = False

    slides_html = build_slides(slides_data, is_horizontal)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>封面预览 — {course_name}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
<style>
{CSS_TEMPLATE}
</style>
</head>
<body>

<h1>封面预览 — {course_name}</h1>

<div class="size-tabs">
  <button class="size-tab" data-size="4x3">4:3 Facebook</button>
  <button class="size-tab active" data-size="3x4">3:4 小红书</button>
  <button class="size-tab" data-size="1x1">1:1 Instagram</button>
  <button class="size-tab" data-size="16x9">16:9 YouTube</button>
</div>

<div class="preview-container">
{slides_html['4x3']}
{slides_html['3x4']}
{slides_html['1x1']}
{slides_html['16x9']}
</div>

<div class="controls">
  <button class="nav-btn" id="prevBtn">◀</button>
  <div class="dots">
    <div class="dot active" data-index="0"></div>
    <div class="dot" data-index="1"></div>
    <div class="dot" data-index="2"></div>
  </div>
  <button class="nav-btn" id="nextBtn">▶</button>
  <button class="export-btn" id="exportBtn">导出当前</button>
</div>

{JS_TEMPLATE.replace('{DOWNLOAD_PREFIX}', download_prefix)}

</body>
</html>'''

    out_path = os.path.join(course_dir, 'cover.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Generated: {out_path}')

def main():
    base = '/Users/xiaoxiang/Documents/self-media/冥想/output'

    courses = [
        ('01-归零', '01归零', '归零', [
            ('精力越来越差\n专注力越来越差\n压力越来越大\n<span class="hl">——这不是你一个人的问题</span>', '01归零', '先导片'),
            ('你的大脑\n还停留在原始社会\n<span class="hl">你知道吗？</span>', '01归零', '先导片'),
            ('全球已有<span class="hl">2亿人</span>\n在练习冥想\n你还在犹豫什么？', '01归零', '先导片'),
        ], '归零'),

        ('02-与脑共处', '02与脑共处', '与脑共处', [
            ('大脑里有个\n"刀子嘴豆腐心"的朋友\n它一直在骗你', '02与脑共处', '讲解'),
            ('为什么你总是\n焦虑紧张？\n答案在大脑里', '02与脑共处', '讲解'),
            ('成年后大脑还能改变\n<span class="hl">你知道吗？</span>', '02与脑共处', '讲解'),
        ], '与脑共处'),

        ('03-天时地利', '03天时地利', '天时地利', [
            ('大多数自称冥想的人\n都是<span class="hl">三天打鱼两天晒网</span>', '03天时地利', '讲解'),
            ('冥想能不能坚持\n就看这一点', '03天时地利', '讲解'),
            ('手机是冥想最大的敌人\n<span class="hl">你知道吗？</span>', '03天时地利', '讲解'),
        ], '天时地利'),

        ('04-探索身体', '04探索身体', '探索身体', [
            ('唯一糟糕的冥想\n是没有做的冥想', '04探索身体', '跟练'),
            ('第一次冥想\n不知道该想什么？', '04探索身体', '跟练'),
            ('在浮躁的时代\n能把注意力转向内心\n已经是一件难得了', '04探索身体', '跟练'),
        ], '探索身体'),

        ('05-身体觉醒', '05身体觉醒', '身体觉醒', [
            ('你多久没有\n关注过自己的身体了？', '05身体觉醒', '讲解'),
            ('身体必须先有感受\n注意力才能捕捉到', '05身体觉醒', '讲解'),
            ('冥想不是让你放空\n是让你<span class="hl">回到身体里</span>', '05身体觉醒', '讲解'),
        ], '身体觉醒'),

        ('06-躺平冥想', '06躺平冥想', '躺平冥想', [
            ('躺着冥想\n睡着了也算<span class="hl">练到了</span>', '06躺平冥想', '跟练'),
            ('午休用它代替\n晚上睡得更香', '06躺平冥想', '跟练'),
            ('唯一糟糕的冥想\n是没有做的冥想', '06躺平冥想', '跟练'),
        ], '躺平冥想'),

        ('07-先动后静', '07先动后静', '先动后静', [
            ('坐不住？\n<span class="hl">先动后静</span>\n冥想从此不难', '07先动后静', '跟练'),
            ('拉伸后再冥想\n感觉完全不一样', '07先动后静', '跟练'),
            ('冥想和运动是绝配', '07先动后静', '跟练'),
        ], '先动后静'),

        ('08-四两拨千斤', '08四两拨千斤', '四两拨千斤', [
            ('冥想打瞌睡\n不是你的问题\n是身体在说话', '08四两拨千斤', '讲解'),
            ('冥想是<span class="hl">改善生活</span>的第一步\n不是最后一招', '08四两拨千斤', '讲解'),
            ('你以为冥想是休息\n其实它在<span class="hl">揭示问题</span>', '08四两拨千斤', '讲解'),
        ], '四两拨千斤'),

        ('09-先紧后松', '09先紧后松', '先紧后松', [
            ('<span class="hl">先紧后松</span>\n冥想的另一种打开方式', '09先紧后松', '跟练'),
            ('细微的舒展动作\n比坐着放空更有效', '09先紧后松', '跟练'),
            ('通过收紧来放松\n你试过吗？', '09先紧后松', '跟练'),
        ], '先紧后松'),

        ('10-坐法', '10坐法', '坐法', [
            ('冥想用什么姿势最好？\n坐着、躺着还是盘腿？', '10坐法', '讲解'),
            ('舒服是最重要的\n冥想姿势原则', '10坐法', '讲解'),
            ('冥想三天了\n你坐得舒服吗？', '10坐法', '讲解'),
        ], '坐法'),

        ('11-动中冥想', '11动中冥想', '动中冥想', [
            ('活动身体时\n也能冥想\n你试过吗？', '11动中冥想', '跟练'),
            ('<span class="hl">动中冥想</span>\n在动作里找到平静', '11动中冥想', '跟练'),
            ('不用坐着\n活动中也能\n进入冥想状态', '11动中冥想', '跟练'),
        ], '动中冥想'),

        ('12-正念与觉知', '12正念与觉知', '正念与觉知', [
            ('<span class="hl">正念</span>是什么意思？\n冥想中最容易被误解的概念', '12正念与觉知', '讲解'),
            ('<span class="hl">正念</span>就是什么都不想？\n你可能误解了', '12正念与觉知', '讲解'),
            ('觉知和专注的区别\n<span class="hl">90%的人</span>不知道', '12正念与觉知', '讲解'),
        ], '正念与觉知'),

        ('13-要点梳理', '13要点梳理', '要点梳理', [
            ('完成了第一阶段\n<span class="hl">恭喜你</span>', '13要点梳理', '小结'),
            ('冥想最难的部分\n不是技巧\n是愿意坐下来', '13要点梳理', '小结'),
            ('第一阶段踩过的坑\n你中了<span class="hl">几个</span>？', '13要点梳理', '小结'),
        ], '要点梳理'),
    ]

    print('Generating 13 course covers with new styles...\n')
    for course_dir, course_num_display, download_prefix, slides_data, course_name in courses:
        course_path = os.path.join(base, course_dir)
        generate_cover(course_path, course_name, slides_data, download_prefix, course_num_display)

    print('\nDone!')

if __name__ == '__main__':
    main()