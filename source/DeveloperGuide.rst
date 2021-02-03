Developer Guide
===============

.. note::
    This page describes information for RELION developers and code contributors.
    General users do not need information here.

Coding styles in C++
--------------------

Indentation should be done with tabs, while alignment should be done with spaces.

New lines should be as follows.
Note that due to limitation of rST syntax, I used spaces instead of tabs.

::

    // Use this
    void test(int a, int b)
    {
        if (!flag)
        {
            A();
            B();
        }
        else
        {
            C();
            D();
        }
    }

    // Not this
    void test(int a, int b) {
        if (!flag) {
            A();
            B();
        } else {
            A();
            B();
        }
    }

How to compile this documentation
---------------------------------

To compile this documentation into HTML, type::

    make html

For PDF, perform::

    make latex
    cd build/latex
    pdflatex relion.tex # you might have to install several style files

If your system has ``latexmk``, this can be done in one line::

    make latexpdf

If above commands complain about missing Python packages, try::

    python3 -m pip install --upgrade sphinx sphinxcontrib-bibtex

Coding styles in reStructuredText (rST)
---------------------------------------

To make ``git diff`` easier to understand, each sentense should use a new line.

::

    A sentence.
    Next sentence.

    A new paragraph.
    ``Keyword``, *emphasis by italic* and **emphasis by bold** are marked like this.
    You can cite a paper :cite:`Zivanov_estimation_2019`.
    A link to `rST documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.
    Note the underline.

    We have custom tags for :button:`buttons`, :joblist:`joblists`, :jobtype:`jobtypes` and :guitab:`guitabs`.
    |RELION| prints RELION in smallscaps.
    We also have |MotionCor2| and |CTFFIND4.1| defined.

    This paragram is a bad example. Two sentences are in one line.

    ::

        A block quote for commands is an indented block following two
        colons and an empty line.

    -   When using a list, be careful about indentation.
        The second sentence must be aligned.
    -   The second item in the list.

    :Field list: suggested value

        (Explanation sentence 1.
        Note the indentation of this line!
        Also note the following blank line.)

    :Another option without a value: \

        (Please put `\` at the end of the line to the field that should be left empty.)

The above example is rendered as:

A sentence.
Next sentence.

A new paragraph.
``Keyword``, *emphasis by italic* and **emphasis by bold** are marked like this.
You can cite a paper :cite:`Zivanov_estimation_2019`.
A link to `rST documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.
Note the underline.

We have custom tags for :button:`buttons`, :joblist:`joblists`, :jobtype:`jobtypes` and :guitab:`guitabs`.
|RELION| prints RELION in smallscaps.
We also have |MotionCor2| and |CTFFIND4.1| defined.

This paragram is a bad example. Two sentences are in one line.

::

    A block quote for commands is an indented block following two
    colons and an empty line.

-   When using a list, be careful about indentation.
    The second sentence must be aligned.
-   The second item in the list.

:Field list: suggested value

    (Explanation sentence 1.
    Note the indentation of this line!
    Also note the blank lines.)

:Another option without a value: \

    (Please put ``\`` at the end of the line to the field that should be left empty.)