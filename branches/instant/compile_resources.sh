#!/bin/sh

echo "Regenerating Traxter parser"
apr -f -d StupidSheet/compiler/ StupidSheet/compiler/traxter.apr
exit
echo "Compiling UI files"
for ui in StupidSheet/ui/*.ui
do
  pyuic4 $ui -o `dirname $ui`/Ui_`basename $ui .ui`.py
done
echo "Compiling resource files"
for qrc in StupidSheet/ui/*.qrc
do
  pyrcc4 $qrc -o `dirname $ui`/`basename $ui .qrc`_rc.py
done
