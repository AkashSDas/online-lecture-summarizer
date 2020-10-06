import re


def clean_text(column):
    for row in column:
        row = re.sub("(\\t)", ' ', str(row)).lower()
        row = re.sub("(\\r)", ' ', str(row)).lower()
        row = re.sub("(\\n)", ' ', str(row)).lower()

        row = re.sub("(__+)", ' ', str(row)).lower()
        row = re.sub("(--+)", ' ', str(row)).lower()
        row = re.sub("(~~+)", ' ', str(row)).lower()
        row = re.sub("(\+\++)", ' ', str(row)).lower()
        row = re.sub("(\.\.+)", ' ', str(row)).lower()

        row = re.sub(r"[<>()|&©ø\[\]\'\",;?~*!]", ' ', str(row)).lower()

        row = re.sub("(mailto:)", ' ', str(row)).lower()
        row = re.sub(r"(\\x9\d)", ' ', str(row)).lower()
        row = re.sub("([iI][nN][cC]\d+)", 'INC_NUM', str(row)).lower()
        row = re.sub("([cC][mM]\d+)|([cC][hH][gG]\d+)",
                     'CM_NUM', str(row)).lower()

        row = re.sub("(\.\s+)", ' ', str(row)).lower()
        row = re.sub("(\-\s+)", ' ', str(row)).lower()
        row = re.sub("(\:\s+)", ' ', str(row)).lower()
        row = re.sub("(\s+.\s+)", ' ', str(row)).lower()

        try:
            url = re.search(r'((https*:\/*)([^\/\s]+))(.[^\s]+)', str(row))
            repl_url = url.group(3)
            row = re.sub(
                r'((https*:\/*)([^\/\s]+))(.[^\s]+)', repl_url, str(row))
        except:
            pass

        row = re.sub("(\s+)", ' ', str(row)).lower()
        row = re.sub("(\s+.\s+)", ' ', str(row)).lower()

        yield row
