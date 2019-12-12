import os

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pyemu_basics.ipynb")
os.system("jupyter nbconvert --to pdf pyemu_basics.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace pyemu_basics.ipynb")

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace setup_pest_interface.ipynb")
os.system("jupyter nbconvert --to pdf setup_pest_interface.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace setup_pest_interface.ipynb")

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace prior_monte_carlo.ipynb")
os.system("jupyter nbconvert --to pdf prior_monte_carlo.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace prior_monte_carlo.ipynb")

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pestpp-glm_part1.ipynb")
os.system("jupyter nbconvert --to pdf pestpp-glm_part1.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace pest_glm_part1.ipynb")

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace dataworth.ipynb")
os.system("jupyter nbconvert --to pdf dataworth.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace dataworth.ipynb")

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pestpp-glm_part2.ipynb")
os.system("jupyter nbconvert --to pdf pestpp-glm_part2.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace pest_glm_part2.ipynb")

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pestpp-ies.ipynb")
os.system("jupyter nbconvert --to pdf pestpp-ies.ipynb")
os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace pestpp-ies.ipynb")