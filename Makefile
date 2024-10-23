all:
	python -m unittest tests/EmpresaTest.py tests/FuncionarioTest.py tests/ProjetoTest.py

coverage:
	coverage run --source=src -m unittest tests/EmpresaTest.py tests/FuncionarioTest.py tests/ProjetoTest.py && coverage html
