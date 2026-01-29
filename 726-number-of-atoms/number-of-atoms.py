class Solution(object):
    def count_simple(self, s):
        elements = set()
        d = dict()
        for i in range(len(s)):
            if s[i].isalpha() and s[i].isupper(): #Get elements
                j = i + 1
                while j < len(s) and s[j].isalpha() and s[j].islower():
                    j += 1
                elements.add(s[i:j])
             
        elements = list(elements) # list of elements
        for e in elements:
            list_index = []
            for i in range(len(s)):
                if s.startswith(e, i):
                    if (i + len(e) < len(s) and not s[i+len(e)].islower()):
                        list_index.append(i)
                    elif i +len(e) >= len(s):
                        list_index.append(i)
            count = 0
            for i in list_index:
                number = ''
                j = i+len(e)
                while j < len(s) and s[j].isdigit():
                    number += s[j]
                    j+=1
                if number != '':
                    count += int(number)
                else: count +=1
            d[e] = count
        print(d)
        return d       
        
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        temp = formula.find(")")        
        while temp >0:
            a = formula[temp::-1]
            index_start = len(a) - a.find("(") -1
            sub_formula = formula[index_start+1:temp]
            d2 = self.count_simple(sub_formula)
            # Get the number after ')'
            number = ''
            m = temp+1
            while m < len(formula) and formula[m].isdigit():
                number += formula[m]
                m+=1
            s = ''
            for key, value in d2.items():
                if len(number) >0:
                    s = s + key + str(value * int(number)) 
                else:
                    s = s + key + str(value)  
            formula = formula[:index_start] + s + formula[temp+len(number)+1:]
            temp = formula.find(")")
        d = self.count_simple(formula)
        sorted_keys = sorted(d.keys())
        s = ''
        for key in sorted_keys:
            s = s + key + str(d[key]) if d[key] > 1 else s + key
        return s      