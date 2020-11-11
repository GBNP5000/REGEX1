# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?<=>|\()[0-9\.,-]+"

test_str = ("<span class=\"span_price_wrap stprh grn_hilight grnclr\">1770.00</span>'\n"
            "b'<span class=\"span_price_arrow green_arwup\"></span>'\n"
            "b'<span class=\"span_price_change_prcnt grnpc1\">11.25 <em>(-0.64%)</em></")

matches = re.finditer(regex, test_str, re.MULTILINE)
print(matches)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                        start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
