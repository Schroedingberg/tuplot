
for file in *.txt; do
    sed -E -e 's/\s+//' $file | sed -E  -e 's/\s+/,/g' | sed -E -e 's/,//3' > results_cleaned/$file
done
# 1. Entferne alle Folgen Leerzeichen in der Datei, die am Anfang einer Zeile stehen.
# 2. Ersetze alle noch übrigen Folgen von Leerzeichen durch ein Komma.
# 3. Entferne in jeder Zeile das dritte Komma, damit beim Einlesen keine leere Spalte entsteht.


