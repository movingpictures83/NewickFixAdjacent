import sys

def isDigit(c):
    return ((c=='0') or (c=='1') or (c=='2') or (c=='3') or (c=='4') or (c=='5') or (c=='6') or (c=='7') or (c=='8') or (c=='9'))

class NewickFixAdjacentPlugin:
    def input(self, filename):
       infile = open(filename, 'r')
       self.mystr = infile.read()

    def run(self):
       i = 0
       self.newstr = ""
       while (i+1 < len(self.mystr)):
          if (self.mystr[i] == ')'):
              #self.newstr += self.mystr[i];
              #i += 1
              #while (i < len(self.mystr) and isDigit(self.mystr[i])):
              if (isDigit(self.mystr[i+1])):
                    self.newstr += self.mystr[i] + ':1,'
              else:
                 self.newstr += self.mystr[i]
              #    i += 1
              #if (i != len(self.mystr)):
              #self.newstr += self.mystr[i];
          else:
              self.newstr += self.mystr[i]
          i += 1

       while (i < len(self.mystr)):
           self.newstr += self.mystr[i]
           i += 1

    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.newstr)
       outfile.write("\n")
