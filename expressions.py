from mutation import *
import random
"""
Expression list
* Initialise
* Operator
* Conditional
"""
def div(a,b):
    if b != 0:
        return a/b
    else:
        return a/(b+1)
def mod(a,b):
    if b != 0:
        return a%b
    else:
        return a%(b+1)

class Initialise:
    def __init__(self, name, val, indent=0):
        self.name = name
        self.val = val
        self.indent = indent
    def __str__(self):
        return '\t'*self.indent + self.name + ' = ' + self.val

class Operator:
    def __init__(self, name, val1, op, val2, indent=0):
        self.name = name
        self.val1 = val1
        self.op = op
        self.val2 = val2
        self.indent = indent
    def __str__(self):
        if self.op in ['+', '-', '*']:
            return '\t'*self.indent + self.name + ' = ' + self.val1 + ' ' + self.op + ' ' + self.val2
        elif self.op == "div" or self.op == "mod":
            # print(self.op)
            return '\t' * self.indent + self.name + ' = ' + self.op + '(' + self.val1 + ', ' + self.val2 + ')'

class Conditional:
    def __init__(self, val1, ineq, val2, block, indent=0):
        self.val1 = val1
        self.ineq = ineq
        self.val2 = val2
        self.block = block
        self.indent = indent
    def __str__(self):
        return '\t'*self.indent + "if " + self.val1 + ' ' + self.ineq + ' '+ self.val2 + ":" + "".join(["\n\t" + str(exp) for exp in self.block])

class Function:
    def __init__(self, name, chro, new=True):
        self.name = name
        self.vars = ['v0']
        self.chro = chro
        self.exp_lst = self.create_exp_lst(self.chro, new=True)
        self.func_str = self.create_func()
        self.stats = {
            'create': 0,
            'modify': 0,
            'delete': 0,
            'c_initialise': 0,
            'c_assign': 0,
            'c_if': 0,
            'm_variable': 0,
            'm_operator': 0,
            'm_if': 0,
        }

    def mutate(self):
        # Create
        decision = random.random()
        if decision < probabilities['create']:
            self.stats['create'] += 1
            action = random.random()
            if action < create['initialise']:
                self.stats['c_initialise'] += 1
                gene = self.c_initialise()
                if gene:
                    self.chro.append(gene)
            elif action < create['assign']:
                self.stats['c_assign'] += 1
                gene = self.c_assign()
                if gene:
                    self.chro.append(gene)
            elif action < create['if']:
                self.stats['c_if'] += 1
                gene = self.c_if()
                if gene:
                    self.chro.append(gene)

        elif decision < probabilities['modify']:
            self.stats['modify'] += 1
            action = random.random()
            if action < modify['variable']:
                self.stats['m_variable'] += 1
                self.m_variable()
            elif action < modify['operator']:
                self.stats['m_operator'] += 1
                self.m_operator()
            elif action < modify['if']:
                self.stats['m_if'] += 1
                self.m_if()
        # elif decision < probabilities['delete']:
        #         self.delete()
        # for c in self.chro:
        #     print(c)
        # print(self.chro)
        self.exp_lst = self.create_exp_lst(self.chro, new=False)
        self.func_str = self.create_func()

    def c_initialise(self, indent=0):
        # print("c_initialise")
        # Creates a new initialisation
        n = len(self.vars)
        self.vars.append('v' + str(n))
        return ['I', ['v'+str(n), '0', indent]]

    def c_assign(self, indent=0):
        # print("c_assign")
        # Create a new assignment
        n = random.randint(0, len(self.vars)-1)
        op = random.choice(['+', '-', '*', 'div', 'mod'])
        var1 = random.choice(self.vars)
        var2 = random.choice(self.vars)
        # if (op == '%' or op == '/') and ll[var2] == 0:
        #     # print(var2+1)
        #     return ['O', ['v'+str(n), var1, op, var2+1, indent]]
        # else:
        return ['O', ['v'+str(n), var1, op, var2, indent]]
        # self.vars.append('v' + str(n))


    def c_if(self, indent=0):
        # print("c_if")
        n = len(self.vars)
        ineq = random.choice(['>', '<', '=='])
        var1 = random.choice(self.vars)
        var2 = random.choice(self.vars)
        # self.vars.append('v' + str(n))

        g_c = random.random()
        if g_c < 0.5:
            g = self.c_assign(indent=indent+1)
        else:
            g = self.c_if(indent=indent+1)

        if g:
            g = [g]
        else:
            g = []
        return ['C', [var1, ineq, var2, g, indent]]

    def m_variable(self):
        # print("m_variable")
        chros = []
        for c in self.chro:
            if c[0] == 'I' or c[0] == 'C':
                chros.append(c)
        if chros:
            # print(chros)
            chro = random.choice(chros)
            if chro[0] == 'I':
                # print(chro[1][1])
                chro[1][1] = str(int(chro[1][1]) + random.choice([1,-1]))
                # print(chro[1][1])
            elif chro[0] == 'C':
                if chro[1][3][0][0] == 'I':
                    v = chro[1][3][0][1][1]
                    chro[1][3][0][1][1] = str(int(v) + random.choice([1, -1]))

    def m_operator(self):
        # print("m_operator")
        chros = []
        for c in self.chro:
            if c[0] == 'O':
                chros.append(c)
        if chros:
            chro = random.choice(chros)
            chro[1][2] = random.choice(['+','-','*','div','mod'])

    def m_if(self):
        # print("m_if")
        chros = []
        for c in self.chro:
            if c[0] == 'C':
                chros.append(c)
        if chros:
            chro = random.choice(chros)
            chro[1][1] = random.choice(['<', '>', '=='])

    # def delete(self):
    #     """Deleting 1 line might make the code unrunnable."""
    #     self.exp_lst.pop(random.randrange(len(self.exp_lst)))

    def create_exp_lst(self, chro, new, indent=0):
        # Create exp list
        exp_lst = []
        for c in chro:
            if c[0] == 'I':
                e = Initialise(*c[1])
                if new:
                    self.vars.append(e.name)
            elif c[0] == 'O':
                e = Operator(*c[1])
                if new:
                    self.vars.append(e.name)
            elif c[0] == 'C':
                e = Conditional(c[1][0], c[1][1], c[1][2], self.create_exp_lst(c[1][3], new=False, indent=indent+1), indent=indent)
            exp_lst.append(e)
        return exp_lst

    def create_func(self):
        f = "def " + self.name + "(v0):"
        for e in self.exp_lst:
            f += "\n\t" + str(e)
        f += "\n\treturn " + "v0"
        return f
    def __str__(self):
        return self.func_str


"""
from expressions import *
e1 = Initialise("v1", '0')
e2 = Operator("v2", "v1", "+", "v1")
e3 = Conditional("v2", "<", "v1", ["print(\"successful\")"])
"""