"""Convert diagonal <line> arrows to orthogonal <path> in vol3/4/5 arch diagrams."""
import re, json

def line_to_ortho_path(m):
    """Replace <line x1 y1 x2 y2 ...marker-end.../> with orthogonal <path d=.../>."""
    tag = m.group(0)
    x1 = int(m.group(1)); y1 = int(m.group(2))
    x2 = int(m.group(3)); y2 = int(m.group(4))

    if x1 == x2 or y1 == y2:
        return tag  # already orthogonal, keep as-is

    # Bend: go horizontal to x2, then vertical to y2
    d = f"M{x1},{y1} L{x2},{y1} L{x2},{y2}"

    # Re-use all attributes except x1/y1/x2/y2, replace tag name
    attrs = tag
    attrs = re.sub(r'\bx1="[^"]*"', '', attrs)
    attrs = re.sub(r'\by1="[^"]*"', '', attrs)
    attrs = re.sub(r'\bx2="[^"]*"', '', attrs)
    attrs = re.sub(r'\by2="[^"]*"', '', attrs)
    attrs = re.sub(r'^<line\b', '', attrs)
    attrs = re.sub(r'/>\s*$', '', attrs).strip()

    return f'<path d="{d}" fill="none" {attrs}/>'

LINE_PAT = re.compile(
    r'<line\s+x1="(\d+)"\s+y1="(\d+)"\s+x2="(\d+)"\s+y2="(\d+)"([^/]*)/>',
    re.DOTALL
)

def fix_svgs(svg_block):
    """Fix all diagonal line arrows in an SVG block."""
    return LINE_PAT.sub(line_to_ortho_path, svg_block)

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
        if 'arch-box' not in exp:
            continue
        new_exp = fix_svgs(exp)
        n = sum(1 for a, b in zip(exp.split('<line'), new_exp.split('<line')) if a != b)
        fixed = (exp != new_exp)
        if fixed:
            # Count how many lines were changed
            old_diag = len([x for x in LINE_PAT.finditer(exp)
                            if x.group(1) != x.group(3) and x.group(2) != x.group(4)])
            fixed_lines += old_diag
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

# Find and fix all arch-box SVG sections
def fix_arch_box(m):
    return fix_svgs(m.group(0))

old_diag = sum(
    1 for x in LINE_PAT.finditer(content)
    if x.group(1) != x.group(3) and x.group(2) != x.group(4)
)
new_content = re.sub(
    r'<div class="arch-box">.*?</svg></div>',
    fix_arch_box,
    content,
    flags=re.DOTALL
)
fixed_lines = old_diag - sum(
    1 for x in LINE_PAT.finditer(new_content)
    if x.group(1) != x.group(3) and x.group(2) != x.group(4)
)
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"vol5: fixed {fixed_lines} diagonal lines")
