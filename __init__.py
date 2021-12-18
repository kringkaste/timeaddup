from albert import *
import timecalc

__title__ = "Time add up"
__version__ = "0.0.1"
__triggers__ = "t "

def handleQuery(Query):

    if not Query.isTriggered:
        return

    result = timecalc.calc(Query)

    return Item(id=__title__,
                text=result,
                actions=[
                    ClipAction(text=result,
                               clipboardText=result)
                ])