seq1 = [1, 2.3, 'dfg', "ewrwer", True, (4, 6, 1e+10, '12'), 1.123e+10,
        {'u_id': 'bv1244513', 'name_id': 'dfsgfhystr'}, [1, 2, 3, 4]]
for i in seq1:
    if type(i) in (tuple, dict, list):
        print(type(i))
        for j in i:
            print(f'    ', type(j))
    else:
        print(type(i))
