"""gen_vol6_v2.py – Re-generate vol6.html with enhanced exp_html from vol6_exp.py."""
import sys, os, json
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import base questions (runs data-building only; file-write guarded by __name__)
import gen_vol6

# Import all enhanced exp functions
from vol6_exp import (
    exp_q1,  exp_q2,  exp_q3,  exp_q4,  exp_q5,  exp_q6,  exp_q7,
    exp_q8,  exp_q9,  exp_q10, exp_q11, exp_q12, exp_q13, exp_q14,
    exp_q15, exp_q16, exp_q17, exp_q18, exp_q19, exp_q20, exp_q21,
    exp_q22, exp_q23, exp_q24, exp_q25, exp_q26, exp_q27, exp_q28,
    exp_q29, exp_q30, exp_q31, exp_q32, exp_q33, exp_q34, exp_q35,
    exp_q36, exp_q37, exp_q38,
)

EXP_FUNCS = [
    exp_q1,  exp_q2,  exp_q3,  exp_q4,  exp_q5,  exp_q6,  exp_q7,
    exp_q8,  exp_q9,  exp_q10, exp_q11, exp_q12, exp_q13, exp_q14,
    exp_q15, exp_q16, exp_q17, exp_q18, exp_q19, exp_q20, exp_q21,
    exp_q22, exp_q23, exp_q24, exp_q25, exp_q26, exp_q27, exp_q28,
    exp_q29, exp_q30, exp_q31, exp_q32, exp_q33, exp_q34, exp_q35,
    exp_q36, exp_q37, exp_q38,
]

# Copy questions and replace exp_html with enhanced versions
QUESTIONS = [dict(q) for q in gen_vol6.QUESTIONS]
for q, fn in zip(QUESTIONS, EXP_FUNCS):
    q['exp_html'] = fn()

# Rebuild JSON and inject into existing HTML template
TOTAL = len(QUESTIONS)
domain_counts = Counter(q["domain"] for q in QUESTIONS)
new_json = json.dumps(QUESTIONS, ensure_ascii=False, separators=(',', ':'))
HTML = gen_vol6.HTML.replace(gen_vol6.QUESTIONS_JSON, new_json, 1)

# ── Write ─────────────────────────────────────────────────────────────────────
out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'vol6.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"Generated {out_path} with {TOTAL} questions (enhanced exp_html)")
print("Domain distribution:", dict(domain_counts))
