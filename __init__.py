from albert import *
import os
import timecalc

__title__ = "Time add up"
__version__ = "0.0.1"
__triggers__ = "t "
__authors__ = "kringkaste"

def handleQuery(Query):

    if not Query.isTriggered:
        return

    result = timecalc.calc(Query.string)

    return Item(id=__title__,
                text=result,
                icon=os.path.dirname(__file__)+"/clock.svg",
                actions=[
                    ClipAction(text=result,
                               clipboardText=result)
                ])