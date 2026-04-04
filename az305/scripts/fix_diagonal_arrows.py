"""Convert diagonal <line> arrows to orthogonal <path> in vol3/4/5 arch diagrams."""
import re, json

# Match any <line .../> regardless of attribute order or / inside url()
LINE_PAT = re.compile(r'<line\b((?:[^/]|/(?!>))*)/>', re.DOTALL)

def _coord(tag, name):
    m = re.search(rf'\b{name}="(\d+)"', tag)
    return m.group(1) if m else None

def line_to_ortho_path(m):
    tag = m.group(0)
    x1s = _coord(tag, 'x1'); y1s = _coord(tag, 'y1')
    x2s = _coord(tag, 'x2'); y2s = _coord(tag, 'y2')
    if None in (x1s, y1s, x2s, y2s):
        return tag
    x1, y1, x2, y2 = int(x1s), int(y1s), int(x2s), int(y2s)
    if x1 == x2 or y1 == y2:
        return tag  # already orthogonal
    # Bend: go horizontal first, then vertical
    d = f"M{x1},{y1} L{x2},{y1} L{x2},{y2}"
    attrs = m.group(1)
    attrs = re.sub(r'\bx1="[^"]*"', '', attrs)
    attrs = re.sub(r'\by1="[^"]*"', '', attrs)
    attrs = re.sub(r'\bx2="[^"]*"', '', attrs)
    attrs = re.sub(r'\by2="[^"]*"', '', attrs)
    attrs = attrs.strip()
    return f'<path d="{d}" fill="none" {attrs}/>'

def fix_svgs(text):
    return LINE_PAT.sub(line_to_ortho_path, text)

def count_diag(text):
    return sum(
        1 for x in LINE_PAT.finditer(text)
        if _coord(x.group(0), 'x1') and
           _coord(x.group(0), 'x1') != _coord(x.group(0), 'x2') and
           _coord(x.group(0), 'y1') != _coord(x.group(0), 'y2')
    )

# ── vol3/vol4: arch in JSON QUESTIONS ──────────────────────────────────────────
for vol in ['vol3', 'vol4']:
    path = f"az305/{vol}.html"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'(const QUESTIONS = )(\[.*?\]);', content, re.DOTALL)
    prefix = m.group(1)
    qs = json.loads(m.group(2))

    fixed_qs = 0
    fixed_lines = 0
    for q in qs:
        exp = q.get('exp_html', '')
        if '<line' not in exp:
            continue
        before = count_diag(exp)
        new_exp = fix_svgs(exp)
        after = count_diag(new_exp)
        if new_exp != exp:
            fixed_lines += (before - after)
            fixed_qs += 1
            q['exp_html'] = new_exp

    new_json = json.dumps(qs, ensure_ascii=False, separators=(',', ':'))
    new_content = content[:m.start()] + prefix + new_json + ';' + content[m.end():]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"{vol}: fixed {fixed_lines} diagonal lines in {fixed_qs} questions")

# ── vol5: arch in raw HTML ──────────────────────────────────────────────────────
path = "az305/vol5.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_diag = count_diag(content)
new_content = re.sub(
    r'<div class="arch-box">.*?</svg></div>',
    lambda m: fix_svgs(m.group(0)),
    content,
    flags=re.DOTALL
)
fixed_lines = old_diag - count_diag(new_content)
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"vol5: fixed {fixed_lines} diagonal lines")
