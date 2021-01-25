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

Coding styles in rST
--------------------

To make Git diff easier to understand, each sentense should use a new line.

::

    A sentence.
    Next sentence.

    A new paragraph.

    -   When using a list, be careful about indentation.
        The second sentence must be aligned.

    :same for: option lists.
        (Explanation sentenec 1.
        Note the indentation of this line!)

    This paragram is a bad example. Two sentences are in one line.

The above example is rendered as:

A sentence.
Next sentence.

A new paragraph.

-   When using a list, be careful about indentation.
    The second sentence must be aligned.

:same for: option lists.
    (Explanation sentenec 1.
    Note the indentation of this line!)

This paragram is a bad example. Two sentences are in one line.