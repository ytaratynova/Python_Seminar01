# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

x = [True, False]
y = [True, False]
z = [True, False]

for i in x:
    for j in y:
        for k in z:
            # print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для X {x[i]}, Y {y[j]}, Z {z[k]}: {not(not (x[i] or y[j] or z[k]) != (not x[i]) and (not y[j]) and (not z[k]))}')
           logic1 = not (x[i] or y[j] or z[k])
           logic2 = (not x[i]) and (not y[j]) and (not z[k])

           if logic1 == logic2:
                print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для X {x[i]}, Y {y[j]}, Z {z[k]}: уверждение истинноe')
           else:
                print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для X {x[i]}, Y {y[j]}, Z {z[k]}: уверждение ложноe')