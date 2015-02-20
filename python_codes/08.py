import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq, solve

def narrowPhaseLine(formula):
    solutions = solve(Eq(formula,0),y(t))
    solutions.sort()
    ran = solutions[-1]-solutions[0]
    ydomain = np.linspace(float(solutions[0]-0.25*ran), float(solutions[-1]+0.25*ran))
    fig = plt.figure(num=1, figsize=(1,4))

    plt.plot([0 for dummy in ydomain],ydomain, color = 'black')
    plt.plot([0 for dummy in solutions], solutions, 'or')
    plt.axis(xmin = -0.5, xmax = 0.5)
    intervals = [float(solutions[0]-0.25*ran)]+solutions+[float(solutions[-1]+0.25*ran)]
    for i in range(len(intervals)-1):
        midpoint = (intervals[i]+intervals[i+1])/2.0
        intervalSign = sign(formula.evalf(subs={'y(t)':midpoint}))
        if intervalSign == -1:
            plt.text(0, midpoint, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
        elif intervalSign == 1:
            plt.text(0, midpoint, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
    return fig

a = [0, -0.125, -0.25, -0.375]



y = Function('y')
formula = y(t)*(1-y(t))-0.125
fg = narrowPhaseLine(formula)
fg.show()
