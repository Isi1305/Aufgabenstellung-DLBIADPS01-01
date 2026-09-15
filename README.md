Das Repository ist nur dafür da Aufgaben besser zu visualisieren.

Aufgabenstellung 3: 
Die Bücher einer Bibliothek sollen mittels einer XML-Struktur verwaltet werden. Berücksichtige, dass ein Buch in 
mehreren Versionen/Editionen verfügbar sein kann. 
a) Erstelle dafür ein Document Type Declaration (DTD) für die XML-Struktur zur Erfassung der Bücher, inkl. 
Referenz zu einem Titelbild. 
b) Erstelle ein zugehöriges XML mit mindestens drei Büchern. 
c) Nutze XSLT, um die in der Bibliothek vorhanden Bücher als HTML-Seite darzustellen. 


Aufgabenstellung 4: 
Gegeben ist die Funktion naiveMatch und die zugehörige Testfunktion test_match_function() 
def naiveMatch(p,t): 
  if not p or not t: 
    return False 
  m = len(p) 
  n = len(t) 
  found = False 
  for i in range(n-m+1): 
    j=0 
    k=i 
    while j < m and i < n and p[j]==t[k]: 
      j+=1 
      k+=1 
      if j== m: 
        found = True 
  return found 
  
def test_match_function(): 
assert naiveMatch('abc','aaaa') == False, "NoMatch failed" 

a) Wie hoch ist die Codeabdeckung der naiveMatch-Funktion durch die Testfunktion? Welche Prüfungen 
müssen ergänzt werden, um eine hundertprozentige Abdeckung zu erreichen? 
b) Ändere die Funktion und die Tests so ab, dass die Anzahl der gefundenen Übereinstimmungen 
zurückgegeben wird und eine hundertprozentige Codeabdeckung erreicht wird.


Aufgabenstellung 6: 
Gegeben ist das folgende Programm in Haskell, das eine Zahl faktorisiert: 

factors n = [f | f <-[1..n], mod n f == 0] 
main = do 
print $ factors 

Wie würde dieses Programm in C mittels imperativer Programmierung realisiert werden? 
Diskutiere anhand dieses Beispiels wie sich die Paradigmen für imperative und funktionale Programmierung 
unterscheiden.
