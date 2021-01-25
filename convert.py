# This is the script used to convert the original LaTeX source code.
# Added only for archival purpose.
# This script must be executed with LC_ALL=en_US.utf8

import re
import sys

with open("relion31_tutorial.tex") as f:
    inp = f.read()

    inp = inp.replace(r"{\AA}", u"\u212b")
    inp = inp.replace(r"\AA", u"\u212b")
    inp = inp.replace(r"OR:", "OR\:")
    inp = inp.replace(r"\citep", r"\cite")

    inp = inp.replace(r"''", r"``")
    inp = inp.replace(r"*", r"\*")

    # job paramaters
    inp = inp.replace(r"\begin{itemize}", "")
    inp = inp.replace(r"\end{itemize}", "") 
    inp = re.sub(r"\\entry(newline)?\{([^}]*)\}\{([^}]*)\}([^\n]+)", r":\2: \3\n\n    \4\n", inp)
    inp = re.sub(r"\\entry(newline)?\{([^}]*)\}\{([^}]*)\}", r":\2: \3\n", inp)

    inp = re.sub(r"\\item\{([^}]+)\}", r"- \1", inp) # sometimes fails
    inp = inp.replace(r"\item ", "- ")

    # ref
    inp = re.sub(r"\\ref\{sec:([^}]+)\}", r":ref:`sec_\1`", inp)

    # href
    inp = re.sub(r"\\href\{([^}]+)\}\{([^}]+)\}", r"`\2 <\1>`_", inp)

    # verbatim
    inp = re.sub(r"\\begin\{verbatim\}(.+?)\\end\{verbatim\}",
                 lambda m: "::\n" + "\n".join(["    " + x for x in m.group(1).split("\n")]), inp, flags=re.DOTALL)

    # typewriter
    inp = re.sub(r"\\verb\+([^+]*)\+", r"`\1`", inp)
    inp = re.sub(r"\\texttt\{([^}]+)\}", r"`\1`", inp)

    # italic
    inp = re.sub(r"\\textit\{([^}]+)\}", r"*\1*", inp)

    # bold
    inp = re.sub(r"\\textbf\{([^}]+)\}", r"**\1**", inp)
    inp = re.sub(r"\\emph\{([^}]+)\}", r"**\1**", inp)

    # headers
    inp = inp.replace(r"\newpage", "")
    inp = re.sub(r"\\section\{([^}]+)\}",
                 lambda m: "\n" + m.group(1) + "\n" + ("=" * len(m.group(1))) + "\n", inp)
    inp = re.sub(r"\\subsection\{([^}]+)\}",
                 lambda m: "\n" + m.group(1) + "\n" + ("-" * len(m.group(1))) + "\n", inp)
    inp = re.sub(r"\\subsubsection\{([^}]+)\}",
                 lambda m: "\n" + m.group(1) + "\n" + ("^" * len(m.group(1))) + "\n", inp)

    # standard commands
    commands = ["joblist", "jobtype", "button", "cite", "textsc", "guitab", "runbutton"]
    for comm in commands:
        inp = re.sub(r"\\" + comm + r"\{([^}]*?)\}", ":" + comm + r":`\1`", inp)

    sys.stdout.write("""
.. role:: textsc
   :class: smallcaps
.. role:: button
.. role:: runbutton
.. role:: joblist
.. role:: jobtype
.. role:: guitab
.. |relion| replace:: :textsc:`relion`
""")
    sys.stdout.write(inp)
