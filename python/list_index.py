alist = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']

prev = None
curr = alist[0]

for nxt in alist[1:] + [None]:
    print(f'prev: {prev}, curr: {curr}, next: {nxt}')
    prev = curr
    curr = nxt
