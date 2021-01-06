# taxi = {}
# while True:
#     st = input()
#     if st == "конец":
#         break
#     else:
#         data = st.split(", ")
#         taxi.setdefault(data[0],[]).append(int(data[1]))
#
# for driver in taxi:
#     taxi[driver] = sum(taxi[driver])/len(taxi[driver])
taxi = {'Джек': 2.5, 'Билл': 4.0, 'Антуан': 4.0}

# for driver in reversed(sorted(taxi.items(), key = lambda zz : (zz[1],zz[0]))):
#     print(*driver)
