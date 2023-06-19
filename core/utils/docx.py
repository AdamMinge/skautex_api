# Python Import
import re
from docx.shared import Pt


def __bold_formatters(run):
    run.bold = True


def __italic_formatters(run):
    run.italic = True


def try_formatters(run):
    style_formatters = {
        '<i>(.*)</i>': __italic_formatters,
        '<b>(.*)</b>': __bold_formatters
    }

    for regex, formatters in style_formatters.items():
        match = re.match(regex, str(run.text))
        if match:
            formatters(run)
            run.text = match.group(1)
            return


def format_paragraph(paragraph, text, **kwargs):
    styled_texts = re.findall('<.+>.*</.+>', text)
    normal_texts = re.split('<.+>.*</.+>', text)

    texts = []
    for i in range(len(styled_texts) + len(normal_texts)):
        texts.append(normal_texts[i // 2] if not i % 2 else styled_texts[i // 2])

    for text in texts:
        added_run = paragraph.add_run(text)
        try_formatters(added_run)

        if 'font_size' in kwargs:
            added_run.font.size = Pt(int(kwargs['font_size']))
