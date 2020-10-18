# Entrada da verificação se a pessoa esta com tosse, febre e/ou dificuldade na respiração
tosse = input()
febre = input()
dif_res = input()

tosse_bool = tosse == "True"
febre_bool = febre == "True"
dif_res_bool = dif_res == "True"
res = tosse_bool and febre_bool and dif_res_bool

print("Tosse:", tosse_bool)
print("Febre:", febre_bool)
print("Dificuldade para respirar:", dif_res_bool)
print("Provavelmente eh COVID-19:", res)
