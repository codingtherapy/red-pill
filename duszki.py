FIGURES = [('ghost', 'white'), ('armchair', 'red'), ('mouse', 'grey'), ('book', 'blue'), ('bottle', 'green')]

def test_solution():
    assert(solution(('ghost', 'blue'), ('armchair', 'red'))==('armchair', 'red'))
    assert(solution(('ghost', 'white'), ('armchair', 'grey'))==('ghost', 'white'))
    assert(solution(('ghost', 'blue'), ('armchair', 'green'))==('mouse', 'grey'))
    assert(solution(('mouse', 'blue'), ('bottle', 'white'))==('armchair', 'red'))

def test_filter():
    assert(filter(('ghost', 'grey'), ('armchair', 'blue'))==('bottle', 'green'))
    assert(filter(('ghost', 'green'), ('book', 'red'))==('mouse', 'grey'))

def filter(fig1, fig2):
    figures = dict([(fig, False) for fig in FIGURES])
    for fig in FIGURES:
        if fig1[0] == fig[0] or fig2[0] == fig[0] or fig1[1] == fig[1] or fig2[1] == fig[1]:
            figures[fig] = True
    return [fig for fig in figures if figures[fig] == False][0]

def solution(fig1, fig2):
    if fig1 in FIGURES:
        return fig1
    elif fig2 in FIGURES:
        return fig2
    else:
        return filter(fig1, fig2)

if __name__=='__main__':
    test_solution()
